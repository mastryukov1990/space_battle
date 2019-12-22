import pygame
import random
import math
from Constants import c
from reloads import ReloadSuperBullet, ReloadBullet

rnd = random.randrange


def add_mob():
    m = Mob(p1, p2)  # p1 and p2 - players
    all_sprites.add(m)
    mobs.add(m)
    objects.add(m)


class SuperBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, stripe):
        pygame.sprite.Sprite.__init__(self)
        self.stripe = stripe  # type of player (1 or 2)
        self.size_X = 8
        self.size_Y = 60
        self.image = pygame.Surface((self.size_X, self.size_Y))
        self.image.fill(c['WHITE'])
        self.rect = self.image.get_rect()
        self.rect.y = int(y - self.size_Y / 2)
        self.rect.x = x
        self.Vy = 5
        self.Vx = 5
        self.live = 5
        self.damage = c['super_bullet_damage']

    def update(self):
        if self.stripe == 1:
            self.rect.x = self.rect.x - self.Vx
            if self.rect.left < 0:
                self.kill()
        if self.stripe == 2:
            self.rect.x = self.rect.x + self.Vx
            if self.rect.right > c['WIDTH']:
                self.kill()
        hit_objects = pygame.sprite.spritecollide(
            self,
            objects,
            True,
            pygame.sprite.collide_rect
        )

        for hit in hit_objects:
            self.live = self.live - hit.damage
        if self.live < 0:
            self.kill()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, stripe):
        pygame.sprite.Sprite.__init__(self)
        self.stripe = stripe
        self.image = pygame.Surface((c['Bullet_size_X'], c['Bullet_size_Y']))

        if self.stripe == 1:
            self.image = pygame.transform.rotate(pygame.image.load('weak_bullet.png'), -90)
            self.image = pygame.transform.scale(self.image, (c['Bullet_size_X'] * 2, 2 * c['Bullet_size_Y']))
        if self.stripe == 2:
            self.image = pygame.transform.rotate(self.image, 90)
            self.image = pygame.transform.scale(pygame.image.load('meteor_bright.png'),
                                                (
                                                    c['Bullet_size_X'] * 2,
                                                    c['Bullet_size_Y'] * 2)
                                                )
        self.rect = self.image.get_rect()
        self.rect.y = int(y - c['Bullet_size_X'] / 2)
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
                p1.energy = p1.energy
        if self.stripe == 2:
            self.rect.x = self.rect.x + self.Vx
            if self.rect.right > c['WIDTH']:
                self.kill()
                p2.energy = p2.energy
        if self.live == 0:
            self.kill()


class Mob(pygame.sprite.Sprite):
    def __init__(self, p1, p2):
        pygame.sprite.Sprite.__init__(self)
        self.p1 = p1
        self.p2 = p2
        self.type = rnd(-1, 1)
        self.speedy = rnd(1, 2)
        self.speedx = rnd(-2, 2)
        self.damage = 1
        self.Mob_size = rnd(15, 30)
        if self.speedy == 0:
            self.angle = -90
        else:
            self.angle = -90 + math.atan(self.speedx / self.speedy) * 57.3

        if self.type == 0:
            self.image = pygame.transform.scale(pygame.image.load('meteor1_stone.png'),
                                                (int(self.Mob_size), int(self.Mob_size)))
            self.image = pygame.transform.rotate(self.image, self.angle)
        if self.type == 1:
            self.image = pygame.transform.scale(pygame.image.load('meteor2_stone.png'),
                                                (self.Mob_size, int(self.Mob_size)))
            self.image = pygame.transform.rotate(self.image, self.angle)
        if self.type == -1:
            self.image = pygame.transform.scale(pygame.image.load('meteor2_stone.png'),
                                                (self.Mob_size, int(self.Mob_size)))
            self.image = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.y = rnd(-580, 0)
        self.rect.x = rnd(10, 1360)
        self.last_update = pygame.time.get_ticks()
        self.frame = '1'

    def update(self):
        self.rect.y = self.rect.y + self.speedy
        self.rect.x = self.rect.x + self.speedx

        hits_bullet1 = pygame.sprite.spritecollide(self, bullets1, True, pygame.sprite.collide_rect)
        for hit in hits_bullet1:
            self.damage -= hit.damage

        hits_bullet2 = pygame.sprite.spritecollide(self, bullets2, True, pygame.sprite.collide_rect)
        for hit in hits_bullet2:
            self.damage -= hit.damage
        if self.rect.y > c['HEIGHT'] or self.rect.x > c['WIDTH'] or self.rect.x < 0:
            self.kill()
            add_mob()
        if self.damage <= 0:
            self.kill()
            add_mob()

    def animate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 300:
            self.last_update = now
            self.image = meteor[self.frame]
            self.image = pygame.transform.rotate(self.image, self.angle)
            if self.frame == '5':
                self.frame = '1'
            else:
                self.frame = str(int(self.frame) + 1)


