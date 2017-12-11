import pygame

from game.components import AnimationGroups
from game.scripts.script import Script
from game.scripts.ui.controller import UiEventType

class Button(Script):
    def __init__(self):
        self.held = False
        self.inside = False

        self.cb_press = None
        self.cb_release = None
    
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
    
    def on_press(self):
        if self.cb_press != None:
            self.cb_press()
    
    def on_release(self):
        if self.cb_release != None:
            self.cb_release()
    
    def set_cb_press(self, cb_press):
        self.cb_press = cb_press
    
    def set_cb_release(self, cb_release):
        self.cb_release = cb_release