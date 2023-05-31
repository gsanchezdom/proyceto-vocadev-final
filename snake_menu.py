import pygame
import os
from boton import Boton

pygame.init() # now use display and fonts

''''class Dificultad_x:
    def __init__(self, difficulty = 10):
        self.difficulty = difficulty

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
    
    def get_difficulty(self):
        return self.difficulty'''

dificultad = 0

musica = "musica5.mp3"
pygame.mixer.music.load(musica)
pygame.mixer.music.play(-1)

juego_snake_facil = os.path.abspath("snake_facil.py")
juego_snake_medio = os.path.abspath("snake_medio.py")
juego_snake_dificil = os.path.abspath("snake_dificil.py")

BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
NARANJA = (255, 128, 0)
COLOR_TEXTO = (176, 243, 151)

screen = 1280, 720
screen = pygame.display.set_mode((screen))
pygame.display.set_caption("Menú Snake")

# Definir Colores
hola = pygame.image.load('504.jpg')
screen.blit(hola,(0,0))



icono = pygame.image.load("bb-img.png")
pygame.display.set_icon(icono)

font = pygame.font.Font(None, 100)



text = font.render("¡Snake!", True, (100, 255, 100))

# Obtener el rectángulo del objeto de texto
text_rect = text.get_rect()

# Centrar el texto en la ventana
text_rect = (525, 75)

boton_easy = Boton(280, 250, 200, 100, COLOR_TEXTO, BLANCO, VERDE, 'Fácil', 50)
boton_medium = Boton(800, 250, 200, 100, COLOR_TEXTO, BLANCO, NARANJA, 'Medio', 50)
boton_hard = Boton(540, 450, 200, 50, COLOR_TEXTO, BLANCO, ROJO, 'Difícil', 50)

botones = [boton_easy, boton_medium, boton_hard]

start = True


def inside_button_easy(mouse_pos):
    x = mouse_pos[0]
    y = mouse_pos[1]
    print(mouse_pos)
    if x >= 280 and x <= 480 and y >= 250 and y <= 350:
        dificultad = 10
        return True
    return False

def inside_button_medium(mouse_pos):
    x = mouse_pos[0]
    y = mouse_pos[1]
    if x >= 800 and x <= 1000 and y >= 250 and y <= 350:
        dificultad = 25
        return True
    return False

def inside_button_hard(mouse_pos):
    x = mouse_pos[0]
    y = mouse_pos[1]
    if x >= 540 and x <= 740 and y >= 450 and y <= 500:
        dificultad = 40
        return True
    return False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if inside_button_easy(mouse_pos):
                    os.system(juego_snake_facil)
                if inside_button_medium(mouse_pos):
                    os.system(juego_snake_medio)
                if inside_button_hard(mouse_pos):
                    os.system(juego_snake_dificil)
                else:
                    pass

    # Obtener la posición del mouse
    mouse_pos = pygame.mouse.get_pos()

    # Dibujar en la pantalla
    screen.blit(text, text_rect)  # Dibuja el texto en la pantalla
    pygame.display.flip()  # Actualiza la pantalla

    # Actualizar los botones
    for boton in botones:
        boton.update(mouse_pos)


    # Dibujar los botones
    for boton in botones:
        boton.draw(screen)