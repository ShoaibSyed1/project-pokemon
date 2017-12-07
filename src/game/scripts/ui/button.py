import pygame

from game.components import AnimationGroups, Transform
from game.scripts.script import Script
from game.scripts.ui.controller import UiEventType

class Button(Script):
    def start(self):
        self.anim_groups = self.world.component_for_entity(self.entity, AnimationGroups)
    
    def on_ui_event(self, event):
        if event.type == UiEventType.MOUSE_HOVER:
            pass
        elif event.type == UiEventType.MOUSE_DOWN:
            self.anim_groups.current = 'down'
        elif event.type == UiEventType.MOUSE_UP:
            self.anim_groups.current = 'up'