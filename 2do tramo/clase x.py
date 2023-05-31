from Class_personaje import Personaje
import pygame, sys

#AREA de constantes
LARGO = 1000
ALTO = 600
screen_size = (LARGO, ALTO)

FPS = 30

pygame.init()

PANTALLA = pygame.display.set_mode((screen_size))#Pixeles

#ICONO
icono = pygame.image.load("Recursos/icono_homero.png")
pygame.display.set_icon((icono))

#FONDO
fondo = pygame.image.load("Recursos/fondo_casa.jpg")
fondo_escalado = pygame.transform.scale(fondo, screen_size)
PANTALLA.blit(fondo_escalado, (0,0))

#MUSICA
pygame.mixer.music.load("Recursos/intro.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.09)

PANTALLA = pygame.display.set_mode((LARGO, ALTO))#Pixeles
clock = pygame.time.Clock()

homero = Personaje((200,200), (LARGO/2, ALTO/2), "Recursos/homero.png")
dona = Personaje((100,100), (LARGO/2, ALTO), "Recursos/dona.png")

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    PANTALLA.blit(fondo_escalado, (0,0))             
    PANTALLA.blit(dona.superficie, dona.rectangulo)
    PANTALLA.blit(homero.superficie, homero.rectangulo)
    
    #MOVIMIENTO
    homero.mover_imagen("Horizontal", 10, (LARGO,ALTO))
    dona.mover_imagen("Vertical", 10, (LARGO,ALTO))
    
    #COLISION
    homero.detectar_colision(dona)
        
    pygame.display.flip()
        
