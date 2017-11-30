class Animation:
    def __init__(self, sheet_width, sheet_height, width, height, delay=1000, loop_start=0, loop_end=0):
        self.sheet_width = sheet_width
        self.sheet_height = sheet_height
        self.width = width
        self.height = height
        self.delay = delay

        if int(sheet_width % width) != 0:
            raise ImageSizeError()
        
        if int(sheet_height % height) != 0:
            raise ImageSizeError()
        
        self.counter = 0

        self.xcount = int(self.sheet_width / self.width)
        self.ycount = int(self.sheet_height / self.height)

        self.loop_index = 0
        self.loop_max = self.xcount * self.ycount
        self.loop_start = loop_start
        self.loop_end = loop_end

class ImageSizeError(Exception):
    pass
