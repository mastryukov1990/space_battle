import pygame
from Constants import c
objects = pygame.sprite.Group()
class Super_Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, stripe):
        pygame.sprite.Sprite.__init__(self)
        self.stripe = stripe
        self.size_X = 8
        self.size_Y = 60
        self.image = pygame.Surface((self.size_X, self.size_Y))
        self.image.fill(c['WHITE'])
        self.rect = self.image.get_rect()
        self.rect.y = y - self.size_Y / 2
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