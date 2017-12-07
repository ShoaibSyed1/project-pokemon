from enum import Enum

import pygame
from pygame.math import Vector2

from game.components import ScriptComponent, Transform
from game.components.ui import Element
from game.scripts.script import Script

class UiController(Script):
    def __init__(self):
        self.mouse_x = 0
        self.mouse_y = 0
    
    def update(self, delta):
        pass
    
    def on_event(self, event):
        for ent, (element, script_comp, transform) in self.world.get_components(Element, ScriptComponent, Transform):
            element_size = Vector2(element.size.x * transform.scale.x, element.size.y * transform.scale.y)

            if event.type == pygame.MOUSEMOTION:
                if is_inside(event.pos, transform.pos, element_size):
                    script_comp.script.on_ui_event(
                        UiEvent(UiEventType.MOUSE_HOVER,
                                Vector2(event.pos[0] - transform.pos.x, event.pos[1] - transform.pos.y)))
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if is_inside(event.pos, transform.pos, element_size):
                    script_comp.script.on_ui_event(
                        UiEvent(UiEventType.MOUSE_DOWN,
                                Vector2(event.pos[0] - transform.pos.x, event.pos[1] - transform.pos.y)))
            elif event.type == pygame.MOUSEBUTTONUP:
                if is_inside(event.pos, transform.pos, element_size):
                    script_comp.script.on_ui_event(
                        UiEvent(UiEventType.MOUSE_UP,
                                Vector2(event.pos[0] - transform.pos.x, event.pos[1] - transform.pos.y)))
    

def is_inside(mouse_pos, pos, size):
    return mouse_pos[0] > pos.x and mouse_pos[1] > pos.y and mouse_pos[0] < (pos.x + size.x) and mouse_pos[1] < (pos.y + size.y)

class UiEvent:
    def __init__(self, type, data):
        self.type = type
        self.data = data

class UiEventType(Enum):
    MOUSE_HOVER = 0
    MOUSE_DOWN = 1
    MOUSE_UP = 2