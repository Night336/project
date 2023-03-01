import pygame

MOVE_TO_SPAUN = 0
STAND = 1
ATTACKED = 2

class Enemy:
    def __init__(self, hp, player):
        self.player = player
        self.rect = pygame.Rect(220 * 3, 160, 160, 160)
        self.animation_move_lst = []
        self.animation_hurt_lst = []
        self.animation_idle_lst = []
        self.current_animation_lst = []

        for i in range(4):
            image = pygame.image.load(f"data/images/slime-move-{i}.png")
            image = pygame.transform.scale(image, (self.rect.width, self.rect.height))
            self.animation_move_lst.append(image)

        for i in range(4):
            image = pygame.image.load(f"data/images/slime-hurt-{i}.png")
            image = pygame.transform.scale(image, (self.rect.width, self.rect.height))
            self.animation_hurt_lst.append(image)

        for i in range(4):
            image = pygame.image.load(f"data/images/slime-idle-{i}.png")
            image = pygame.transform.scale(image, (self.rect.width, self.rect.height))
            self.animation_idle_lst.append(image)
        self.snawn(player.hp)

    def snawn(self, hp):
        self.frame = 0
        self.hp = hp
        self.curr_hp = hp
        self.is_dead = False
        self.rect = pygame.Rect(220 * 3, 160, 160, 160)
        self.color = (0, 200, 0)
        self.clickable = False
        self.state = MOVE_TO_SPAUN
        self.current_animation_lst = self.animation_move_lst

    def update(self):
        self.frame += 0.1
        if self.state == ATTACKED and self.frame > len(self.animation_hurt_lst):
            self.state = STAND
            self.current_animation_lst = self.animation_idle_lst

        self.frame %= len(self.current_animation_lst)
        if self.rect.x > 220:
            self.rect.x -= 5
        elif self.state == MOVE_TO_SPAUN:
            self.state = STAND
            self.current_animation_lst = self.animation_idle_lst


    def foo(self):
        print('появляется')

    def foo2(self):
        print("Уходит с экрана")

    def attacked(self, damage):
        self.state = ATTACKED
        self.frame = 0
        self.current_animation_lst = self.animation_hurt_lst
        self.curr_hp -= damage
        if self.curr_hp <= 0:
            self.is_dead = True
            self.color = (100, 100, 100)
            self.snawn(self.hp * 1.3)

    def mouse_motion_event(self, pos):
        if self.rect.collidepoint(pos):
            self.clickable = True
        else:
            self.clickable = False

    def mouse_button_down(self, pos):
        self.mouse_motion_event(pos)
        if self.state != MOVE_TO_SPAUN and self.clickable:
            self.attacked(self.player.attack(pos))




    def draw(self, screen):
        if self.hp > 0:
            procent = self.curr_hp / self.hp
        else:
            procent = 0
        # pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.current_animation_lst[int(self.frame)], (self.rect.x, self.rect.y))

        height_hp = 0.08 * self.rect.height
        pygame.draw.rect(screen, (200, 20, 0), (self.rect.x, self.rect.y - height_hp - 5,
                                                procent * self.rect.width, height_hp))
