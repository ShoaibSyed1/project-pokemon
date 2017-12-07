import json

from pygame.math import Vector2

from game.components import ScriptComponent, Transform
from game.components.ui import Element
from game.loaders.sprite import SpriteLoader
from game.scripts.ui import Button

class UiLoader:
    def __init__(self, path):
        self.path = "assets/ui/" + path + ".json"
    
    def start(self, world):
        ui_info = None
        with open(self.path) as file:
            ui_info = json.load(file)
        
        entities = []
        
        for key, value in ui_info.items():
            self.create(entities, value, world)
        
        return entities

    def create(self, entities, value, world):
        x = value['x']
        y = value['y']
        scale_x = value['scale_x']
        scale_y = value['scale_y']
        width = value['width']
        height = value['height']

        element = Element(Vector2(width, height))
        script_comp = None
        transform = Transform(Vector2(x, y), Vector2(scale_x, scale_y))
        
        element_type = value['element']
        if element_type == 'button':
            script_comp = ScriptComponent(Button())
        
        sprite_path = value['sprite']
        sprite_loader = SpriteLoader(sprite_path)
        spr, anim, anim_groups = sprite_loader.load()

        entities.append(world.create_entity(
            element,
            script_comp,
            transform,
            spr,
            anim,
            anim_groups
        ))