from enum import Enum

import pygame

from pygame.math import Vector2

from game import uuids
from game.components import AnimationGroups, InputComponent
from game.components.tile import Direction, Tile
from game.components.transform import Transform
from game.components.world import WorldInfo
from game.scripts.script import Script

class PlayerScript(Script):
    def __init__(self, data):
        self.data = data

        self.can_move = True

        self.move_tracker = MoveTracker()
    
    def start(self):
        self.anim_groups = self.world.component_for_entity(self.entity, AnimationGroups)
        self.tile = self.world.component_for_entity(self.entity, Tile)
        self.transform = self.world.component_for_entity(self.entity, Transform)

        self.camera_ent = self.get_entity(uuids.CAMERA)
        self.camera_transform = self.world.component_for_entity(self.camera_ent, Transform)

        self.world_ent = self.get_entity(uuids.WORLD)
        self.world_info = self.world.component_for_entity(self.world_ent, WorldInfo)
    
    def update(self, delta):
        if not self.tile.is_moving:
            self.anim_groups.current = 'still'
            direction = self.move_tracker.peek()
            if direction != None and self.can_move:
                self.tile.move_path.insert(0, direction)
        else:
            if self.tile.move_dir == Direction.DOWN:
                self.anim_groups.current = 'walk_down'
        
        self.camera_transform.pos = Vector2(self.transform.pos.x - 512, self.transform.pos.y - 288)
    
    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.move_tracker.hold(Direction.UP)
            elif event.key == pygame.K_a:
                self.move_tracker.hold(Direction.LEFT)
            elif event.key == pygame.K_s:
                self.move_tracker.hold(Direction.DOWN)
            elif event.key == pygame.K_d:
                self.move_tracker.hold(Direction.RIGHT)
            elif event.key == pygame.K_SPACE:
                self.interact()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.move_tracker.release(Direction.UP)
            elif event.key == pygame.K_a:
                self.move_tracker.release(Direction.LEFT)
            elif event.key == pygame.K_s:
                self.move_tracker.release(Direction.DOWN)
            elif event.key == pygame.K_d:
                self.move_tracker.release(Direction.RIGHT)
    
    def interact(self):
        if self.can_move and not self.tile.is_moving:
            ix = self.tile.pos.x
            iy = self.tile.pos.y

            if self.tile.move_dir == Direction.UP:
                iy -= 1
            elif self.tile.move_dir == Direction.DOWN:
                iy += 1
            elif self.tile.move_dir == Direction.LEFT:
                ix -= 1
            elif self.tile.move_dir == Direction.RIGHT:
                ix += 1
            
            self.world_info.interact = (int(ix), int(iy), self)

class MoveTracker:
    def __init__(self):
        self.inner = []
    
    def hold(self, direction):
        if direction in self.inner:
            for num in range(0, self.inner.count(direction)):
                self.inner.remove(direction)
        
        self.inner.append(direction)
    
    def release(self, direction):
        for num in range(0, self.inner.count(direction)):
            self.inner.remove(direction)
    
    def peek(self):
        if len(self.inner) > 0:
            return self.inner[len(self.inner)-1]
        else:
            return None
