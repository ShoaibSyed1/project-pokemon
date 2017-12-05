import json

from esper import Processor

import pygame

from pygame.math import Vector2

from game import constants, paths
from game.components import Sprite, Transform, WorldInfo

class WorldProcessor(Processor):
    def __init__(self, entity, player, scale):
        self.world_info_entity = entity
        self.player = player
        self.tilesets = {}
        self.scale = scale
        self.loaded_chunks = []
        self.loaded_entities = {}
    
    def process(self, delta):
        self.world_info = self.world.component_for_entity(self.world_info_entity, WorldInfo)

        if self.world_info.info == None:
            info_path = paths.get_world(self.world_info.name)
            info_json = open(info_path)
            self.world_info.info = json.load(info_json)
            info_json.close()

            mappings_path = paths.get_mappings(self.world_info.name)
            mappings_json = open(mappings_path)
            self.world_info.mappings = json.load(mappings_json)
            mappings_json.close()

            for tileset_name in self.world_info.mappings['tilesets']:
                tileset_json_path = "assets/tilesets/" + tileset_name + ".json"
                tileset_img_path = "assets/tilesets/" + tileset_name + ".png"

                tileset_json = open(tileset_json_path)
                tileset = json.load(tileset_json)
                tileset_json.close()

                tileset_img = pygame.image.load(tileset_img_path)

                self.tilesets[tileset_name] = {
                    'info': tileset,
                    'img': tileset_img
                }
            
        player_pos = self.world.component_for_entity(self.player, Transform).pos

        chunk_x = int(player_pos.x / (constants.CHUNK_SIZE_PIXELS * self.scale))
        chunk_y = int(player_pos.y / (constants.CHUNK_SIZE_PIXELS * self.scale))

        if not (chunk_x, chunk_y) in self.loaded_chunks:
            for chunk_pos in self.loaded_chunks:
                for entity in self.loaded_entities[chunk_pos]:
                    self.world.delete_entity(entity)
                    self.loaded_entities[chunk_pos] = None
            self.loaded_chunks.clear()
            self.load_chunk(chunk_x, chunk_y)
    
    def load_chunk(self, chunk_x, chunk_y):
        self.loaded_chunks.append((chunk_x, chunk_y))
        try:
            chunk_name = next(filter(lambda ch: ch['pos']==[chunk_x, chunk_y], self.world_info.info['chunks']))['name']
        except StopIteration:
            print("No chunk defined for chunk position ({}, {})".format(chunk_x, chunk_y))
            raise

        chunk_path = paths.get_chunk(self.world_info.name, chunk_name)
        chunk_json = open(chunk_path)
        chunk = json.load(chunk_json)
        chunk_json.close()

        self.loaded_entities[(chunk_x, chunk_y)] = []

        for y in range(0, constants.CHUNK_SIZE):
            for x in range(0, constants.CHUNK_SIZE):
                tile_id = chunk['layout'][y][x]
                tile_info = self.world_info.mappings[str(tile_id)]
                tileset_name = tile_info[0]
                tile_name = tile_info[1]

                tileset = self.tilesets[tileset_name]
                tile_img_pos = tileset['info'][tile_name]
                tile_size = tileset['info']['tile_size']

                spr = Sprite(tileset['img'], pygame.Rect(tile_img_pos[0], tile_img_pos[1], tile_size, tile_size), self.scale)
                transform = Transform(Vector2(x * tile_size * self.scale, y * tile_size * self.scale), Vector2(self.scale, self.scale))
                
                self.loaded_entities[(chunk_x, chunk_y)].append(self.world.create_entity(spr, transform))