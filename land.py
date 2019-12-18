import pygame
import random
from tkinter import*
from MENUR import*
from reloads import*

Mob_size = 10
super_sec = 10

number_of_mobs = 40 # 20000-MAX
WIDTH = 1300
on = 1  # Mobi
mob_lives = 10
touch = 0
shield = 0
Game_mode = 1
xp = 10
WHITE = (255, 255, 255)
n = 1  # lives_Players
HEIGHT = 750
FPS = 50
Size_B = 6
Size_A = 6
s_live = 10
rnd = random.randrange
Nuber_of_STRIKE = 6
# Задаю цвета
all_parametrs = [
            Mob_size,
            super_sec,
            number_of_mobs,
            on,
            mob_lives,
            touch,
            shield,
            Game_mode,
            n,
            Nuber_of_STRIKE
            ]
f = open('Game_mode.txt')
Game_mode = int(f.read())

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def add_Mobi():
    m = Mobi(p1, p2)
    all_sprites.add(m)
    mobi.add(m)
    objects.add(m)
def versus():
    f1 = open('Game_mode.txt', 'w')
    f1.write('0')
    f1.close()
    root.destroy()
    play()


class SuperBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, stripe):
        pygame.sprite.Sprite.__init__(self)
        self.stripe = stripe
        self.s_sizeB = 8
        self.s_sizeA = 60
        self.image = pygame.Surface((self.s_sizeB, self.s_sizeA))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.y = int(y - self.s_sizeB / 2)
        self.rect.x = int(x - self.s_sizeA / 2)
        self.Vy = 5
        self.Vx = 5
        self.s_live = 5
        self.damage = 5

    def update(self):
        if self.stripe == 1:
            self.rect.x = self.rect.x - self.Vx
            if self.rect.left < 0:
                self.kill()
                
        if self.stripe == 2:
            self.rect.x = self.rect.x + self.Vx
            if self.rect.right > WIDTH:
                self.kill()
        hit_objects = pygame.sprite.spritecollide(self,objects,True,pygame.sprite.collide_rect)
        for hit in hit_objects:
            self.s_live = self.s_live - hit.damage
        if self.s_live < 0:
            self.kill()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, stripe):
        pygame.sprite.Sprite.__init__(self)
        self.stripe = stripe
        self.image = pygame.Surface((Size_B, Size_A))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.y = y - Size_B/2
        self.rect.x = x
        self.live = 1
        self.Vx = 10
        self.Vy = 10
        self.damage = 1

    def update(self):
        if self.stripe == 1:
            self.rect.x = self.rect.x - self.Vx
            if self.rect.left < 0:
                self.kill()
                p1.energy = p1.energy + 1
        if self.stripe == 2:
            self.rect.x = self.rect.x + self.Vx
            if self.rect.right > WIDTH:
                self.kill()
                p2.energy = p2.energy + 1
        if self.live == 0:
            self.kill()


class Mobi(pygame.sprite.Sprite):
    def __init__(self, p1, p2):
        pygame.sprite.Sprite.__init__(self)
        self.p1 = p1
        self.p2 = p2
        self.image = pygame.Surface((Mob_size, Mob_size))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.y = rnd(-580, 0)
        self.rect.x = rnd(10, 1360)
        self.speedy = rnd(1, 2)
        self.speedx = rnd(-2, 2)
        self.damage = 1
        self.touch = touch

    def update(self):
        self.rect.y = self.rect.y + self.speedy
        self.rect.x = self.rect.x + self.speedx
        if self.rect.y > HEIGHT or self.rect.x > WIDTH or self.rect.x < 0:
            self.rect.y = rnd(-80, 0)
            self.rect.x = rnd(-10, WIDTH)
        if self.damage == 0:
            self.rect.y = rnd(-80, 0)
            self.rect.x = rnd(100, WIDTH)
        hits_bullet1 = pygame.sprite.spritecollide(self, bullets1, True, pygame.sprite.collide_rect)
        for hit in hits_bullet1:
            self.damage -= hit.damage
            if self.damage <=0 :
                add_Mobi()
        hits_bullet2 = pygame.sprite.spritecollide(self, bullets2, True, pygame.sprite.collide_rect)
        for hit in hits_bullet2:
            self.damage -= hit.damage
            if self.damage <=0 :
                add_Mobi()
        if touch:

            hit = pygame.sprite.collide_rect(self, self.p1)

            if hit:
                if self.rect.left > p1.rect.right:
                    self.p1.rect.right = self.rect.left
                elif self.rect.right < p1.rect.left:
                    self.p1.rect.left = self.rect.right
            hit = pygame.sprite.collide_rect(self, self.p1)
            if hit:

                if self.rect.y < p1.rect.y:
                    self.p1.rect.top = self.rect.bottom
                else:
                    self.p1.rect.bottom = self.rect.top
            hit = pygame.sprite.collide_rect(self, self.p2)

            if hit:
                if self.rect.x > p2.rect.x:
                    self.p2.rect.right = self.rect.left
                else:
                    self.p2.rect.left = self.rect.right
            hit = pygame.sprite.collide_rect_top(self, self.p2)
            if hit:

                if self.rect.y < p2.rect.y:
                    self.p2.rect.top = self.rect.bottom
                else:
                    self.p2.rect.bottom = self.rect.top



