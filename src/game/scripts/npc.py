from enum import Enum

from game.scripts.script import Script

class Npc(Script):
    def __init__(self, npc_type, npc_info):
        self.npc_type = npc_type
        self.npc_info = npc_info

    def interact(self, player):
        print("TODO")

class NpcType(Enum):
    STILL = 0