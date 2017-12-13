import json

class SceneLoader:
    def load(path, world):
        from game import processors
        from game.loaders import EntityLoader, UiLoader

        path = "assets/scenes/" + path + ".json"

        scene_info = None
        with open(path) as file:
            scene_info = json.load(file)
        
        if 'entities' in scene_info.keys():
            for entity in scene_info['entities']:
                EntityLoader.load_from(entity, world)
        
        if 'processors' in scene_info.keys():
            for processor_info in scene_info['processors']:
                name = processor_info['name']
                priority = processor_info.get('priority', 0)

                world.add_processor(processors.get(name, None), priority)
        
        if 'ui' in scene_info.keys():
            UiLoader(scene_info['ui']).load(world)