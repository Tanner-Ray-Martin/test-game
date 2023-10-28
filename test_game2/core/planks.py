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
def generate_plank_spritesheet_and_frames():
    
    cloud_image = pygame.image.load(chosen_plank_image_path)
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
    return cloud_image, cloud_frames, cloud_width, cloud_height


class Plank:
    def __init__(self, x:int, y:int):
        self.spritesheet, self.frames, imw, imh = generate_plank_spritesheet_and_frames()
        self.image = self.frames_data_to_frames_animation()
        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.velocity = [0, 1]
    def frames_data_to_frames_animation(self)->pygame.surface.Surface:
        animation_frames = []
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
                animation_frames.append(frame)
            except Exception as e:
                print(e)
        return choice(animation_frames)
    def move(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def update(self, window:pygame.Surface):
        window.blit(self.image, self.rect)

class Ground:
    def __init__(self, ww:int, wh:int, window:pygame.Surface):
        self.planks:list[Plank] = []
        x = 0
        pw = int(pygame.image.load(chosen_plank_image_path).convert().get_width()/3)
        ph = int(pygame.image.load(chosen_plank_image_path).convert().get_height()/2)
        self.height = wh-ph
        y = wh-ph
        while x < ww:
            self.planks.append(Plank(x, y))
            x += pw
        self.window = window

    def update(self):
        [i.update(self.window) for i in self.planks]
