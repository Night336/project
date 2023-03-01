import pygame.image

from enemy import Enemy
from base_views import BaseView
from menu import Button, Menu, Input

WIDTH, HEIGHT = 600, 400

class Interface:
    def __init__(self, player):
        self.button_list = []
        for i in range(5):
            button = Button('', lambda: print('Hello'))
            button.set_size(40, 40)
            button.set_pos(i * (button.rect.width + 10) + 150, HEIGHT - button.rect.height)
            self.button_list.append(button)
        self.button_list[0].obj = player.dmg_up
        button = Button('menu', lambda: print('Hello'))
        button.set_size(60, 30)
        button.set_pos(WIDTH - (button.rect.width + 2), 2)
        self.button_list.append(button)


    def draw(self, screen):
        for button in self.button_list:
            button.draw(screen)

    def mouse_motion_event(self, pos):
        for button in self.button_list:
            button.mouse_motion_event(pos)

    def mouse_button_down(self, pos):
        for button in self.button_list:
            button.mouse_button_down(pos)

    def mouse_button_up(self, pos):
        for button in self.button_list:
            button.mouse_button_up(pos)


class Game(BaseView):
    def __init__(self, stack, player, new=False):
        super().__init__(stack, player)
        self.new = new
        self.image = pygame.image.load('data/images/game_background.png')
        self.image = pygame.transform.scale(self.image, (WIDTH, HEIGHT))

    def start_game(self):
        self.interface = Interface(self.player)
        self.enemy = Enemy(1, self.player)

    def __call__(self):
        self.stack.append(self)
        if self.new:
            input_elem = Input('Введите имя персонажа')
            button = Button('создать', self.player.new_game(input_elem, self.stack, self.start_game))
            create_player_menu = Menu(self.stack, self.player, input_elem, button)
            self.stack.append(create_player_menu)
        else:
            self.start_game()

    def update(self):
        self.enemy.update()


    def draw(self, screen):
        screen.fill((0, 0, 200))
        screen.blit(self.image, (0, 0))
        self.enemy.draw(screen)
        self.interface.draw(screen)
        self.player.draw(screen)


    def mouse_motion_event(self, pos):
        self.interface.mouse_motion_event(pos)
        self.enemy.mouse_motion_event(pos)

    def mouse_button_down(self, pos):
        self.interface.mouse_button_down(pos)
        self.enemy.mouse_button_down(pos)

    def mouse_button_up(self, pos):
        self.interface.mouse_button_up(pos)