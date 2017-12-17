from pygame.font import Font
from pygame.math import Vector2

from game.components import Element
from game.scripts.script import Script

DEFAULT_SIZE = 48

class Label(Script):
    def __init__(self, arg):
        self.last_text = None
        self.text = arg.get('text', "")
        self.font = Font("assets/fonts/normal.ttf", arg.get('size', DEFAULT_SIZE))
        
        self.text_entity = None
    
    def start(self):
        self.element = self.world.component_for_entity(self.entity, Element)
    
    def update(self, delta):
        if self.text != self.last_text:
            self.update_text()
    
    def update_text(self):
        from game.components import Sprite, Transform

        if self.text_entity != None:
            self.world.delete_entity(self.text_entity)
            self.text_entity = None
        
        self.last_text = self.text

        spr = self.font.render(self.text, False, (0, 0, 0))
        self.text_entity = self.world.create_entity(
            Element({
                'name': self.element.name + "_text",
                'pos': Vector2(self.element.pos.x, self.element.pos.y)
            }),
            Sprite(spr),
            Transform({'layer': 25})
        )