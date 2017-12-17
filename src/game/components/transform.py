from pygame.math import Vector2

class Transform:
    def __init__(self, arg):
        self.pos = Vector2(arg.get('pos', [-1000, -1000])[0], arg.get('pos', [-1000, -1000])[1])
        self.scale = Vector2(arg.get('scale', [1, 1])[0], arg.get('scale', [1, 1])[1])
        self.layer = arg.get('layer', 0)