import pygame

from game.components import AnimationGroups, Transform
from game.scripts.script import Script
from game.scripts.ui.controller import UiEventType

class Button(Script):
    def __init__(self):
        self.held = False
        self.inside = False
    
    def start(self):
        self.anim_groups = self.world.component_for_entity(self.entity, AnimationGroups)
    
    def on_ui_event(self, event):
        if event.type == UiEventType.MOUSE_ENTER and not self.held:
            self.anim_groups.current = 'hover'
            self.inside = True
        elif event.type == UiEventType.MOUSE_DOWN:
            self.held = True
            self.anim_groups.current = 'down'
            self.on_press()
        elif event.type == UiEventType.MOUSE_UP:
            self.held = False
            if self.inside:
                self.anim_groups.current = 'hover'
            else:
                self.anim_groups.current = 'up'
            self.on_release()
        elif event.type == UiEventType.MOUSE_LEAVE:
            self.inside = False
            if not self.held:
                self.anim_groups.current = 'up'
    
    def on_press(self): pass
    
    def on_release(self): pass