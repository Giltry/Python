import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mi Juego")

# Cargar la imagen del jugador y ajustar el tamaño
original_player_image = pygame.image.load("player.png")
player_width, player_height = 50, 50
player_image = pygame.transform.scale(original_player_image, (player_width, player_height))
player_rect = player_image.get_rect()

# Crear bloques
block_width, block_height = 50, 50
block1 = pygame.Rect(200, 300, block_width, block_height)
block2 = pygame.Rect(400, 300, block_width, block_height)

blocks = [block1, block2]

# Inicializar el reloj
clock = pygame.time.Clock()

# Velocidad de movimiento del jugador
player_speed = 5

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obtener las teclas presionadas
    keys = pygame.key.get_pressed()

    # Guardar la posición anterior del jugador
    old_player_rect = player_rect.copy()

    # Actualizar la posición del jugador
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_rect.x += player_speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_rect.y -= player_speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_rect.y += player_speed

    # Verificar colisiones con bloques
    for block in blocks:
        if player_rect.colliderect(block):
            # Si hay una colisión, revertir la posición del jugador
            player_rect = old_player_rect

    # Limpiar la pantalla
    screen.fill((255, 255, 255))

    # Dibujar al jugador en la pantalla
    screen.blit(player_image, player_rect)

    # Dibujar bloques
    for block in blocks:
        pygame.draw.rect(screen, (0, 0, 255), block)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad del juego
    clock.tick(60)  # 60 fotogramas por segundo

# Salir correctamente de Pygame
pygame.quit()
sys.exit()
