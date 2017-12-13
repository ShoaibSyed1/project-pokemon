import json

import pygame
from pygame.math import Vector2

from game.components import EventListener, ScriptComponent, Transform
from game.components.ui import Element
from game.loaders.sprite import SpriteLoader
from game.scripts.ui import Button, Textbox

class UiLoader:
    def __init__(self, path):
        self.path = "assets/ui/" + path + ".json"
    
    def load(self, world):
        ui_info = None
        with open(self.path) as file:
            ui_info = json.load(file)
        
        entities = []
        
        for key, value in ui_info.items():
            self.create(key, entities, value, world)
        
        return entities

    def create(self, name, entities, value, world):
        x = value['x']
        y = value['y']
        scale_x = value['scale_x']
        scale_y = value['scale_y']
        width = value['width']
        height = value['height']

        element = Element(name, Vector2(width, height), Vector2(x, y))
        script_comp = None
        transform = Transform({
            'pos': Vector2(x, y),
            'scale': Vector2(scale_x, scale_y)
        })

        sprite_path = value['sprite']
        sprite_loader = SpriteLoader(sprite_path)
        spr, anim, anim_groups = sprite_loader.load()
        
        element_type = value['element']
        if element_type == 'button':
            script_comp = ScriptComponent(Button())
            entities.append(world.create_entity(
                element,
                script_comp,
                transform,
                spr,
                anim,
                anim_groups
            ))
        elif element_type == 'textbox':
            script_comp = ScriptComponent(Textbox())
            entites.append(world.create_entity(
                element,
                EventListener({
                    'events': ["KEYDOWN", "KEYUP", "MOUSEBUTTONDOWN", "MOUSEBUTTONUP", "MOUSEMOTION"]
                }),
                script_comp,
                transform,
                spr,
                anim,
                anim_groups
            ))