import pygame
class Buttom(pygame.sprite.Sprite):
    def __init__(self, x, y, color, centerx, centery):
        pygame.sprite.Sprite.__init__(self)
        self.size_x = x
        self.size_y = y
        self.color = color
        self.centerx = centerx
        self.centery = centery
        self.image = pygame.Surface((self.size_x, self.size_y))
        self.rect = self.image.get_rect()
        self.image.fill(self.color)
        self.rect.y = centerx
        self.rect.x = centery
        
    

    def single(self):
        Game_mode =1
        print (Game_mode)
    def versus(self):
        Game_mode = 0
        print (Game_mode)
    def show_rule(self):
        d = 1
    def updating(self):
        if self.typi == 'single':
            single()
        if self.typi == 'versus':
            versus ()
GREEN = (0,255,0)
BLACK = (0,0,0)
WIDTH = 1366
HEIGHT = 720
single ='single'
FPS = 30
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
b = Buttom(30,30, GREEN, 100, 100)
running = 1
all_sprites.add(b)
while running == 1:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()
    
    # Рендеринг
    screen.fill(GREEN)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()


        
    
    

    
