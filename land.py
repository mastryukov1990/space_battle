import pygame
import random
from tkinter import*
from button import*
from MENUR import*
Mob_size = 10
super_sec = 10
super_energy = 3
number_of_mobs = 10  # 20000-MAX
WIDTH = 1366
on = 1  # Mobi
mob_lives = 10
touch = 0
shield = 0
Game_mode = 1
WHITE = (255, 255, 255)
n = 1  # lives_Players
HEIGHT = 720
FPS = 50
Size_B = 6
Size_A = 6
rnd = random.randrange
Nuber_of_STRIKE = 5
# Задаю цвета
f = open('Game_mode.txt')
Game_mode = int(f.read())
print(Game_mode)
print(on)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def add_Mobi():
    m = Mobi(p1, p2)
    all_sprites.add(m)
    mobi.add(m)


class S_bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, stripe):
        pygame.sprite.Sprite.__init__(self)
        self.stripe = stripe
        self.image = pygame.Surface((s_sizeB, s_sizeA))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.y = y - s_sizeB/2
        self.rect.x = x
        self.Vy = 10
        self.Vx = 10
        self.s_live = s_live

    def update(self):
        if self.stripe == 1:
            self.rect.x = self.rect.x - self.Vx
            if self.rect.left < 0:
                self.kill()
                p1.s_energy = p1.s_energy + 1
        if self.stripe == 2:
            self.rect.x = self.rect.x + self.Vx
            if self.rect.right > WIDTH:
                self.kill()
                p2.s_energy = p2.s_energy + 1


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, stripe):
        pygame.sprite.Sprite.__init__(self)
        self.stripe = stripe
        self.image = pygame.Surface((Size_B, Size_A))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.y = y - Size_B/2
        self.rect.x = x
        self.Vx = 10
        self.Vy = 10

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


class Mobi(pygame.sprite.Sprite):
    def __init__(self, p1, p2):
        pygame.sprite.Sprite.__init__(self)
        self.p1 = p1
        self.p2 = p2
        self.image = pygame.Surface((Mob_size, Mob_size))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.y = rnd(-80, 0)
        self.rect.x = rnd(10, 1360)
        self.speedy = rnd(1, 2)
        self.speedx = rnd(-1, 1)
        self.live = mob_lives
        self.touch = touch

    def update(self):
        self.rect.y = self.rect.y + self.speedy
        self.rect.x = self.rect.x + self.speedx
        if self.rect.y > 700 or self.rect.x > WIDTH or self.rect.x < 0:
            self.rect.y = rnd(-80, 0)
            self.rect.x = rnd(-10, WIDTH)
        if self.live == 0:
            self.rect.y = rnd(-80, 0)
            self.rect.x = rnd(100, WIDTH)
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
            hit = pygame.sprite.collide_rect(self, self.p2)
            if hit:

                if self.rect.y < p2.rect.y:
                    self.p2.rect.top = self.rect.bottom
                else:
                    self.p2.rect.bottom = self.rect.top


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
        self.super_energy = super_energy
        self.super_sec = super_sec
        self.rect = self.image.get_rect()
        self.rect.center = (x / 2, y / 2)
        self.Vx = 5
        self.Vy = 5
        self.speedx = 0
        self.speedy = 0
        self.live = n
        self.energy = Nuber_of_STRIKE

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

    def shoot(self):
        if self.energy > 0:
            if self.stripe == 1:
                bullet = Bullet(self.rect.left - 8,
                                self.rect.centery,
                                self.stripe
                                )
                all_sprites.add(bullet)
                bullets1.add(bullet)
            if self.stripe == 2:
                bullet = Bullet(self.rect.right + 8,
                                self.rect.centery,
                                self.stripe)
                all_sprites.add(bullet)
                bullets2.add(bullet)
            self.energy = self.energy - 1

    def super_shoot(self):
        if self.super_energy > 0:
            if self.stripe == 1:
                s_bullet = S_bullet(self.rect.left - 8,
                                    self.rect.centery,
                                    self.stripe
                                    )
                all_sprites.add(s_bullet)
                bullets1.add(s_bullet)
            if self.stripe == 2:
                s_bullet = S_bullet(self.rect.right,
                                    self.rect.centery,
                                    self.stripe
                                    )
                all_sprites.add(s_bullet)
                bullets2.add(s_bullet)
            self.super_energy = self.super_energy - self.super_sec
bullets1 = pygame.sprite.Group()
bullets2 = pygame.sprite.Group()
mobi = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
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
if Game_mode == 1:
    p1 = Player(1, WIDTH*3/2, 200)
    all_sprites.add(p1)
    players.add(p1)
    all_sprites.add(p1)
    p2 = Player(1, WIDTH*3/2, 200)
    all_sprites.add(p2)
    players.add(p2)
    all_sprites.add(p2)
# Создаем игру и окно


def play():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()
    if on == 1:
        for i in range(number_of_mobs):
            add_Mobi()

    # Цикл игры
    running = True
    while running:
        # Держим цикл на правильной скорости
        clock.tick(FPS)
        hits = pygame.sprite.groupcollide(players, mobi, 1-shield,  1-shield)
        if hits and shield == 0:
            running = False
            add_Mobi()
        hitts1 = pygame.sprite.groupcollide(mobi, bullets1, True, True)
        if hitts1:
            p1.energy = p1.energy + 1

        hitts2 = pygame.sprite.groupcollide(mobi, bullets2, True, True)
        if hitts2:
            p2.energy = p2.energy + 1

        hittts1 = pygame.sprite.groupcollide(players, bullets1, True, False)
        if hittts1:
            running = False
        hittts2 = pygame.sprite.groupcollide(players, bullets2, True, False)
        if hittts2:
            running = False
        if on == 1:
            for hit in hitts1:
                m = Mobi(p1, p2)
                all_sprites.add(m)
                mobi.add(m)
        if on == 1:
            for hit in hitts2:
                m = Mobi(p1, p2)
                all_sprites.add(m)
                mobi.add(m)
        # Ввод процесса (события)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RALT:
                    p1.shoot()

                if event.key == pygame.K_q:
                    p2.shoot()

        all_sprites.update()
        screen.fill(BLACK)
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()
play()