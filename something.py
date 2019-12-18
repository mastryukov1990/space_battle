import pygame
pygame.init()
sc = pygame.display.set_mode((400, 300))
sc.fill((100, 150, 200))
dog_surf = pygame.image.load('dog2.bmp')
dog_rect = dog_surf.get_rect(bottomright = (400, 300))
sc.blit(dog_surf, dog_rect)

pygame.display.update()

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

    pygame.time.delay(20)