import pygame
pygame.init()

def rot_center( rect, angle):
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image,rot_rect
sc = pygame.display.set_mode((400, 300))
sc.fill((100, 150, 200))
 
dog_surf = pygame.Surface((50,50))
dog_surf.set_colorkey((255, 255, 255))
dog_rect = dog_surf.get_rect(center=(200, 150))
sc.blit(dog_surf, dog_rect)
 
pygame.display.update()
 
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.KEYDOWN:
            rot_center(image, rect, angle)
            flip = pygame.transform.flip(dog_surf, 100, 0)
            sc.fill((100, 150, 200))
            sc.blit(flip, dog_rect)
            pygame.display.update(dog_rect)
 
    pygame.time.delay(20)