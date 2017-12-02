from enum import Enum

import pygame

from game.components import InputComponent
from game.components.transform import Transform
from game.scripts.script import Script

class PlayerScript(Script):    
    def start(self):
        self.input = self.world.component_for_entity(self.entity, InputComponent)
        self.transform = self.world.component_for_entity(self.entity, Transform)
    
    def update(self, delta):
        if self.input.keys[pygame.K_w]:
            self.transform.pos.y -= 2.5
        if self.input.keys[pygame.K_s]:
            self.transform.pos.y += 2.5
        if self.input.keys[pygame.K_a]:
            self.transform.pos.x -= 2.5
        if self.input.keys[pygame.K_d]:
            self.transform.pos.x += 2.5