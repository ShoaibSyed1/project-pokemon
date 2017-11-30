class Animation:
    def __init__(self, sheet, width, height, delay=1000, loop_start=0, loop_end=0):
        self.sheet = sheet
        self.width = width
        self.height = height
        self.delay = delay

        if self.sheet.get_width() % self.width != 0:
            raise ImageSizeError()
        
        if self.sheet.get_height() % self.height != 0:
            raise ImageSizeError()
        
        self.counter = 0
        self.sprites_x = self.sheet.get_width() / self.width
        self.sprites_y = self.sheet.get_height() / self.height
        self.loop_index = 0
        self.loop_max = self.sprites_x * self.sprites_y
        self.loop_start = loop_start
        self.loop_end = loop_end

class ImageSizeError(Exception):
    pass
