from pygame import Rect

class Sprite:
    def __init__(self, surface, bounds=Rect(0, 0, 0, 0)):
        self.surface = surface
        self.bounds = bounds