class Health(pygame.sprite.Sprite):
    def __init__(self,p):
        pygame.sprite.Sprite.__init__(self)
        
        self.p = p
        self.stripe = self.p.stripe
        self.width = 100
        self.height = 8
        if self.stripe == 2:
            self.x = 30
            self.y = 30
        if self.stripe == 1:
            self.x = 1200
            self.y = 30
            
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.a = 10
        self.rect.center = (self.x , self.y  )
    def update(self):
        
        self.rect.x = self.x
        self.rect.y = self.y
        self.scaling()
    def scaling(self):
        self.image = pygame.transform.scale(
                                self.image,
                                (
                                self.p.xp * self.a,
                                self.height))

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
        self.super_sec = super_sec
        self.rect = self.image.get_rect()
        self.rect.center = (self.x / 2, self.y / 2)
        self.Vx = 5
        self.Vy = 5
        self.speedx = 0
        self.speedy = 0
        self.live = n
        self.energy = 10
        self.energy_start = 10
        self.shoot_delay = 300
        self.super_shoot_delay = 600
        self.super_energy = 20
        self.super_energy_start = 20
        self.last_shot = pygame.time.get_ticks()
        self.last_super_shot  = pygame.time.get_ticks()
        self.go = 300
        self.mobs = mobi
        self.last_go = pygame.time.get_ticks()
        self.xp = xp
        self.start_xp = xp
        self.bullets2 = bullets2
        self.bullets1 = bullets1
        
    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if self.stripe == 1:
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
            if self.rect.left < WIDTH/2:
                self.rect.left = WIDTH/2
            if keystate[pygame.K_LEFT]:
                self.speedx = -5
            if keystate[pygame.K_UP]:
                self.speedy = -5
            if keystate[pygame.K_DOWN]:
                self.speedy = 5
            if keystate[pygame.K_RIGHT]:
                self.speedx = 5
            if keystate[pygame.K_m]:
                p1.shoot()
            if keystate[pygame.K_RCTRL]:
                p1.super_shoot()
                
        if self.stripe == 2:
            if self.rect.right > WIDTH/2:
                self.rect.right = WIDTH/2
            if self.rect.left < 0:
                self.rect.left = 0
            if keystate[pygame.K_a]:
                self.speedx = -5
            if keystate[pygame.K_w]:
                self.speedy = -5
            if keystate[pygame.K_s]:
                self.speedy = 5
            if keystate[pygame.K_d]:
                self.speedx = 5
            if keystate[pygame.K_q]:
                p2.shoot()
            if keystate[pygame.K_LSHIFT]:
                p2.super_shoot()
                
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.y > HEIGHT - 50:
            self.rect.y = HEIGHT - 50
        if self.rect.top < 0:
            self.rect.top = 0
        hits_mobs = pygame.sprite.spritecollide(self, self.mobs, True, pygame.sprite.collide_circle)
        for hit in hits_mobs:
            self.xp -= 1
            
            add_Mobi()
        if self.stripe == 1:
            hits_bullet = pygame.sprite.spritecollide(self, self.bullets2,True, pygame.sprite.collide_circle)
            for hit in hits_bullet:
                self.xp -= hit.damage
            
        if self.stripe == 2:
            hits_bullet = pygame.sprite.spritecollide(self, self.bullets1,True, pygame.sprite.collide_circle)
            for hit in hits_bullet:
                self.xp -= hit.damage
        self.now_super_bullet = pygame.time.get_ticks()
        if self.super_energy_start  > self.super_energy:
            if self.now_super_bullet - self.last_super_shot > self.super_shoot_delay:
                if self.super_energy_start > self.super_energy:
                    self.last_super_shot = self.now_super_bullet
                    self.super_energy += 1
                    print(self.super_energy)
        self.now_bullet = pygame.time.get_ticks()
        if self.energy_start  > self.energy:
            if self.now_super_bullet - self.last_super_shot > self.super_shoot_delay:
                if self.energy_start > self.super_energy:
                    self.last_shot = self.now_bullet
                    self.energy += 1

    def shoot(self):
        if self.energy > 0:
            now = pygame.time.get_ticks() 
            if self.stripe == 1:
                if now - self.last_shot > self.shoot_delay:
                    self.last_shot = now
                    bullet = Bullet(self.rect.left - 8,
                                self.rect.centery,
                                self.stripe
                                )
                    all_sprites.add(bullet)
                    bullets1.add(bullet)
                    objects.add(bullet)
                    self.energy = self.energy
            if self.stripe == 2:
                if now - self.last_shot > self.shoot_delay:
                    self.last_shot = now
                    bullet = Bullet(self.rect.right + 8,
                                    self.rect.centery,
                                    self.stripe)
                    all_sprites.add(bullet)
                    bullets2.add(bullet)
                    objects.add(bullet)
                    self.energy = self.energy - 1

    def super_shoot(self):
        if self.super_energy == self.super_energy_start:
            if self.stripe == 1:
                s_bullet1 = SuperBullet(self.rect.left - 8,
                                    self.rect.centery,
                                    self.stripe
                                    )
                all_sprites.add(s_bullet1)
                bullets1.add(s_bullet1)
                self.super_energy = 1
            if self.stripe == 2:
                s_bullet2 = SuperBullet(self.rect.right + 8,
                                    self.rect.centery,
                                    self.stripe
                                    )
                all_sprites.add(s_bullet2)
                bullets2.add(s_bullet2)
                self.super_energy = 1

        
    def returnXP(self):
        return (int(self.xp))

    def returnSuper_time_reload(self):
        return (1)

