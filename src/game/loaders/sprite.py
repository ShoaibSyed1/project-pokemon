import json

import pygame

from game.components import Animation, AnimationGroup, AnimationGroups, Sprite

class SpriteLoader:
    def __init__(self, path):
        self.img_path = 'assets/sprites/' + path + ".png"
        self.json_path = 'assets/sprites/' + path + ".json"
    
    def load(self):
        sprite_info = None
        with open(self.json_path) as file:
            sprite_info = json.load(file)
        
        surface = pygame.image.load(self.img_path)
        x = sprite_info.get('x', 0)
        y = sprite_info.get('y', 0)
        width = sprite_info.get('width', surface.get_width())
        height = sprite_info.get('height', surface.get_height())
        sprite = Sprite(surface, pygame.Rect(x, y, width, height))

        animation = None
        animation_groups = None

        animation_info = sprite_info.get('animation', None)
        if animation_info == None:
            animation = Animation(width, height, width, height, -1, 0, 1)
        else:
            s_width = animation_info.get('width', width)
            s_height = animation_info.get('height', height)
            delay = animation_info.get('delay', -1)
            start = animation_info.get('start', 0)
            end = animation_info.get('end', int(width / s_width) * int(height / s_height))

            animation = Animation(width, height, s_width, s_height, delay, start, end)

            animation_groups_info = animation_info.get('groups', None)
            if animation_groups_info != None:
                groups = {}
                for key, value in animation_groups_info.items():
                    g_loop = value.get('loop', True)
                    g_start = value.get('start', 0)
                    g_end = value.get('end', end)
                    g_delay = value.get('delay', delay)

                    group = AnimationGroup(g_loop, g_start, g_end, g_delay)
                    groups[key] = group
                
                animation_groups = AnimationGroups(animation_info['default'], groups)

        return (sprite, animation, animation_groups)