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

        on_interact = self.npc_info.get('on_interact', None)
        if on_interact != None:
            if on_interact['type'] == 'textbox':
                text = on_interact['text']
                owner = on_interact.get('owner', None)
                textbox = Textbox(text, owner)
                self.world.create_entity(
                    Animation(1536, 192, 768, 192, -1),
                    AnimationGroups('noname', {
                        'noname': AnimationGroup(False, 0, 1, -1),
                        'named': AnimationGroup(False, 1, 2, -1)
                    }),
                    Element("textbox", Vector2(768, 192), Vector2(128, 352)),
                    EventListener([pygame.KEYDOWN, pygame.KEYUP]),
                    ScriptComponent(textbox),
                    Sprite(pygame.image.load("assets/sprites/ui/textbox/textbox.png")),
                    Transform(layer=20)
                )

class NpcType(Enum):
    STILL = 0