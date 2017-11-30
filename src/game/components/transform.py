from game.math import Vector2

class Transform:
    def __init__(self, pos=Vector2(), scale=Vector2(1.0, 1.0)):
        self.pos = pos
        self.scale = scale