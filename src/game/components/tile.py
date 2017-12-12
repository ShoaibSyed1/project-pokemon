from enum import Enum

from pygame.math import Vector2

class Tile:
    def __init__(self, arg):
        self.pos = Vector2(arg['pos'][0], arg['pos'][1])
        self.w = arg.get('size', [1, 1])[0]
        self.h = arg.get('size', [1, 1])[1]
        
        self.is_moving = False
        self.move_dir = Direction.UP
        self.move_path = []
        self.move_speed = arg.get('speed', 1)

class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3