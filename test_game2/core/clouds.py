import pygame
from random import choice, randint, uniform
import os
import json
from typing import Literal

# Player Image constants and settings
CLOUD_DIR = r"C:\Users\tanner.martin\Desktop\test_game\test_game2\resources\Items"
AVAILABLE_CLOUD_PREFIXES = ["cloud0","cloud1", "cloud2", "cloud3", "cloud4", "cloud5"]
AVAILABLE_CLOUD_POSTFIXES = [""]
PRE_POST_SEPERATOR = ""
CLOUD_SS_PATH = os.path.join(CLOUD_DIR, "cloud6.png")

def generate_cloud_spritesheet_and_frames():
    
    cloud_image = pygame.image.load(CLOUD_SS_PATH)
    try:
        cloud_image = cloud_image.convert_alpha()
    except:
        ...
    cloud_width = int(cloud_image.get_width() / 3)
    cloud_height = int(cloud_image.get_height()/2)
    cloud_x, cloud_y = 0, 0
    cloud_frames = []
    for  i in range(3):
        cloud_frames.append({"x":cloud_x, "y":cloud_y, "w":cloud_width, "h":cloud_height})
        cloud_x += cloud_width
    cloud_x = 0
    cloud_y += cloud_height
    for  i in range(3):
        cloud_frames.append({"x":cloud_x, "y":cloud_y, "w":cloud_width, "h":cloud_height})
        cloud_x += cloud_width
    return cloud_image, cloud_frames

class Cloud(pygame.sprite.Sprite):
    def __init__(self, x:int):
        super().__init__()
        self.spritesheet, self.frames = generate_cloud_spritesheet_and_frames()
        self.animation_frames: list[pygame.surface.Surface] = []
        self.frame_index = 0
        self._frames_data_to_frames_animation()
        self.frame_index = randint(0, len(self.animation_frames)-1)
        self.image = self.animation_frames[self.frame_index]
        self.velocity = [-1,0]
        self.velocity_counter = uniform(0.01, 0.99)
        y = randint(0, 200)
        w = self.image.get_width()
        h = self.image.get_height()
        self.rect = pygame.Rect(x, y, w, h)
        self.random_y()
        self.frame_index = randint(0, len(self.animation_frames)-1)
        self.image: pygame.surface.Surface = self.animation_frames[self.frame_index]
        
    
    def _frames_data_to_frames_animation(self):
        for frame_data in self.frames:
            try:
                frame = self.spritesheet.subsurface(
                    pygame.Rect(
                        frame_data.get("x"),
                        frame_data.get("y"),
                        frame_data.get("w"),
                        frame_data.get("h"),
                    )
                )
                self.animation_frames.append(frame)
            except Exception as e:
                print(e)

    def get_image(self):
        self.change_frame_index()
        image = self.animation_frames[self.frame_index]
        return image
    
    def move(self, ww):
        if self.velocity[0] > 0 and self.rect.left >= ww:
            self.rect.right = -10
            self.random_y()
        elif self.velocity[0] < 0 and self.rect.right <= 0:
            self.rect.left = ww +10
            self.random_y()

    def change_frame_index(self):
        self.frame_index += 1
        if self.frame_index >= len(self.animation_frames):
            self.frame_index = 0
    
    def random_y(self):
        self.rect.y = randint(0, 200)
        if self.rect.y < 200:
            self.velocity[0] = -2
        if self.rect.y < 150:
            self.velocity[0] = -1

    def update(self):
        self.image = self.get_image()
        self.rect.move_ip(self.velocity)

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
    