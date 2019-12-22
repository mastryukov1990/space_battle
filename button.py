import pygame
import land
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
FPS = 50


class Button_Versus(pygame.sprite.Sprite):

    def __init__(self, x, y, x_size, y_size):
        pygame.sprite.Sprite.__init__(self)
        self.x_size = x_size
        self.y_size = y_size
        self.image = pygame.Surface((self.x_size, self.y_size))
        self.image.fill(RED)
        self.OWEN = (255, 0, 0)
        self.NEW = (0, 255, 0)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.button_timer = pygame.time.get_ticks()
        self.delay = 250

    def update(self):
        mouse_location = pygame.mouse.get_pos()
        mouse_press = pygame.mouse.get_pressed()
        now = pygame.time.get_ticks()
        if self.rect.collidepoint(mouse_location):
            self.image.fill((int(self.OWEN[0] / 2), int(self.OWEN[1] / 2), int(self.OWEN[2] / 2)))
        else:
            self.image.fill(self.OWEN)
        if now - self.button_timer > self.delay:
            self.button_timer = now

            if mouse_press[0] and self.rect.collidepoint(mouse_location):
                land.play()
                print(1)




t = pygame.init()

window = pygame.display.set_mode((800, 600))

sheldon = Button_Versus(10, 10, 100, 100)

all_sprites1 = pygame.sprite.Group()
all_sprites1.add(sheldon)

clock = pygame.time.Clock()
running = True
while running:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or \
                        (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    running = False

            window.fill(BLACK)
            all_sprites1.update()
            all_sprites1.draw(window)
            pygame.display.flip()
pygame.quit()

