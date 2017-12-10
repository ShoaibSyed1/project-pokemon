from enum import Enum

import pygame
from pygame.font import Font
from pygame.math import Vector2

from game.components import ScriptComponent, Sprite, Transform
from game.components.ui import Element
from game.scripts.script import Script

TEXT_SIZE = 48

class Textbox(Script):
    def __init__(self, player):
        self.font = Font("assets/fonts/normal.ttf", TEXT_SIZE)
        self.text_entity = [None, None, None]
        self.state = TextboxState.OPENING

        self.player_ent = player
    
    def start(self):
        self.element = self.world.component_for_entity(self.entity, Element)
        self.transform = self.world.component_for_entity(self.entity, Transform)

        self.player_script_comp = self.world.component_for_entity(self.player_ent, ScriptComponent)
        self.player_script_comp.script.can_move = False

        self.transform.scale = Vector2(0.1, 0.1)
    
    def update(self, delta):
        if self.state == TextboxState.OPENING:
            if self.transform.scale.x < 1:
                self.transform.scale.x += 0.05
                self.transform.scale.y = self.transform.scale.x

            if self.transform.scale.x > 1:
                self.transform.scale.x = 1.0
                self.transform.scale.y = 1.0
                self.state = TextboxState.READING
        elif self.state == TextboxState.CLOSING:
            if self.transform.scale.x <= 0.1:
                self.world.delete_entity(self.entity)
                self.player_script_comp.script.can_move = True
            else:
                self.transform.scale.x -= 0.05
                self.transform.scale.y = self.transform.scale.x
    
    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if self.state == TextboxState.OPENING:
                    self.set_reading()
                elif self.state == TextboxState.READING:
                    self.set_closing()
    
    def set_reading(self):
        self.transform.scale.x = 1.0
        self.transform.scale.y = 1.0
        self.state = TextboxState.READING
    
    def set_closing(self):
        self.state = TextboxState.CLOSING
    
    def set_text(self, lines):
        for i in range(0, 3):
            if self.text_entity[i] != None:
                self.world.delete_entity(self.text_entity[i])
            self.text_entity[i] = self.world.create_entity(
                Element(self.element.name + "_text" + str(i), pos=Vector2(self.element.pos.x + 8, self.element.pos.y + TEXT_SIZE * i)),
                Sprite(self.font.render(lines[i], False, (0, 0, 0))),
                Transform(Vector2(10, 10), layer=20)
            )

class TextboxState(Enum):
    OPENING = 0
    READING = 1
    CLOSING = 2