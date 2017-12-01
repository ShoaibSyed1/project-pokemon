from pymunk.vec2d import Vec2d

class Transform:
    def __init__(self, pos=Vec2d(), scale=Vec2d(1.0, 1.0)):
        self.pos = pos
        self.scale = scale