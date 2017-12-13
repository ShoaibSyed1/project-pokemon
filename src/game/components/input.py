from enum import Enum

class InputComponent:
    def __init__(self, arg):
        self.keys = {}
        for id in arg['keys']:
            self.keys[id] = False