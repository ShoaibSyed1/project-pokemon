from enum import Enum

from pygame.math import Vector2

class Tile:
    def __init__(self, pos, solid=True, w=1, h=1, move_speed=0):
        self.pos = pos
        self.w = w
        self.h = h
        self.solid = solid
        
        self.is_moving = False
        self.move_dir = Direction.UP
        self.move_path = []
        self.move_speed = move_speed

class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3