from enum import Enum

from game.data import pokemon
from game.loaders import EntityLoader
from game.scripts.script import Script

class BattleController(Script):
    def __init__(self):
        self.battle_info = BattleInfo(pokemon.PokemonData('charmander', 'pepsi man', 20, [
            pokemon.MoveData('tackle', 20)
        ]), pokemon.PokemonData('charmander', 'mynamjeff', 20, [
            pokemon.MoveData('tackle', 20)
        ]))
        self.state = BattleState.WAITING

        self.attack_buttons = [None, None, None, None]
        self.item_button = None
        self.poke_button = None
        self.run_button = None

        self.info_label = None

        self.status_panel_front = None
        self.status_panel_back = None

        self.attack_button_scripts = [None, None, None, None]

    def start(self):
        from game import lang
        from game.components import AnimationGroups, ScriptComponent

        self.pokemon_front = EntityLoader.load("battle/front", self.world,
                              {'sprite': "pokemon/battle/" + self.battle_info.front_info.pokemon})
        self.pokemon_front_anim = self.world.component_for_entity(self.pokemon_front, AnimationGroups)
        self.pokemon_front_script = self.world.component_for_entity(self.pokemon_front, ScriptComponent).script

        self.pokemon_back = EntityLoader.load("battle/back", self.world,
                              {'sprite': "pokemon/battle/" + self.battle_info.back_info.pokemon})
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

            self.attack_button_scripts[i] = self.world.component_for_entity(self.attack_buttons[i], ScriptComponent).script
            self.attack_button_scripts[i].set_cb_enter(self.attack_hover, i)
            self.attack_button_scripts[i].set_cb_release(self.attack_use, i)

            try:
                move = self.battle_info.front_info.moves[i]
                self.attack_button_scripts[i].text = lang.get('move.' + move.name)
            except IndexError:
                self.attack_button_scripts[i].text = ""
                self.attack_button_scripts[i].disabled = True
        
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
        
        self.status_panel_front = EntityLoader.load("battle/ui/status_panel_front", self.world, {
            "script": {
                "args": {
                    "name": self.battle_info.front_info.name
                }
            }
        })
        self.status_panel_back = EntityLoader.load("battle/ui/status_panel_back", self.world, {
            "script": {
                "args": {
                    "name": self.battle_info.back_info.name
                }
            }
        })
        anim = self.world.component_for_entity(self.status_panel_back, AnimationGroups).current = 'back'
    
    def update(self, delta):
        pass
    
    def attack_hover(self, index):
        self.info_label_script.text = str(index)
    
    def attack_use(self, index):
        print("USED", index)

class BattleState(Enum):
    WAITING = 0

class BattleInfo:
    def __init__(self, front_info, back_info):
        self.front_info = front_info
        self.back_info = back_info