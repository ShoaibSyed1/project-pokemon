class Sprite:
    def __init__(self, surface, bounds=None):
        self.surface = surface
        if bounds == None:
            bounds = surface.get_rect()
        self.bounds = bounds