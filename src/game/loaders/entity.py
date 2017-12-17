import json

class EntityLoader:
    def load(path, world, merge=None):
        entity_info = EntityLoader.load_obj(path)
        
        return EntityLoader.load_from(entity_info, world, merge)
    
    def load_obj(path):
        import game

        path = "assets/entities/" + path + ".json"
        entity_info = None
        with open(path) as file:
            entity_info = json.load(file)
        
        if entity_info.get('parent', None) != None:
            parent_info = EntityLoader.load_obj(entity_info['parent'])
            entity_info['parent'] = None

            entity_info = game.deepupdate(parent_info, entity_info)
        
        return entity_info

    def load_from(entity_info, world, merge=None):
        import game
        from game import components, uuids
        from game.loaders import SpriteLoader
        
        if entity_info.get('parent', None) != None:
            parent_info = EntityLoader.load_obj(entity_info['parent'])
            entity_info['parent'] = None
            
            entity_info = game.deepupdate(parent_info, entity_info)
        
        if merge != None:
            entity_info = game.deepupdate(entity_info, merge)
        
        comps = []
        
        for key, value in entity_info.items():
            if key == 'sprite':
                sprite_loader = SpriteLoader(value)
                sprite, anim, anim_groups = sprite_loader.load()
                comps.append(sprite)
                comps.append(anim)
                comps.append(anim_groups)
            elif key == 'uuid':
                comps.append(components.get('uuid', uuids.get(value)))
            elif key == 'script':
                script_class = getattr(__import__("game.scripts" + value['path'], globals(), fromlist=[value['class']]), value['class'])
                script = None
                if "args" in value.keys():
                    script = script_class(value['args'])
                else:
                    script = script_class()
                comps.append(components.get('script', script))
            elif key == 'parent':
                continue
            else:
                comps.append(components.get(key, value))
        
        return world.create_entity(*comps)