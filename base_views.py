import pygame


class BaseView:
    def __init__(self, stack, player):
        self.stack = stack
        self.player = player
    
    def close(self):
        self.stack.pop()

    def exit(self):
        self.stack.clear()

    def mouse_motion_event(self, pos):
        pass

    def mouse_button_click_event(self, pos):
        pass

    def mouse_button_down(self, pos):
        pass
    
    def mouse_button_up(self, pos):
        pass

    def key_down(self, key):
        pass

    def event_handler(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.player.save()
                self.exit()
            elif event.type == pygame.MOUSEMOTION:
                self.mouse_motion_event(event.pos)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_button_down(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                self.mouse_button_up(event.pos)
            elif event.type == pygame.KEYDOWN:
                self.key_down(event)


    def update(self):
        pass

    def draw(self, screen):
        pass
