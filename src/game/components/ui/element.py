from pygame.math import Vector2

class Element:
    def __init__(self, name, size=Vector2(0, 0)):
        self.name = name
        self.size = size