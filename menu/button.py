import pygame

class Button:
    def __init__(self, text, obj):
        size = 24
        font = pygame.font.Font(None, size)
        self.text = font.render(text, True, (255, 255, 255))

        self.obj = obj 
        self.rect = pygame.Rect(0, 0, 10, 10)
        self.image = pygame.Surface((self.rect.width, self.rect.height))
        self.is_hover = False
        self.mouse_button_is_down = False

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y
    
    def set_size(self, width, heigh):
        self.rect.width = width
        self.rect.height = heigh

    def draw(self, screen):
        if self.is_hover:
            if self.mouse_button_is_down:
                color = (250, 100, 100)
            else:
                color = (255, 0, 0)
        else:
            color = (200, 0, 0)
        pygame.draw.rect(screen, color, self.rect)
        screen.blit(self.text, (self.rect.x, self.rect.y))


    def is_inside(self, pos):
        x1, y1 = self.rect.x, self.rect.y
        x2, y2 = x1 + self.rect.width, y1 + self.rect.height
        return x1 < pos[0] < x2 and y1 < pos[1] < y2

    def mouse_motion_event(self, pos):
        self.is_hover = self.is_inside(pos)

    def mouse_button_down(self, pos):
        if self.is_hover:
            self.mouse_button_is_down = True

    def mouse_button_up(self, pos):
        if self.mouse_button_is_down and self.is_hover:
            self.obj()
        self.mouse_button_is_down = False

    def key_down(self, key):
        pass