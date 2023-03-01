from database import Database
from player import Player
from menu import Menu, Button, Exit
from game import Game
from setting import Setting
from score import Score
import pygame

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    player = Player('Петя')

    game_stack = []
    menu_lst = []
    if player.player_is_exist(player.name):
        menu_lst.append(Button("Продолжить", Game(game_stack, player)))
    else:
        pass

    menu_lst.extend([
        Button("Старт", Game(game_stack, player, new=True)),
        Button("Настройки", Setting(game_stack, player)),
        Button("Рекорды", Score(game_stack, player)),
        Button("Выход", lambda: Exit(game_stack, player))
    ])
    main_dialog = Menu(
        game_stack,
        player,
        *menu_lst
    )


    game_stack.append(main_dialog)
    clock = pygame.time.Clock()
    while game_stack:
        game_stack[-1].update()
        game_stack[-1].draw(screen)
        game_stack[-1].event_handler(pygame.event.get())
        
        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)
    pygame.quit()