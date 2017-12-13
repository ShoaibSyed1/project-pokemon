from pygame.math import Vector2

class Transform:
    def __init__(self, arg):
        self.pos = Vector2(arg.get('pos', [0, 0])[0], arg.get('pos', [0, 0])[1])
        self.scale = Vector2(arg.get('scale', [1, 1])[0], arg.get('scale', [1, 1])[1])
        self.layer = arg.get('layer', 0)