from enum import Enum

import pygame
from pygame.font import Font
from pygame.math import Vector2

from game import uuids
from game.components import AnimationGroups, ScriptComponent, Sprite, Transform
from game.components.ui import Element
from game.scripts.script import Script

TEXT_SIZE = 48

class Textbox(Script):
    def __init__(self, text=None, owner=None):
        self.font = Font("assets/fonts/normal.ttf", TEXT_SIZE)
        self.owner_entity = None
        self.text_entity = [None, None, None]
        self.state = TextboxState.OPENING
        self.text_index = 0
        self.text_max = 0
        if text != None:
            self.text_max = len(text)

        self.scaler = 0.001

        self.text = text
        self.owner = owner
    
    def start(self):
        self.anim = self.world.component_for_entity(self.entity, AnimationGroups)
        self.element = self.world.component_for_entity(self.entity, Element)
        self.transform = self.world.component_for_entity(self.entity, Transform)
        
        self.player_ent = self.get_entity(uuids.get('player'))
        self.player_script_comp = self.world.component_for_entity(self.player_ent, ScriptComponent)
        self.player_script_comp.script.can_move = False

        self.transform.scale = Vector2(0.01, 0.01)

        if self.owner != None:
            self.anim.current = 'named'
    
    def update(self, delta):
        if self.state == TextboxState.OPENING:
            if self.transform.scale.x < 1:
                self.transform.scale.x += self.scaler
                self.scaler += 0.005
                self.transform.scale.y = self.transform.scale.x

            if self.transform.scale.x > 1:
                self.set_reading()
        elif self.state == TextboxState.CLOSING:
            for i in range(0, 3):
                if self.text_entity[i] != None:
                    self.world.delete_entity(self.text_entity[i])
                    self.text_entity[i] = None
                if self.owner_entity != None:
                    self.world.delete_entity(self.owner_entity)
                    self.owner_entity = None
            if self.transform.scale.x <= 0.1:
                self.world.delete_entity(self.entity)
                self.player_script_comp.script.can_move = True
            else:
                self.transform.scale.x -= self.scaler
                self.scaler += 0.005
                self.transform.scale.y = self.transform.scale.x
                if self.transform.scale.x < 0:
                    self.transform.scale.x = 0
                    self.transform.scale.y = 0
    
    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if self.state == TextboxState.OPENING:
                    self.set_reading()
                elif self.state == TextboxState.READING:
                    self.text_index += 1
                    if self.text_index < self.text_max:
                        self.set_text(self.text[self.text_index])
                    else:
                        self.set_closing()
    
    def set_reading(self):
        self.transform.scale.x = 1.0
        self.transform.scale.y = 1.0
        self.state = TextboxState.READING

        if self.owner != None:
            self.owner_entity = self.world.create_entity(
                Element(self.element.name + "_owner", pos=Vector2(self.element.pos.x + 8, self.element.pos.y)),
                Sprite(self.font.render(self.owner, False, (0, 0, 0))),
                Transform({'layer': 25})
            )

        if self.text != None:
            self.set_text(self.text[self.text_index])
    
    def set_closing(self):
        self.state = TextboxState.CLOSING
        self.scaler = 0.001
    
    def set_text(self, lines):
        for i in range(0, 3):
            if self.text_entity[i] != None:
                self.world.delete_entity(self.text_entity[i])
            self.text_entity[i] = self.world.create_entity(
                Element(self.element.name + "_text" + str(i), pos=Vector2(self.element.pos.x + 8, self.element.pos.y + TEXT_SIZE * i + 48)),
                Sprite(self.font.render(lines[i], False, (0, 0, 0))),
                Transform({'layer': 25})
            )

class TextboxState(Enum):
    OPENING = 0
    READING = 1
    CLOSING = 2