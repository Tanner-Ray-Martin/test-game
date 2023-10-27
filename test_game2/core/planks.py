import pygame
from random import choice
import os
import json
from typing import Literal

# Player Image constants and settings
PLANK_DIR = r"C:\Users\tanner.martin\Desktop\test_game\test_game2\resources\Planks"
chosen_plank_name = "grassMid"
chosen_plank_image_name = chosen_plank_name + ".png"
chosen_plank_image_path = os.path.join(PLANK_DIR, chosen_plank_image_name)
chosen_plank_image = pygame.image.load(chosen_plank_image_path)


class Plank:
    def __init__(self, x:int, y:int):
        self.image = chosen_plank_image
        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.velocity = [0, 1]
        
    def move(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def update(self, window:pygame.Surface):
        window.blit(self.image, self.rect)

class Ground:
    def __init__(self, ww:int, wh:int, window:pygame.Surface):
        self.planks:list[Plank] = []
        x = 0
        pw = chosen_plank_image.get_width()
        ph = chosen_plank_image.get_height()
        self.height = wh-ph
        y = wh-ph
        while x < ww:
            self.planks.append(Plank(x, y))
            x += pw
        self.window = window

    def update(self):
        [i.update(self.window) for i in self.planks]
