from pygame.math import Vector2

class Element:
    def __init__(self, arg):
        self.name = arg['name']
        self.size = Vector2(arg.get('size', [0, 0])[0], arg.get('size', [0, 0])[1])
        self.pos = Vector2(arg.get('pos', [0, 0])[0], arg.get('pos', [0, 0])[1])