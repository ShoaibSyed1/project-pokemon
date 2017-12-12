import pygame

EVENT_MAP = {
    "KEYDOWN": pygame.KEYDOWN,
    "KEYUP": pygame.KEYUP,
    'MOUSEBUTTONDOWN': pygame.MOUSEBUTTONDOWN,
    'MOUSEBUTTONUP': pygame.MOUSEBUTTONUP,
    'MOUSEMOTION': pygame.MOUSEMOTION
}

class EventListener:
    def __init__(self, arg):
        self.listen = list(map(lambda x: EVENT_MAP[x], arg['events']))