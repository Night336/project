import pygame

class Input():
    def __init__(self, text):
        self.size = 24
        self.font = pygame.font.Font(None, self.size)
        self.default_text = self.font.render(text, True, (100, 100, 100))
        self.text = ''
        self.rend_text = self.font.render(self.text, True, (0, 0, 0))
        self.rect = pygame.Rect(0, 0, 10, 10)

        self.is_hover = False
        self.mouse_button_is_down = False
        self.is_active = False

    def get_text(self):
        return self.text

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y
    
    def set_size(self, width, heigh):
        self.rect.width = width
        self.rect.height = heigh

    def draw(self, screen):
        if self.is_active:
            color = (255, 255, 255)
        else:
            color = (200, 200, 200)
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, width=2)
        if not self.is_active and not self.text:
            screen.blit(self.default_text, (self.rect.x, self.rect.y + 10))
        else:
            screen.blit(self.rend_text, (self.rect.x, self.rect.y + 10))


    def is_inside(self, pos):
        x1, y1 = self.rect.x, self.rect.y
        x2, y2 = x1 + self.rect.width, y1 + self.rect.height
        return x1 < pos[0] < x2 and y1 < pos[1] < y2

    def key_down(self, event):
        if self.is_active:
            if event.unicode.isalpha():
                self.text += event.unicode
                self.rend_text = self.font.render(self.text, True, (0, 0, 0))
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
                self.rend_text = self.font.render(self.text, True, (0, 0, 0))



    def mouse_motion_event(self, pos):
        self.is_hover = self.is_inside(pos)

    def mouse_button_down(self, pos):
        if self.is_hover:
            self.is_active = True
        else:
            self.is_active = False

    def mouse_button_up(self, pos):
        pass