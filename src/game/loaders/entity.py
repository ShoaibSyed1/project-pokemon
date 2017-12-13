import json

class EntityLoader:
    def load(path, world):
        from game import components, uuids
        from game.loaders import SpriteLoader

        path = "assets/entities/" + path + ".json"

        entity_info = None
        with open(path) as file:
            entity_info = json.load(file)
        
        if entity_info.get('parent', None) != None:
            parent_path = entity_info['parent']
            parent_info = None
            with open(parent_path) as file:
                parent_info = json.load(file)
            
            for key, value in entity_info.items():
                parent_info[key] = value
            
            entity_info = parent_info
        
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
            else:
                comps.append(components.get(key, value))
        
        return world.create_entity(*comps)