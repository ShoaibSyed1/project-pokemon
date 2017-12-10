from enum import Enum

import pygame
from pygame.math import Vector2

from game.components import ScriptComponent, Transform
from game.components.ui import Element
from game.scripts.script import Script

class UiController(Script):
    def __init__(self, camera_ent):
        self.mouse_x = 0
        self.mouse_y = 0

        self.camera_ent = camera_ent

        self.hold_tracking = set()
        self.hover_tracking = set()
    
    def start(self):
        self.camera_transform = self.world.component_for_entity(self.camera_ent, Transform)
    
    def update(self, delta):
        for ent, (element, transform) in self.world.get_components(Element, Transform)  :
            transform.pos = Vector2(self.camera_transform.pos.x + element.pos.x, self.camera_transform.pos.y + element.pos.y)
    
    def on_event(self, event):
        for ent, (element, script_comp, transform) in self.world.get_components(Element, ScriptComponent, Transform):
            element_size = Vector2(element.size.x, element.size.y)

            if event.type == pygame.MOUSEMOTION:
                to_remove = []
                for t_ent in self.hover_tracking:
                    t_element = self.world.component_for_entity(t_ent, Element)
                    t_script_comp = self.world.component_for_entity(t_ent, ScriptComponent)
                    t_transform = self.world.component_for_entity(t_ent, Transform)
                    t_element_size = Vector2(t_element.size.x, t_element.size.y)
                    if not is_inside(event.pos, t_transform.pos, t_element_size):
                        t_script_comp.script.on_ui_event(UiEvent(UiEventType.MOUSE_LEAVE))
                        to_remove.append(t_ent)
                for r_ent in to_remove:
                    self.hover_tracking.remove(r_ent)
                
                if is_inside(event.pos, transform.pos, element_size) and len(self.hold_tracking) == 0:
                    self.hover_tracking.add(ent)
                    script_comp.script.on_ui_event(
                        UiEvent(UiEventType.MOUSE_ENTER,
                                Vector2(event.pos[0] - transform.pos.x, event.pos[1] - transform.pos.y)))
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if is_inside(event.pos, transform.pos, element_size):
                    self.hold_tracking.add(ent)
                    script_comp.script.on_ui_event(
                        UiEvent(UiEventType.MOUSE_DOWN,
                                Vector2(event.pos[0] - transform.pos.x, event.pos[1] - transform.pos.y)))
            elif event.type == pygame.MOUSEBUTTONUP:
                ui_event = UiEvent(UiEventType.MOUSE_UP,
                    Vector2(event.pos[0] - transform.pos.x, event.pos[1] - transform.pos.y))

                if ent in self.hold_tracking:
                    script_comp.script.on_ui_event(ui_event)
                    self.hold_tracking.remove(ent)
    

def is_inside(mouse_pos, pos, size):
    return mouse_pos[0] > pos.x and mouse_pos[1] > pos.y and mouse_pos[0] < (pos.x + size.x) and mouse_pos[1] < (pos.y + size.y)

class UiEvent:
    def __init__(self, type, data=None):
        self.type = type
        self.data = data

class UiEventType(Enum):
    MOUSE_DOWN = 0
    MOUSE_UP = 1
    MOUSE_ENTER = 2
    MOUSE_LEAVE = 3