from time import sleep

import pygame

from database import Database


class Attack:
    def __init__(self, damage, pos):
        self.time_line = 15
        self.size = 24
        self.font = pygame.font.Font(None, self.size)
        self.text = self.font.render(str(round(damage, 2)), True, (255, 255, 255))
        self.x, self.y = pos
        self.y -= 10

    def update(self):
        self.y -= 1
        self.time_line -= 0.3
        if self.time_line < 0:
            return False
        return True

    def draw(self, surface):
        surface.blit(self.text, (self.x, self.y))
        return self



class Player():
    def __init__(self, name):
        self.name = name
        self.dmg = 1
        self.attack_lst = []
        self.db = Database('data/database/db.db')
        self.lvl = 0
        self.dmg = 0
        self.hp = 1
        if self.db.player_is_exist(name):
            self.lvl, self.hp, self.dmg = self.db.save_from_player(self.name)

    def save(self):
        id = self.db.get_player_id(self.name)
        self.db.delete_saves(id)
        self.db.add_saving(self.lvl, self.hp, id, self.dmg)

    def create(self):
        self.db.add_player(self.name)
        id = self.db.get_player_id(self.name)
        self.db.add_saving(1, 1, id, 1)
        self.lvl = 1
        self.hp = 1
        self.dmg = 1


    def new_game(self, inp, stack, *args):
        def set_name():
            if inp.get_text() and not self.player_is_exist(inp.get_text()):
                self.name = inp.get_text()
                self.create()
                stack.pop()
                for fnc in args:
                    fnc()
            else:
                print('персонаж не создан')
        return set_name

    def player_is_exist(self, name):
        if name:
            return self.db.player_is_exist(name)
        return False

    def attack(self, pos):
        self.attack_lst.append(Attack(self.dmg, pos))
        return self.dmg

    def dmg_up(self):
        self.dmg += 1

    def draw(self, surface):
        self.attack_lst = [attack.draw(surface) for attack in self.attack_lst if attack.update()]