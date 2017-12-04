import json

from esper import Processor

from game import paths
from game.components import Transform, WorldInfo

class WorldProcessor(Processor):
    def __init__(self, entity, player):
        self.world_info = entity
        self.player = player
    
    def process(self, delta):
        world_info = self.world.component_for_entity(self.world_info, WorldInfo)

        if world_info.info == None:
            world_path = paths.get_world(world_info.name) + "world.json"
            world_json = open(world_path)
            world_info.info = json.load(world_json)
        
        player_transform = self.world.component_for_entity(self.player, Transform)
        player_pos = player_transform.pos
        chunk_x = int(player_pos.x / 256) #TODO: Replace with constants
        chunk_y = int(player_pos.y / 256)

        if not [chunk_x, chunk_y] in world_info.loaded:
            chunk_path = None
            for chunk in world_info.info['chunks']:
                if chunk['pos'] == [chunk_x, chunk_y]:
                    chunk_path = chunk['path']

            chunk_path = paths.get_chunk(world_info.name, chunk_path)
            chunk_json = open(chunk_path)
            chunk = json.load(chunk_json)

            mapping_path = paths.get_mapping(world_info.name, chunk['mapping'])
            mapping_json = open(mapping_path)
            mapping = json.load(mapping_json)
            #TODO: Load chunk