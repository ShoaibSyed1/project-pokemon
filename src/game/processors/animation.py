from esper import Processor
from pygame import Rect

from game.components import Animation, AnimationGroups, Sprite, Transform

class AnimationProcessor(Processor):
    def __init__(self):
        pass
    
    def process(self, delta):
        et = None
        for ent, (anim, anim_groups) in self.world.get_components(Animation, AnimationGroups):
            current = anim_groups.groups[anim_groups.current]
            if current != None:
                anim.loop_start = current.loop_start
                anim.loop_end = current.loop_end
                anim.delay = current.delay

        for ent, (anim, spr, transform) in self.world.get_components(Animation, Sprite, Transform):
            anim.counter += delta

            if anim.delay == -1:
                anim.counter = 0

            if anim.counter >= anim.delay:
                anim.counter = 0
                anim.loop_index += 1
                if anim.loop_index >= anim.loop_max or anim.loop_index >= anim.loop_end or anim.loop_index <= anim.loop_start:
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