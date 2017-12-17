from enum import Enum

from game.loaders import EntityLoader
from game.scripts.script import Script

class BattleController(Script):
    def __init__(self, battle_info):
        self.battle_info = battle_info
        self.state = BattleState.WAITING

        self.attack_buttons = [None, None, None, None]

    def start(self):
        from game.components import ScriptComponent

        self.pokemon_front = EntityLoader.load("battle/front", self.world,
                              {'sprite': "pokemon/battle/" + self.battle_info['front_info']['pokemon']})
        self.pokemon_back = EntityLoader.load("battle/back", self.world,
                              {'sprite': "pokemon/battle/" + self.battle_info['front_info']['pokemon']})

        for i in range(0, 4):
            self.attack_buttons[i] = EntityLoader.load("battle/ui/button_attack", self.world, {
                "element": {
                    "pos": [0, i * 80]
                },
                "script": {
                    "args": "Attack"
                }
            })

            self.world.component_for_entity(self.attack_buttons[i], ScriptComponent).script.set_cb_enter(self.attack_hover, i)
    
    def update(self, delta):
        pass
    
    def attack_hover(self, index):
        print(index)

class BattleState(Enum):
    WAITING = 0