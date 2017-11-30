from esper import Processor
from pygame import Rect

from game.components import Animation, Sprite, Transform

class AnimationProcessor(Processor):
    def __init__(self):
        pass
    
    def process(self, delta):
        for ent, (anim, spr, transform) in self.world.get_components(Animation, Sprite, Transform):
            anim.counter += delta

            if anim.counter >= anim.delay:
                anim.counter = 0
                anim.loop_index += 1
                if anim.loop_index >= anim.loop_max or anim.loop_index >= anim.loop_end:
                    anim.loop_index = anim.loop_start
                
                temp_x = anim.loop_index
                temp_y = 0
                while temp_x >= anim.xcount:
                    temp_x -= anim.ycount
                    temp_y += 1
                
                temp_width = int(anim.width * transform.scale.x)
                temp_height = int(anim.height * transform.scale.y)
                
                temp_x *= temp_width
                temp_y *= temp_height

                spr.bounds = Rect(temp_x, temp_y, temp_width, temp_height)