import json

from esper import Processor

import pygame

from pygame.math import Vector2

from game import constants, paths
from game.components import Animation, Sprite, Transform, WorldInfo

class WorldProcessor(Processor):
    def __init__(self, entity, player, scale):
        self.world_info_entity = entity
        self.player = player
        self.tilesets = {}
        self.scale = scale
        self.loaded_chunks = []
        self.loaded_entities = {}
        self.loaded_objects = {}
    
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
                tileset_json_path = paths.get_tileset_json(tileset_name)
                tileset_img_path = paths.get_tileset_img(tileset_name)

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
        
        new_chunks_pos = []

        for y_offset in range(-1, 2):
            for x_offset in range(-1, 2):
                act_x = max(0, chunk_x + x_offset)
                act_y = max(0, chunk_y + y_offset)

                new_chunks_pos.append((act_x, act_y))
        
        new_chunks_pos = list(set(new_chunks_pos))
        
        for old_chunk_pos in self.loaded_chunks:
            if not old_chunk_pos in new_chunks_pos:
                for entity in self.loaded_entities[old_chunk_pos]:
                    self.world.delete_entity(entity)
                for obj in self.loaded_objects[old_chunk_pos]:
                    if obj != None:
                        self.world.delete_entity(obj)
                self.loaded_entities[old_chunk_pos] = None
                self.loaded_chunks.remove(old_chunk_pos)
        
        for new_chunk_pos in new_chunks_pos:
            if not new_chunk_pos in self.loaded_chunks:
                self.load_chunk(new_chunk_pos[0], new_chunk_pos[1])
    
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

        chunk_surface = pygame.Surface((int(constants.CHUNK_SIZE_PIXELS),
                                       int(constants.CHUNK_SIZE_PIXELS)))
        for layout in chunk['layouts']:
            for y in range(0, constants.CHUNK_SIZE):
                for x in range(0, constants.CHUNK_SIZE):
                    tile_id = layout[y][x]
                    tile_info = self.world_info.mappings[str(tile_id)]
                    tileset_name = tile_info[0]
                    tile_name = tile_info[1]

                    tileset = self.tilesets[tileset_name]
                    tile_img_pos = tileset['info'][tile_name]
                    tile_size = tileset['info']['tile_size']

                    chunk_surface.blit(tileset['img'],
                                    (x * tile_size, y * tile_size),
                                    pygame.Rect(tile_img_pos[0],
                                                tile_img_pos[1],
                                                tile_size,
                                                tile_size))
        
        spr = Sprite(chunk_surface, pygame.Rect(0, 0, constants.CHUNK_SIZE_PIXELS * self.scale, constants.CHUNK_SIZE_PIXELS * self.scale))
        transform = Transform(Vector2(chunk_x * constants.CHUNK_SIZE_PIXELS * self.scale, chunk_y * constants.CHUNK_SIZE_PIXELS * self.scale),
                              Vector2(self.scale, self.scale))
        self.loaded_entities[(chunk_x, chunk_y)].append(self.world.create_entity(spr, transform))

        objects = chunk['objects']
        object_mappings = chunk['object_mappings']
        for y in range(0, constants.CHUNK_SIZE):
            for x in range(0, constants.CHUNK_SIZE):
                obj_id = objects[y][x]
                obj_info = object_mappings[str(obj_id)]

                obj_x = int(chunk_x * constants.CHUNK_SIZE + x)
                obj_y = int(chunk_y * constants.CHUNK_SIZE + y)

                self.loaded_objects[(obj_x, obj_y)] = self.create_object(obj_info, obj_x, obj_y)

    def create_object(self, obj_info, x, y):
        obj_type = obj_info['type']
        if obj_type == 'none':
            return None