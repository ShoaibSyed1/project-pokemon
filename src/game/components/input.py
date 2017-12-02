from enum import Enum

class InputComponent:
    def __init__(self, listen=[]):
        self.keys = {}
        for id in listen:
            self.keys[id] = False