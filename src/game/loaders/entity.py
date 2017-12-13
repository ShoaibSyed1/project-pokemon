import json

class EntityLoader:
    def __init__(self, path):
        self.path = "assets/entities/" + path + ".json"
    
    def load(self, world):
        from game import components, uuids
        from game.loaders import SpriteLoader

        entity_json = None
        with open(self.path) as file:
            entity_json = json.load(file)
        
        comps = []
        
        for key, value in entity_json.items():
            if key == 'sprite':
                sprite_loader = SpriteLoader(value)
                sprite, anim, anim_groups = sprite_loader.load()
                comps.append(sprite)
                comps.append(anim)
                comps.append(anim_groups)
            elif key == 'uuid':
                comps.append(components.get('uuid', uuids.get(value)))
            else:
                comps.append(components.get(key, value))
        
        return world.create_entity(*comps)