bullets1 = pygame.sprite.Group()
bullets2 = pygame.sprite.Group()

mobi = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
objects = pygame.sprite.Group()
players = pygame.sprite.Group()

if Game_mode == 0:
    p1 = Player(1, WIDTH * 3/2, 200)
    all_sprites.add(p1)
    players.add(p1)
    all_sprites.add(p1)
    p2 = Player(2, WIDTH/2, 600)
    all_sprites.add(p2)
    players.add(p2)
    all_sprites.add(p2)
    h1 = Health(p1)
    all_sprites.add(h1)
    
    h2 = Health(p2)
    all_sprites.add(h2)
    r_super_1 = Reload(40,40,p1)
    all_sprites.add(r_super_1)
    r_super_2 = Reload(40,40,p2)
    all_sprites.add(r_super_2)
    
if Game_mode == 1:
    p1 = Player(1, WIDTH*3/2, 200)
    all_sprites.add(p1)
    players.add(p1)
    all_sprites.add(p1)
    p2 = Player(1, WIDTH*3/2, 200)
    all_sprites.add(p2)
    players.add(p2)
    all_sprites.add(p2)
    h1 = Health(p1)
    
    # Создаем ру и окно
    # Цикл игры

def play():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), flags = pygame.FULLSCREEN)
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()
    if on == 1:
        for i in range(number_of_mobs):
            add_Mobi()
    running = 1
    while running:
        clock.tick(FPS)
        hits = pygame.sprite.groupcollide(players, mobi, 1-shield,  1-shield)
        if hits and shield == 0:
            running = False
            add_Mobi()
        hitts1 = pygame.sprite.groupcollide(mobi, bullets1, True, False)
        if hitts1:
            p1.energy = p1.energy + 1
        hitts2 = pygame.sprite.groupcollide(mobi, bullets2, True, True)
        if hitts2:
            p2.energy = p2.energy + 1
        if on == 1:
            for hit in hitts1:
                add_Mobi()
        if on == 1:
            for hit in hitts2:
                add_Mobi()
        # Ввод процесса (события)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
        
        
        if p1.xp == 0 or p2.xp == 0:
            running = False    
        
        all_sprites.update()
        screen.fill(BLACK)
        all_sprites.draw(screen)
        pygame.display.flip()
        

    pygame.quit()
play()