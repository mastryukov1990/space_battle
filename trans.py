import pygame
pygame.init()
 
sc = pygame.display.set_mode((400, 300))
sc.fill((100, 150, 200))
 
dog_surf = pygame.Surface((50,150))
dog_surf.set_colorkey((0, 5, 255))
dog_rect = dog_surf.get_rect(center=(200, 150))
sc.blit(dog_surf, dog_rect)
rot = pygame.transform.rotate(dog_surf, 300)
rot_rect = rot.get_rect(center=(200, 150))
sc.blit(rot, rot_rect)
pygame.display.update()
angle = 0
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                # собака перевернется слева направо
                flip = pygame.transform.flip(dog_surf, 1, 0)
                sc.fill((100, 150, 200))
                sc.blit(flip, dog_rect)
                pygame.display.update(dog_rect)
                pygame.display.update(rot_rect)
                
                sc.blit(rot, dog_rect)
                angle = angle + 10
                rot = pygame.transform.rotate(dog_surf, angle)
 
    pygame.time.delay(20)