from enum import Enum

from game.loaders import EntityLoader
from game.scripts.script import Script

class BattleController(Script):
    def __init__(self, battle_info):
        self.battle_info = battle_info
        self.state = BattleState.WAITING

        self.attack_buttons = [None, None, None, None]
        self.item_button = None
        self.poke_button = None
        self.run_button = None

        self.info_label = None

    def start(self):
        from game.components import AnimationGroups, ScriptComponent

        self.pokemon_front = EntityLoader.load("battle/front", self.world,
                              {'sprite': "pokemon/battle/" + self.battle_info['front_info']['pokemon']})
        self.pokemon_front_anim = self.world.component_for_entity(self.pokemon_front, AnimationGroups)
        self.pokemon_front_script = self.world.component_for_entity(self.pokemon_front, ScriptComponent).script

        self.pokemon_back = EntityLoader.load("battle/back", self.world,
                              {'sprite': "pokemon/battle/" + self.battle_info['front_info']['pokemon']})
        self.pokemon_back_anim = self.world.component_for_entity(self.pokemon_back, AnimationGroups)
        self.pokemon_back_script = self.world.component_for_entity(self.pokemon_back, ScriptComponent).script

        self.pokemon_back_anim.current = "front"

        EntityLoader.load("battle/ui/panel", self.world)

        for i in range(0, 4):
            self.attack_buttons[i] = EntityLoader.load("battle/ui/button_left", self.world, {
                "element": {
                    "pos": [0, i * 80 + 8]
                },
                "script": {
                    "args": "Attack #" + str(i)
                }
            })

            self.world.component_for_entity(self.attack_buttons[i], ScriptComponent).script.set_cb_enter(self.attack_hover, i)
        
        self.item_button = EntityLoader.load("battle/ui/button_left", self.world, {
            "element": {
                "pos": [0, 332]
            },
            "script": {
                "args": "Item"
            }
        })

        self.poke_button = EntityLoader.load("battle/ui/button_left", self.world, {
            "element": {
                "pos": [0, 412]
            },
            "script": {
                "args": "Pokemon"
            }
        })

        self.run_button = EntityLoader.load("battle/ui/button_left", self.world, {
            "element": {
                "pos": [0, 492]
            },
            "script": {
                "args": "Run"
            }
        })

        self.info_label = EntityLoader.load("battle/ui/info_label", self.world)
        self.info_label_script = self.world.component_for_entity(self.info_label, ScriptComponent).script
    
    def update(self, delta):
        pass
    
    def attack_hover(self, index):
        self.info_label_script.text = str(index)

class BattleState(Enum):
    WAITING = 0