from enum import Enum

import pygame
from pygame.math import Vector2

from game.components import Animation, AnimationGroup, AnimationGroups
from game.components.ui import Element
from game.scripts.script import Script
from game.scripts.ui import Textbox

class Npc(Script):
    def __init__(self, npc_type, npc_info):
        self.npc_type = npc_type
        self.npc_info = npc_info

    def interact(self, player):
        from game.components import EventListener, ScriptComponent, Sprite, Transform
        from game.loaders import EntityLoader

        on_interact = self.npc_info.get('on_interact', None)
        if on_interact != None:
            if on_interact['type'] == 'textbox':
                text = on_interact['text']
                merge = { 'script': { 'args': text } }

                EntityLoader.load("overworld/ui/textbox", self.world, merge)

class NpcType(Enum):
    STILL = 0