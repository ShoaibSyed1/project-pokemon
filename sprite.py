""" Contains the Sprite class """

import pygame


class SpriteSizeError(Exception):
    pass


class Sprite:
    """
    Sprite class to render images and animations from spritesheets.
    """

    def __init__(self, swidth, sheight, image_path, delay=0):
        self._path = image_path

        #Sprite width and height
        self._swidth = swidth
        self._sheight = sheight

        self.x = 0
        self.y = 0

        self._image = pygame.image.load(image_path)

        #Verify that the image dimensions are multiples of sprite dimensions
        if self._image.get_width(
        ) % self._swidth != 0 or self._image.get_height() % self._sheight != 0:
            raise SpriteSizeError

        #Number of sprites in image vertically and horizontally
        self._hcount = int(self._image.get_width() / self._swidth)
        self._vcount = int(self._image.get_height() / self._sheight)

        #Animation looping variables
        self._loop_start = 0
        self._loop_end = self._hcount * self._vcount
        self._loop_index = 0

        self._delay = delay
        self._delay_counter = 0

    def scale(self, swidth, sheight):
        """
        Scale internal image and sprite width and height
        """
        self._swidth = swidth
        self._sheight = sheight

        self._image = pygame.transform.scale(self._image,
                                             (self._swidth * self._hcount,
                                              self._sheight * self._vcount))

    def loop(self, start, end):
        """
        Set frames to loop inside image
        """
        if self._loop_start != start or self._loop_index > self._loop_end:
            self._loop_index = start
        self._loop_start = start
        self._loop_end = end

    def set_delay(self, delay):
        """
        Delay between switching sprite image
        """
        self._delay = delay

    def update(self, dt):
        #Update animation loop index
        if self._delay_counter >= self._delay:
            self._loop_index += 1
            if self._loop_index >= self._loop_end:
                self._loop_index = self._loop_start

            self._delay_counter = 0

        self._delay_counter += dt

    def render(self, screen):
        #Set X and Y variables based on current animation loop index
        temp_x = self._loop_index
        temp_y = 0
        while temp_x >= self._hcount:
            temp_x -= self._hcount
            temp_y += 1

        temp_x *= self._swidth
        temp_y *= self._sheight

        #Draw subsection of internal image as sprite
        screen.blit(
            self._image, (self.x, self.y),
            area=(temp_x, temp_y, self._swidth, self._sheight))
