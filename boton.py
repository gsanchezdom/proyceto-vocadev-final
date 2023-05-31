import pygame

class Boton:
    def __init__(self, x, y, width, height, text_color, inactive_color, active_color, text='', font_size=''):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = inactive_color
        self.text_color = text_color
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.text = text
        self.font = pygame.font.Font(None, font_size)
        self.text_surface = self.font.render(text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

    def update(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.color = self.active_color
        else:
            self.color = self.inactive_color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, 2)
        surface.blit(self.text_surface, self.text_rect)
