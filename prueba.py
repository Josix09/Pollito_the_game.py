import pygame
import sys


ANCHO=800
ALTO=600

#COLORES
BLANCO=(255,255,255)
NEGRO=(0,0,0)
gris1=(128, 128, 128)
gris2=(137, 137, 137)
gris3=(112,112,112)
verde = (0,255,0)
rojo = (255, 0, 0)
cafe= (63, 30, 12)
azul = (0, 0, 255)
naranja = (255,165,0)
cian = (0, 255, 255)

pygame.init()
#VENTANA
ventana = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("POLLITO THE GAME")

clock = pygame.time.Clock()
while 1:
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    ventana.fill(NEGRO)
    #andenes
    pygame.draw.rect(ventana, gris1, (0, 0, 800,90))
    pygame.draw.rect(ventana, gris1, (0, 510, 800,90))
    # separador de la avenida
    pygame.draw.rect(ventana,gris1,(0,280,800,40))
    #cesped
    pygame.draw.rect(ventana,verde,(10,10,780,60))
    pygame.draw.rect(ventana,verde,(10,530,780,60))
    #casas
    #casa 1
    #estructura
    pygame.draw.rect(ventana,BLANCO,(30,40,30,30))
    #techo
    pygame.draw.rect(ventana,rojo,(30,40,30,10))
    #puerta
    pygame.draw.rect(ventana,cafe,(40,55,10,15))
    #casa 2
    #estructura
    pygame.draw.rect(ventana,BLANCO,(90,40,30,30))
    #techo
    pygame.draw.rect(ventana,azul,(90,40,30,10))
    #puerta 
    pygame.draw.rect(ventana,cafe,(100,55,10,15))
    #casa 3
    #estructura
    pygame.draw.rect(ventana,BLANCO,(140,40,30,30))
    #techo
    pygame.draw.rect(ventana,naranja,(140,40,30,10))
    #puerta 
    pygame.draw.rect(ventana,cafe,(150,55,10,15))
    # centrico comercialito 1
    #estructura
    pygame.draw.rect(ventana,BLANCO,(200,40,100,30))
    #techo
    pygame.draw.rect(ventana,cian,(200,40,100,10))
    #puerta 
    pygame.draw.rect(ventana,gris3,(230,55,40,15))
    #casa 4
    pygame.draw.rect(ventana,BLANCO,(350,40,30,30))
    #techo
    pygame.draw.rect(ventana,azul,(350,40,30,10))
    #puerta 
    pygame.draw.rect(ventana,cafe,(360,55,10,15))
    #casa 5
    #estructura
    pygame.draw.rect(ventana,BLANCO,(400,40,30,30))
    #techo
    pygame.draw.rect(ventana,naranja,(400,40,30,10))
    #puerta 
    pygame.draw.rect(ventana,cafe,(410,55,10,15))
     #casa 6
    #estructura
    pygame.draw.rect(ventana,BLANCO,(470,40,30,30))
    #techo
    pygame.draw.rect(ventana,rojo,(470,40,30,10))
    #puerta
    pygame.draw.rect(ventana,cafe,(480,55,10,15))
    #casa 7
    #estructura
    pygame.draw.rect(ventana,BLANCO,(560,40,30,30))
    #techo
    pygame.draw.rect(ventana,azul,(560,40,30,10))
    #puerta 
    pygame.draw.rect(ventana,cafe,(570,55,10,15))
    #casa 8
    #estructura
    pygame.draw.rect(ventana,BLANCO,(620,40,30,30))
    #techo
    pygame.draw.rect(ventana,naranja,(620,40,30,10))
    #puerta 
    pygame.draw.rect(ventana,cafe,(630,55,10,15))
    #casa 9
    #estructura
    pygame.draw.rect(ventana,BLANCO,(690,40,30,30))
    #techo
    pygame.draw.rect(ventana,azul,(690,40,30,10))
    #puerta 
    pygame.draw.rect(ventana,cafe,(700,55,10,15))
    #............................................
    #casas de abajo
    #............................................
    #casa 1
    #estructura
    pygame.draw.rect(ventana,BLANCO,(30,540,30,30))
    #techo
    pygame.draw.rect(ventana,rojo,(30,540,30,10))
    #puerta
    pygame.draw.rect(ventana,cafe,(40,555,10,15))
    #casa 2
    #estructura
    pygame.draw.rect(ventana,BLANCO,(90,540,30,30))
    #techo
    pygame.draw.rect(ventana,azul,(90,540,30,10))
    #puerta 
    pygame.draw.rect(ventana,cafe,(100,555,10,15))
    #casa 3
    #estructura
    pygame.draw.rect(ventana,BLANCO,(140,540,30,30))
    #techo
    pygame.draw.rect(ventana,naranja,(140,540,30,10))
    #puerta 
    pygame.draw.rect(ventana,cafe,(150,555,10,15))
    # centrico comercialito 1
    #estructura
    pygame.draw.rect(ventana,BLANCO,(200,540,170,30))
    #techo
    pygame.draw.rect(ventana,cian,(200,540,170,10))
    #puerta 
    pygame.draw.rect(ventana,gris3,(260,555,50,15))
    #casa 4
    #estructura
    pygame.draw.rect(ventana,BLANCO,(400,540,30,30))
    #techo
    pygame.draw.rect(ventana,naranja,(400,540,30,10))
    #puerta 
    pygame.draw.rect(ventana,cafe,(410,555,10,15))
    #casa 5
    #estructura
    pygame.draw.rect(ventana,BLANCO,(470,540,30,30))
    #techo
    pygame.draw.rect(ventana,rojo,(470,540,30,10))
    #puerta
    pygame.draw.rect(ventana,cafe,(480,555,10,15))
    #casa 6
    #estructura
    pygame.draw.rect(ventana,BLANCO,(560,540,30,30))
    #techo
    pygame.draw.rect(ventana,azul,(560,540,30,10))
    #puerta 
    pygame.draw.rect(ventana,cafe,(570,555,10,15))
    #casa 7
    #estructura
    pygame.draw.rect(ventana,BLANCO,(620,540,30,30))
    #techo
    pygame.draw.rect(ventana,naranja,(620,540,30,10))
    #puerta 
    pygame.draw.rect(ventana,cafe,(630,555,10,15))
    #casa 8
    #estructura
    pygame.draw.rect(ventana,BLANCO,(690,540,30,30))
    #techo
    pygame.draw.rect(ventana,azul,(690,540,30,10))
    #puerta 
    pygame.draw.rect(ventana,cafe,(700,555,10,15))

    #----------------------------------------------
    #----------------POLLITO-----------------------
    #---------------THE GAME-----------------------




    pygame.display.flip()