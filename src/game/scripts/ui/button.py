import pygame

from game.components import Animation, Transform
from game.scripts.script import Script
from game.scripts.ui.controller import UiEventType

class Button(Script):
    def start(self):
        self.animation = self.world.component_for_entity(self.entity, Animation)
    
    def on_ui_event(self, event):
        if event.type == UiEventType.MOUSE_HOVER:
            pass
        elif event.type == UiEventType.MOUSE_DOWN:
            self.animation.loop_start = 1
            self.animation.loop_end = 2
        elif event.type == UiEventType.MOUSE_UP:
            self.animation.loop_start = 0
            self.animation.loop_end = 1