class Shield(pygame.sprite.Sprite):
    def __init__(self, x, y, p):
        pygame.sprite.Sprite.__init__(self)
        self.p = p  # p-player
        self.stripe = self.p.stripe
        self.s_sizeB = 8
        self.s_sizeA = 60
        self.image = pygame.Surface((self.s_sizeB, self.s_sizeA))
        self.image.fill(c['WHITE'])
        self.rect = self.image.get_rect()
        self.rect.y = int(y - self.s_sizeB / 2)
        self.rect.x = int(x - self.s_sizeA / 2)
        self.Vy = 0
        self.Vx = 0
        self.live = self.p.super_energy
        self.damage = 5

    def update(self):
        if self.stripe == 1:
            self.rect.x = self.rect.x - self.Vx
            if self.rect.left < 0:
                self.kill()
            hit_objects = pygame.sprite.spritecollide(
                self,
                bullets2,
                True,
                pygame.sprite.collide_rect
            )

        if self.stripe == 2:
            self.rect.x = self.rect.x + self.Vx
            if self.rect.right > c['WIDTH']:
                self.kill()
            hit_objects = pygame.sprite.spritecollide(
                self,
                bullets1,
                True,
                pygame.sprite.collide_rect)

        for hit in hit_objects:
            if hit != self:
                self.live = self.live - hit.damage
        if self.live < 0:
            self.kill()


class Health(pygame.sprite.Sprite):
    def __init__(self, p):
        pygame.sprite.Sprite.__init__(self)

        self.p = p  # p-player
        self.stripe = self.p.stripe
        self.width = 100
        self.height = 8
        if self.stripe == 2:
            self.x = 90
            self.y = 30
        if self.stripe == 1:
            self.x = 1060
            self.y = 30

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.a = 10
        self.rect.center = (self.x, self.y)

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
        self.scaling()

    def scaling(self):
        if self.p.player_xp > 0:
            self.image = pygame.transform.scale(
                self.image,
                (
                    self.p.player_xp * self.a,
                    self.height
                )
            )


