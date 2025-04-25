import pygame
import sys
import random

ANCHO = 800
ALTO = 600
FPS = 40

# COLORES
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
gris1 = (128, 128, 128)
verde = (0, 255, 0)
rojo = (255, 0, 0)
cafe = (63, 30, 12)
azul = (0, 0, 255)
naranja = (255, 165, 0)
cian = (0, 255, 255)
AMARILLO = (255, 255, 0)

# Clase para el Personaje (Pollito)
class Personaje(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(AMARILLO)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocidad = 5
        self.inicio_y = y  # Guardamos la posición inicial en Y

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.velocidad
        if keys[pygame.K_DOWN]:
            self.rect.y += self.velocidad

        # Mantener al personaje dentro de los límites verticales de la avenida
        if self.rect.top < 90:
            self.rect.top = 90
        if self.rect.bottom > 510:
            self.rect.bottom = 510

    def reset_position(self):
        self.rect.center = (ANCHO // 2, self.inicio_y)

# Clase para los Autos
class Auto(pygame.sprite.Sprite):
    def __init__(self, y, direccion):
        super().__init__()
        self.direccion = direccion
        self.color = random.choice([rojo, azul, naranja, cian])
        self.ancho = random.randrange(40, 70)
        self.alto = 30
        self.image = pygame.Surface([self.ancho, self.alto])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.velocidad = random.randrange(3, 8)

        if self.direccion == "izquierda":
            self.rect.right = 0 - self.ancho
        elif self.direccion == "derecha":
            self.rect.left = ANCHO + self.ancho

    def update(self):
        if self.direccion == "izquierda":
            self.rect.x += self.velocidad
            if self.rect.left > ANCHO:
                self.kill()  # Eliminar el auto cuando sale de la pantalla
        elif self.direccion == "derecha":
            self.rect.x -= self.velocidad
            if self.rect.right < 0:
                self.kill()  # Eliminar el auto cuando sale de la pantalla

pygame.init()
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("POLLITO THE GAME")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)  # Fuente para el texto

# Grupos de sprites
todos_los_sprites = pygame.sprite.Group()
autos = pygame.sprite.Group()
personaje = Personaje(ANCHO // 2, 490)  # Posición inicial en Y (cerca de la parte inferior)
todos_los_sprites.add(personaje)

# Vidas
vidas = 3

# Temporizador para generar autos
auto_timer = 0
auto_interval = 20  # Aumentamos la frecuencia de aparición
carriles_arriba = [150, 230]
carriles_abajo = [370, 450]

# Estado del juego
game_over = False
ganaste = False  # Nuevo estado para cuando el jugador gana

def mostrar_texto(surface, texto, color, x, y):
    texto_renderizado = font.render(texto, True, color)
    rect_texto = texto_renderizado.get_rect(center=(x, y))
    surface.blit(texto_renderizado, rect_texto)

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if not game_over and not ganaste:
        # Generar autos aleatoriamente
        auto_timer += 1
        if auto_timer >= auto_interval:
            auto_timer = 0
            direccion = random.choice(["izquierda", "derecha"])
            if direccion == "derecha":
                y_auto = random.choice(carriles_arriba)
            else:
                y_auto = random.choice(carriles_abajo)
            auto = Auto(y_auto, direccion)
            # Verificar colisión con autos existentes antes de añadir
            if not pygame.sprite.spritecollideany(auto, autos):
                autos.add(auto)
                todos_los_sprites.add(auto)

        # Actualizar sprites
        todos_los_sprites.update()

        # Comprobar colisiones entre el pollito y los autos
        colisiones = pygame.sprite.spritecollide(personaje, autos, False)
        if colisiones:
            vidas -= 1
            personaje.reset_position()
            # Eliminar los autos para que no haya colisiones múltiples inmediatas
            for auto in autos:
                auto.kill()

            if vidas <= 0:
                game_over = True

        # Comprobar si el pollito llegó al andén superior
        if personaje.rect.top <= 90:
            ganaste = True

    # Dibujar todo
    ventana.fill(NEGRO)
    # andenes
    pygame.draw.rect(ventana, gris1, (0, 0, 800, 90))
    pygame.draw.rect(ventana, gris1, (0, 510, 800, 90))
    # separador de la avenida
    pygame.draw.rect(ventana, gris1, (0, 280, 800, 40))
    # cesped
    pygame.draw.rect(ventana, verde, (10, 10, 780, 60))
    pygame.draw.rect(ventana, verde, (10, 530, 780, 60))
    # casas (mismo dibujo que antes)
    pygame.draw.rect(ventana, BLANCO, (30, 40, 30, 30))
    pygame.draw.rect(ventana, rojo, (30, 40, 30, 10))
    pygame.draw.rect(ventana, cafe, (40, 55, 10, 15))
    pygame.draw.rect(ventana, BLANCO, (90, 40, 30, 30))
    pygame.draw.rect(ventana, azul, (90, 40, 30, 10))
    pygame.draw.rect(ventana, cafe, (100, 55, 10, 15))
    pygame.draw.rect(ventana, BLANCO, (140, 40, 30, 30))
    pygame.draw.rect(ventana, naranja, (140, 40, 30, 10))
    pygame.draw.rect(ventana, cafe, (150, 55, 10, 15))
    pygame.draw.rect(ventana, BLANCO, (200, 40, 100, 30))
    pygame.draw.rect(ventana, cian, (200, 40, 100, 10))
    pygame.draw.rect(ventana, gris1, (230, 55, 40, 15))
    pygame.draw.rect(ventana, BLANCO, (350, 40, 30, 30))
    pygame.draw.rect(ventana, azul, (350, 40, 30, 10))
    pygame.draw.rect(ventana, cafe, (360, 55, 10, 15))
    pygame.draw.rect(ventana, BLANCO, (400, 40, 30, 30))
    pygame.draw.rect(ventana, naranja, (400, 40, 30, 10))
    pygame.draw.rect(ventana, cafe, (410, 55, 10, 15))
    pygame.draw.rect(ventana, BLANCO, (470, 40, 30, 30))
    pygame.draw.rect(ventana, rojo, (470, 40, 30, 10))
    pygame.draw.rect(ventana, cafe, (480, 55, 10, 15))
    pygame.draw.rect(ventana, BLANCO, (560, 40, 30, 30))
    pygame.draw.rect(ventana, azul, (560, 40, 30, 10))
    pygame.draw.rect(ventana, cafe, (570, 55, 10, 15))
    pygame.draw.rect(ventana, BLANCO, (620, 40, 30, 30))
    pygame.draw.rect(ventana, naranja, (620, 40, 30, 10))
    pygame.draw.rect(ventana, cafe, (630, 55, 10, 15))
    pygame.draw.rect(ventana, BLANCO, (690, 40, 30, 30))
    pygame.draw.rect(ventana, azul, (690, 40, 30, 10))
    pygame.draw.rect(ventana, cafe, (700, 55, 10, 15))
    pygame.draw.rect(ventana, BLANCO, (30, 540, 30, 30))
    pygame.draw.rect(ventana, rojo, (30, 540, 30, 10))
    pygame.draw.rect(ventana, cafe, (40, 555, 10, 15))
    pygame.draw.rect(ventana, BLANCO, (90, 540, 30, 30))
    pygame.draw.rect(ventana, azul, (90, 540, 30, 10))
    pygame.draw.rect(ventana, cafe, (100, 555, 10, 15))
    pygame.draw.rect(ventana, BLANCO, (140, 540, 30, 30))
    pygame.draw.rect(ventana, naranja, (140, 540, 30, 10))
    pygame.draw.rect(ventana, cafe, (150, 555, 10, 15))
    pygame.draw.rect(ventana, BLANCO, (200, 540, 170, 30))
    pygame.draw.rect(ventana, cian, (200, 540, 170, 10))
    pygame.draw.rect(ventana, gris1, (260, 555, 50, 15))
    pygame.draw.rect(ventana, BLANCO, (400, 540, 30, 30))
    pygame.draw.rect(ventana, naranja, (400, 540, 30, 10))
    pygame.draw.rect(ventana, cafe, (410, 555, 10, 15))
    pygame.draw.rect(ventana, BLANCO, (470, 540, 30, 30))
    pygame.draw.rect(ventana, rojo, (470, 540, 30, 10))
    pygame.draw.rect(ventana, cafe, (480, 555, 10, 15))
    pygame.draw.rect(ventana, BLANCO, (560, 540, 30, 30))
    pygame.draw.rect(ventana, azul, (560, 540, 30, 10))
    pygame.draw.rect(ventana, cafe, (570, 555, 10, 15))
    pygame.draw.rect(ventana, BLANCO, (620, 540, 30, 30))
    pygame.draw.rect(ventana, naranja, (620, 540, 30, 10))
    pygame.draw.rect(ventana, cafe, (630, 555, 10, 15))
    pygame.draw.rect(ventana, BLANCO, (690, 540, 30, 30))
    pygame.draw.rect(ventana, azul, (690, 540, 30, 10))
    pygame.draw.rect(ventana, cafe, (700, 555, 10, 15))

    # Dibujar los sprites (pollito y autos)
    todos_los_sprites.draw(ventana)

    # Mostrar vidas
    mostrar_texto(ventana, f"Vidas: {vidas}", BLANCO, 70, 30)

    # Mostrar Game Over
    if game_over:
        mostrar_texto(ventana, "GAME OVER", rojo, ANCHO // 2, ALTO // 2)

    # Mostrar "¡¡¡GANASTE!!!"
    if ganaste:
        mostrar_texto(ventana, "¡¡¡GANASTE!!!", verde, ANCHO // 2, ALTO // 2)

    pygame.display.flip()