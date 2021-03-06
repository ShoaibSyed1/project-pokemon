class ComponentList:
    def __init__(self):
        self.comps = {}
    
    def register(self, comp, name):
        self.comps[name] = comp
    
    def get(self, name, arg):
        return self.comps[name](arg)

component_list = ComponentList()

get = component_list.get

from game.components.animation import Animation, AnimationGroup, AnimationGroups
from game.components.event import EventListener
from game.components.game_info import GameInfo
from game.components.input import InputComponent
from game.components.script import ScriptComponent
from game.components.sprite import Sprite
from game.components.tile import Direction, Tile
from game.components.tile_object import TileObject
from game.components.transform import Transform
from game.components.uuid import Uuid
from game.components.world import WorldInfo

from game.components.ui import Element

component_list.register(Animation, '_animation')
component_list.register(AnimationGroups, '_animation_groups')
component_list.register(EventListener, 'event_listener')
component_list.register(GameInfo, 'game_info')
component_list.register(InputComponent, 'input')
component_list.register(ScriptComponent, 'script')
component_list.register(Sprite, '_sprite')
component_list.register(Tile, 'tile')
component_list.register(TileObject, 'tile_object')
component_list.register(Transform, 'transform')
component_list.register(Uuid, 'uuid')
component_list.register(WorldInfo, 'world_info')

component_list.register(Element, 'element')