class Player(pygame.sprite.Sprite):
    def __init__(self, stripe, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.stripe = stripe
        self.x = x
        self.y = y
        self.image = None
        if stripe == 1:
            self.image = pygame.transform.scale(pygame.image.load('spaceship1.png'), (80, 80))
            self.image = pygame.transform.rotate(self.image, 90)
        if stripe == 2:
            self.image = pygame.transform.scale(pygame.image.load('spaceship2.png'), (80, 80))
            self.image = pygame.transform.rotate(self.image, -90)

        self.rect = self.image.get_rect()
        self.rect.center = (int(self.x / 2), int(self.y / 2))
        self.Vx = 6
        self.Vy = 6
        self.speedx = 0
        self.speedy = 0
        self.energy = 15
        self.energy_start = 10
        self.shoot_delay = 300
        self.super_shoot_delay = 600
        self.super_energy = 20
        self.super_energy_start = 20
        self.last_shot = pygame.time.get_ticks()
        self.last_super_shot = pygame.time.get_ticks()
        self.last_super_shotBullet = pygame.time.get_ticks()
        self.go = 300
        self.delay = 1000
        self.mobs = mobs
        self.last_go = pygame.time.get_ticks()
        self.player_xp = c['player_xp']
        self.start_xp = c['player_xp']
        self.bullets2 = bullets2
        self.bullets1 = bullets1
        self.shot = pygame.time.get_ticks()

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if self.stripe == 1:
            if self.rect.right > c['WIDTH']:
                self.rect.right = c['WIDTH']
            if self.rect.left < c['WIDTH'] / 2:
                self.rect.left = int(c['WIDTH'] / 2)
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
            if self.rect.right > c['WIDTH'] / 2:
                self.rect.right = int(c['WIDTH'] / 2)
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
        if self.rect.right > c['WIDTH']:
            self.rect.right = c['WIDTH']
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.y > c['HEIGHT'] - 50:
            self.rect.y = c['HEIGHT'] - 50
        if self.rect.top < 0:
            self.rect.top = 0
        hits_mobs = pygame.sprite.spritecollide(self, self.mobs, True, pygame.sprite.collide_circle)
        for hit in hits_mobs:
            self.player_xp -= hit.damage
            add_mob()
        if self.stripe == 1:
            hits_bullet = pygame.sprite.spritecollide(self, self.bullets2, True, pygame.sprite.collide_circle)
            for hit in hits_bullet:
                self.player_xp -= hit.damage

        if self.stripe == 2:
            hits_bullet = pygame.sprite.spritecollide(self, self.bullets1, True, pygame.sprite.collide_circle)
            for hit in hits_bullet:
                self.player_xp -= hit.damage
        self.now_super_bullet = pygame.time.get_ticks()
        if self.super_energy_start > self.super_energy:
            if self.now_super_bullet - self.last_super_shot > self.super_shoot_delay:
                if self.super_energy_start > self.super_energy:
                    self.last_super_shot = self.now_super_bullet
                    self.super_energy += 1
        self.now_bullet = pygame.time.get_ticks()
        if self.energy_start > self.energy:
            if self.now_bullet - self.shot > self.delay:
                if self.energy_start > self.energy:
                    self.shot = self.now_bullet
                    self.energy = self.energy + 1

    def shoot(self):
        if self.energy - 1 > 0:
            now = pygame.time.get_ticks()
            if self.stripe == 1:
                if now - self.last_shot > self.shoot_delay:
                    self.last_shot = now
                    bullet = Bullet(
                        self.rect.left - 8,
                        self.rect.centery,
                        self.stripe
                    )
                    all_sprites.add(bullet)
                    bullets1.add(bullet)
                    objects.add(bullet)
                    self.energy = self.energy - 1
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
        if self.super_energy - c['super_bullet_damage'] >= 1:
            now = pygame.time.get_ticks()
            if self.stripe == 1:
                if now - self.last_super_shotBullet > self.shoot_delay:
                    self.last_super_shotBullet = now
                    s_bullet1 = SuperBullet(
                        self.rect.left - 8,
                        self.rect.centery,
                        self.stripe
                    )
                    all_sprites.add(s_bullet1)
                    bullets1.add(s_bullet1)
                    self.super_energy = self.super_energy - s_bullet1.damage
            if self.stripe == 2:
                if now - self.last_shot > self.shoot_delay:
                    self.last_shot = now
                    s_bullet2 = SuperBullet(
                        self.rect.right + 8,
                        self.rect.centery,
                        self.stripe
                    )
                    all_sprites.add(s_bullet2)
                    bullets2.add(s_bullet2)
                    self.super_energy = self.super_energy - s_bullet2.damage

    def returnXP(self):
        return (int(self.player_xp))

    def returnSuper_time_reload(self):
        return (1)


background = pygame.image.load('star_field.png')
background_rect = background.get_rect()
bullets1 = pygame.sprite.Group()
# Creating_group
bullets2 = pygame.sprite.Group()
mobs = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
objects = pygame.sprite.Group()
players = pygame.sprite.Group()

p1 = Player(1, c['WIDTH'] * 3 / 2, 200)
all_sprites.add(p1)
players.add(p1)
all_sprites.add(p1)
p2 = Player(2, c['WIDTH'] / 2, 600)
all_sprites.add(p2)
players.add(p2)
all_sprites.add(p2)
h1 = Health(p1)
all_sprites.add(h1)
h2 = Health(p2)
all_sprites.add(h2)
r_super_1 = ReloadSuperBullet(40, 40, p1)
all_sprites.add(r_super_1)
r_super_2 = ReloadSuperBullet(90, 40, p2)
all_sprites.add(r_super_2)
r1 = ReloadBullet(40, 50, p1)
all_sprites.add(r1)
r2 = ReloadBullet(90, 50, p2)
all_sprites.add(r2)


def play():
    pygame.init()

    screen = pygame.display.set_mode((c['WIDTH'], c['HEIGHT']), flags=pygame.FULLSCREEN)
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()
    if c['creating_mobs'] == 1:
        for i in range(c['number_of_mobs']):
            add_mob()
    running = 1
    while running:
        clock.tick(c['FPS'])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if p1.player_xp <= 0 or p2.player_xp <= 0:
            running = False
        all_sprites.update()
        screen.fill(c['BLACK'])
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        pygame.display.flip()


play()
