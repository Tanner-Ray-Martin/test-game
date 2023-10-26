import pygame
from random import choice, randint, uniform
import os
import json
from typing import Literal

# Player Image constants and settings
CLOUD_DIR = r"C:\Users\tanner.martin\Desktop\test_game\test_game2\resources\Items"
AVAILABLE_CLOUD_PREFIXES = ["cloud1", "cloud2", "cloud3"]
AVAILABLE_CLOUD_POSTFIXES = [""]
PRE_POST_SEPERATOR = ""

class Cloud:
    def __init__(self, x:int):
        self.velocity = randint(1, 3)
        self.velocity_counter = uniform(0.01, 0.99)
        self.image = generate_cloud_image()
        flipped = choice([True, False])
        if flipped:
            self.image = pygame.transform.flip(self.image, True, False)
        y = randint(0, 300)
        w = self.image.get_width()
        h = self.image.get_height()
        self.rect = pygame.Rect(x, y, w, h)

    def move(self, ww):
        self.velocity_counter += 0.1
        if self.velocity_counter > 1:
            self.velocity_counter = 0
            self.rect.x += 2
        if self.velocity > 0 and self.rect.left >= ww:
            self.rect.right = -10
        elif self.velocity < 0 and self.rect.right <= 0:
            self.rect.left = ww +10

    def update(self, surface:pygame.surface.Surface):
        surface.blit(self.image, self.rect)

def get_random_cloud_image_name():
    return choice(AVAILABLE_CLOUD_PREFIXES)+'.png'

def get_cloud_path(image_name:str):
    return os.path.join(CLOUD_DIR, image_name)

def load_cloud_image(image_path:str):
    image = pygame.image.load(image_path)
    try:
        image = image.convert_alpha()
    except:
        ...
    return image

def generate_cloud_image():
    image_name = get_random_cloud_image_name()
    image_path = get_cloud_path(image_name)
    return load_cloud_image(image_path)
    