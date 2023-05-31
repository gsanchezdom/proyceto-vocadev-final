import pygame
import random
import sys
import os
import webbrowser
from pygame.locals import *
from boton import Boton


pygame.init()


screen = 1280, 720
screen = pygame.display.set_mode((screen))

musica = ["musica1.mp3", "musica2.mp3", "musica3.mp3"]

pygame.mixer.music.load(random.choice(musica))
pygame.mixer.music.play(-1)



pygame.display.set_caption("Minijuegos")


menu_snake = os.path.abspath("snake_menu.py")
menu_pong = os.path.abspath("pong_menu.py")

# Definir Colores


FONDO = (32, 30, 32)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
COLOR_TEXTO = (75, 75, 75)


# Definir Colores
hola = pygame.image.load('background.jpg')
screen.blit(hola,(0,0))



icono = pygame.image.load("bb-img.png")
pygame.display.set_icon(icono)

font = pygame.font.Font(None, 70)

text = font.render("¡Bienvenido al Juego!", True, (255, 255, 255))

# Obtener el rectángulo del objeto de texto
text_rect = text.get_rect()

# Centrar el texto en la ventana
text_rect = (380, 75)


start = True

boton1 = Boton(280, 250, 200, 100, COLOR_TEXTO, BLANCO, VERDE, 'SNAKE', 50)
boton2 = Boton(800, 250, 200, 100, COLOR_TEXTO, BLANCO, AZUL, 'PONG', 50)
boton3 = Boton(540, 450, 200, 50, COLOR_TEXTO, BLANCO, ROJO, 'LANDING PAGE', 30)

botones = [boton1, boton2, boton3]

def inside_button_snake(mouse_pos):
    x = mouse_pos[0]
    y = mouse_pos[1]
    if x >= 280 and x <= 480 and y >= 250 and y <= 350:
        return True
    return False  

def inside_button_pong(mouse_pos):
    x = mouse_pos[0]
    y = mouse_pos[1]
    if x >= 800 and x <= 1000 and y >= 250 and y <= 350:
        return True
    return False  

def inside_button_landing_page(mouse_pos):
    x = mouse_pos[0]
    y = mouse_pos[1]
    if x >= 540 and x <= 740 and y >= 450 and y <= 500:
        return True
    return False
    

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if inside_button_snake(mouse_pos):
                    os.system(menu_snake)
                if inside_button_pong(mouse_pos):
                    os.system(menu_pong)
                if inside_button_landing_page(mouse_pos):
                    webbrowser.open('https://blueberry-malaga--newmalagabrand.repl.co/index.html')
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
           
    pygame.display.update()
    


pygame.quit()