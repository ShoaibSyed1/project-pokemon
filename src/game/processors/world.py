import json

from esper import Processor

import pygame

from pygame.math import Vector2

from game import paths
from game.components import Sprite, Transform, WorldInfo

class WorldProcessor(Processor):
    def __init__(self, entity, player):
        self.world_info_entity = entity
        self.player = player
        self.tilesets = {}
    
    def process(self, delta):
        world_info = self.world.component_for_entity(self.world_info_entity, WorldInfo)

        if world_info.info == None:
            info_path = paths.get_world(world_info.name)
            info_json = open(info_path)
            world_info.info = json.load(info_json)
            info_json.close()

            mappings_path = paths.get_mappings(world_info.name)
            mappings_json = open(mappings_path)
            world_info.mappings = json.load(mappings_json)
            mappings_json.close()

            for tileset_name in world_info.mappings['tilesets']:
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
            
            chunk_name = next(filter(lambda ch: ch['pos']==[0, 0], world_info.info['chunks']))['name']

            chunk_path = paths.get_chunk(world_info.name, chunk_name)
            chunk_json = open(chunk_path)
            chunk = json.load(chunk_json)
            chunk_json.close()

            for y in range(0, 16):
                for x in range(0, 16):
                    tile_id = chunk['layout'][y][x]
                    tile_info = world_info.mappings[str(tile_id)]
                    tileset_name = tile_info[0]
                    tile_name = tile_info[1]

                    tileset = self.tilesets[tileset_name]
                    tile_img_pos = tileset['info'][tile_name]

                    spr = Sprite(tileset['img'], pygame.Rect(tile_img_pos[0], tile_img_pos[1], 32, 32))
                    transform = Transform(Vector2(x * 32, y * 32), Vector2(2, 2))

                    self.world.create_entity(spr, transform)