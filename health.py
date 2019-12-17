
class Health(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.Surface((50, 50))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x / 2, self.y / 2)
    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
