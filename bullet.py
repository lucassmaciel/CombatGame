import pygame
from constants import BLOCK_SIZE
import math


class Bullet(pygame.sprite.Sprite):
    def __init__(self, color, pos, dir):
        super().__init__()
        self.image = pygame.Surface([5, 5])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = 10
        if isinstance(dir[0], (int, float)) and isinstance(dir[1], (int, float)):
            self.dir = self.normalize(dir) 
        else:
            raise ValueError("Os valores de dir devem ser números.")

    def normalize(self, vector):
        magnitude = math.sqrt(vector[0]**2 + vector[1]**2)
        if magnitude == 0:
            return (0, 0)
        return (vector[0] / magnitude, vector[1] / magnitude)

    def update(self, walls, players):
        self.rect.x += self.dir[0] * self.speed
        self.rect.y += self.dir[1] * self.speed

        for wall in walls:
            wall_rect = pygame.Rect(wall[0], wall[1], BLOCK_SIZE, BLOCK_SIZE)
            if self.rect.colliderect(wall_rect):
                self.kill()
                break

        for player in players:
            if self.rect.colliderect(player.rect):
                self.kill()
                player.hit() 
                break
