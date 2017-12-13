import json

class EntityLoader:
    def load(path, world):
        path = "assets/entities/" + path + ".json"

        entity_info = None
        with open(path) as file:
            entity_info = json.load(file)
        
        return EntityLoader.load_from(entity_info, world)

    def load_from(entity_info, world):
        import game
        from game import components, uuids
        from game.loaders import SpriteLoader
        
        if entity_info.get('parent', None) != None:
            parent_path = "assets/entities/" + entity_info['parent'] + ".json"
            parent_info = None
            with open(parent_path) as file:
                parent_info = json.load(file)
            
            entity_info = game.deepupdate(parent_info, entity_info)
        
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