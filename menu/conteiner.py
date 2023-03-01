import pygame.image

from base_views import BaseView
from menu import Button


class Menu(BaseView):
    def __init__(self, stack, player, *args):
        super().__init__(stack, player)
        for ind, button in enumerate(args):
            if isinstance(button, Button):
                button.set_size(100, 50)
            else:
                button.set_size(200, 50)
            button.set_pos(600 / 2 - button.rect.width / 2, 60 * ind + 80)

        self.lst = args
        self.button_lst = args
        # self.exit()
        self.image = pygame.image.load('data/images/menu_background.png')
        self.image = pygame.transform.scale(self.image, (600, 400))

    def draw(self, screen=None):
        screen.blit(self.image, (0, 0))
        for button in self.lst:
            button.draw(screen)

    def mouse_motion_event(self, pos):
        for button in self.lst:
            button.mouse_motion_event(pos)

    def select(self, param):
        self.stack.append(self.lst[int(param)])

    def mouse_button_down(self, pos):
        for button in self.lst:
            button.mouse_button_down(pos)

    def key_down(self, key):
        for button in self.lst:
            button.key_down(key)

    def mouse_button_up(self, pos):
        for button in self.lst:
            button.mouse_button_up(pos)