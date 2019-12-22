import pygame
from Constants import c

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
        self.mobs = LAND.mobs
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
                self.rect.left = c['WIDTH'] / 2
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
                self.rect.right = c['WIDTH'] / 2
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
            add_Mob()
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
                    s_bullet1 = Super_Bullet(
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
                    s_bullet2 = Super_Bullet(
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
