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
    def __init__(self):
        self.image = chosen_plank_image
        

    def move(self):
        ...

    def update(self):
        ...
