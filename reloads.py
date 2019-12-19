import pygame
class Reload(pygame.sprite.Sprite):
    def __init__(self,x,y,p):
        pygame.sprite.Sprite.__init__(self)
        self.p = p
        self.width = 100
        self.height = 8
        if self.p.stripe == 2:
            self.x = x
            self.y = y
        if self.p.stripe == 1:
            self.x = 1100 - x
            self.y = y

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((0,255,255))
        self.rect = self.image.get_rect()
        self.a = 10
        self.rect.center = (self.x / 2 , self.y / 2)
    def update(self):
    
        self.rect.x = self.x
        self.rect.y = self.y
        self.scaling()
    def scaling(self):

        self.image = pygame.transform.scale(
                                self.image,
                                (self.p.super_energy
                                *self.a,
                                self.height))


class Reload_Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,p):
        pygame.sprite.Sprite.__init__(self)
        self.p = p
        self.width = 100
        self.height = 8
        if self.p.stripe == 2:
            self.x = x
            self.y = y
        if self.p.stripe == 1:
            self.x = 1100 - x
            self.y = y

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((0,255,255))
        self.rect = self.image.get_rect()
        self.a = 10
        self.rect.center = (self.x / 2 , self.y / 2)
    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
        self.scaling()
    def scaling(self):
        self.image = pygame.transform.scale(
                                self.image,
                                (self.p.energy
                                *self.a,
                                self.height)
                                )