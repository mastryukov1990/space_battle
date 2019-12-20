import pygame
all_sprites = pygame.sprite.Group()
FPS = 50
BLACK = (255, 0, 0)
def create_menu():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), flags = pygame.FULLSCREEN)
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()
    running = 1
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        all_sprites.update()
        screen.fill(BLACK)
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()
create_menu()