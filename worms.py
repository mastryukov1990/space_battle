import pygame
import random
rnd = random.randrange
BLACK = (0,0,0)
WIDTH = 500
HEIGHT = 500
HIEGHT = 500
GREEN =(255,0,0)
BLUE = (0,255,0)
n =1
r = 100
Mob_size = 20
RED = (0,0,255)
Nuber_of_STRIKE =1
def add_Mobi():
    m = Mobi(p1,p2)
    all_sprites.add(m)
    mobi.add(m)
class Mobi(pygame.sprite.Sprite):
    def __init__(self, p1,p2):
        pygame.sprite.Sprite.__init__(self)
        self.p1 = p1
        self.p2 = p2
        self.image = pygame.Surface((Mob_size,Mob_size))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.y = rnd(0, 20)
        self.rect.x = rnd(10, 500)
        self.speedy = 0
        self.speedx = 0
        self.live = n
        self.b = 1
    def update(self):
        self.speedy = self.speedy + self.b
        self.rect.y = self.rect.y + self.speedy
        self.rect.x = self.rect.x + self.speedx
        if self.rect.y >HIEGHT-100  :
            self.rect.y = HEIGHT-100
        if self.live == 0:
            self.rect.y = rnd(-80,0)
            self.rect.x = rnd(100,WIDTH)
        
        
        hit1 = pygame.sprite.collide_rect(self, self.p1)
            
        
        if hit1:
            p1.a=0
            if self.rect.y < p1.rect.y:
                self.p1.rect.top = self.rect.bottom
            else:
                self.p1.rect.bottom = self.rect.top+5
        
        hit = pygame.sprite.collide_rect(self, self.p2)
        
        if hit:
            p2.a=0
            if self.rect.y < p2.rect.y:
                self.p2.rect.top = self.rect.bottom
            else:
                self.p2.rect.bottom = self.rect.top-4
        

    
class Player(pygame.sprite.Sprite):
    def __init__(self, stripe, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.stripe = stripe
        self.x = x
        self.y = y
        self.image = pygame.Surface((50, 50))
        if stripe == 1:
            self.image.fill(GREEN)
        if stripe == 2:
            self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (x/ 2 , y / 2)
        self.Vx = 5
        self.Vy = 5
        self.a = 0.5
        self.speedx = 0
        self.speedy = 0
        self.live = n
        self.energy = Nuber_of_STRIKE
    def update(self):
        
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if self.stripe == 1:
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
            if self.rect.left < WIDTH/2:
                self.rect.left = WIDTH/2
            if  keystate[pygame.K_LEFT]:
                self.speedx = -5
            if  keystate[pygame.K_UP]:
                self.speedy = -5 
            if  keystate[pygame.K_DOWN]:
                self.speedy = 5
            if  keystate[pygame.K_RIGHT]:
                self.speedx = 5
            
        if self.stripe == 2:
            if self.rect.right > WIDTH/2:
                self.rect.right = WIDTH/2
            if self.rect.left < 0:
                self.rect.left = 0
            if  keystate[pygame.K_a]:
                self.speedx = -5
            if  keystate[pygame.K_w]:
                self.speedy = -5 
            if  keystate[pygame.K_s]:
                self.speedy = 5
            if  keystate[pygame.K_d]:
                self.speedx = 5
        self.speedy = self.speedy + self.a
        self.rect.x += self.speedx
        self.rect.y += self.speedy 
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.y> HEIGHT-50:
            self.rect.y = HEIGHT - 50
        if self.rect.top < 0:
            self.rect.top = 0
all_sprites = pygame.sprite.Group()
mobi = pygame.sprite.Group()
p1 = Player(1,100,-100)
p2 = Player(2,20,-100)
for i in range (r):
    add_Mobi()
    
all_sprites.add(p1)
all_sprites.add(p2)
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH+100, HIEGHT+100))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
running = 1
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0
    all_sprites.update()
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()