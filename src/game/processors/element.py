from esper import Processor

from game.components import Animation, Element, Transform

class ElementProcessor(Processor):
    def process(self, delta):
        for ent, (animation, element, transform) in self.world.get_components(Animation, Element, Transform):
            if element.autoscale and animation.width != 0 and animation.height != 0:
                transform.scale.x = element.size.x / animation.width
                transform.scale.y = element.size.y / animation.height