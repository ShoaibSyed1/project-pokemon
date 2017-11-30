from esper import Processor
from pygame import Rect

from game.components.animation import Animation
from game.components.sprite import Sprite

class AnimationProcessor(Processor):
    def __init__(self):
        pass
    
    def process(self, delta):
        for ent, (anim, spr) in self.world.get_components(Animation, Sprite):
            anim.counter += delta

            if anim.counter > anim.delay:
                anim.counter = 0
                anim.loop_index += 1
                if anim.loop_index >= anim.loop_max or anim.loop_index >= anim.loop_end:
                    anim.loop_index = anim.loop_start
                
                y_index = int(anim.loop_index / anim.sprites_x)
                x_index = int(anim.loop_index % y_index)

                x = x_index * anim.width
                y = y_index * anim.height

                spr.surface = anim.sheet.subsurface(Rect(x, y, anim.width, anim.height))