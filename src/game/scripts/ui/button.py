import pygame
from pygame.font import Font
from pygame.math import Vector2

from game.components import AnimationGroups
from game.components.ui import Element
from game.scripts.script import Script
from game.scripts.ui.controller import UiEventType

TEXT_SIZE = 48

class Button(Script):
    def __init__(self, text):
        self.font = Font("assets/fonts/normal.ttf", TEXT_SIZE)
        self.text = text
        self.text_entity = None

        self.held = False
        self.inside = False

        self.cb_press = None
        self.cb_release = None
    
    def start(self):
        self.anim_groups = self.world.component_for_entity(self.entity, AnimationGroups)
        self.element = self.world.component_for_entity(self.entity, Element)

        if self.text != None:
            self.set_text(self.text)
    
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
    
    def set_text(self, text):
        from game.components import Sprite, Transform

        if self.text_entity != None:
            self.world.delete_entity(self.text_entity)
            self.text_entity = None
        
        spr = self.font.render(text, False, (0, 0, 0))
        self.text_entity = self.world.create_entity(
            Element({
                'name': self.element.name + '_text',
                'pos': Vector2(self.element.pos.x + (self.element.size.x / 2) - (spr.get_width() / 2),
                               self.element.pos.y + (self.element.size.y / 2) - (spr.get_height() / 2))
            }),
            Sprite(spr),
            Transform({'layer': 25})
        )