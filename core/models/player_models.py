from pydantic import BaseModel, validator, model_validator, root_validator
from typing import Literal
from pygame.image import load
from pygame import Surface, surface, Rect
from pygame.display import update
from pygame.time import Clock
import os
from random import randint, choice

from core.constants import PLAYERS_DIR

player_images: dict[str, Surface] = dict()

player_images.update({"p3_stand":"C:\Users\tanner.martin\Desktop\test_game\resources\Player\p3_stand.png"})
player_images.update({"p2_stand":"C:\Users\tanner.martin\Desktop\test_game\resources\Player\p2_stand.png"})
player_images.update({"p1_stand":"C:\Users\tanner.martin\Desktop\test_game\resources\Player\p1_stand.png"})

class Plank:
    def __init__(
        self,
        surface_type: Literal["castle", "dirt", "grass", "sand", "snow", "stone"],
        size: Literal["small", "medium", "big"],
        window: Surface,
        x:int = 0,
        y:int = 0
    ):
        self.x = x
        self.y = y
        self.x_velocity = 0
        self.y_velocity = 0
        self.fall()
        while self.x_velocity == 0:
            self.x_velocity = randint(-3, 3)
        self.window = window
        self.surface_type = surface_type
        self.img_config = {
            "small": ["CliffLeft", "Mid", "CliffRight"],
            "medium": ["CliffLeft", "Mid", "Mid", "CliffRight"],
            "big": ["CliffLeft", "Mid", "Mid", "Mid", "CliffRight"],
        }
        self.image_names:list[str] = self.generate_image_names()

    def generate_image_names(self):
        return [self.surface_type+'.png' for i in player_images]
    
    @property
    def image_objects(self):
        return [player_images.get(i) for i in self.image_names]
    
    def get_window_width(self):
        return self.window.get_size()[0]
    
    def should_change_x_velocity(self, x:int|float, w:int|float):
        return x < 0 or x+w > self.get_window_width()
    
    def change_x_velocity(self):
        self.x_velocity *= -1
    
    def should_change_y_velocity(self, y:int|float, h:int|float):
        return y < 0 or y+h > self.get_window_height()
    
    def change_y_velocty(self):
        self.y_velocity *= -1
    
    def is_landing(self):
        ...
    
    def land(self):
        ...
    
    def should_fall(self):
        return self.y_velocity == 0
    
    def is_jumping(self):
        return self.y_velocity < 0
    
    def jump(self):
        self.y_velocity = -10
    
    def is_falling(self):
        return self.y_velocity > 0
    
    def fall(self):
        self.y_velocity = 1

    @property
    def image_rects(self):
        x, y = self.x, self.y
        w, h = 66, 92
        player_rect = Rect(x, y, w, h)
        return_rects:list[Rect] = [player_rect]

        for image in self.image_objects:
            w, h = image.get_size()
            return_rects.append()
            if self.should_change_x_velocity(x, w):
                self.change_x_velocity()
            x += w

        return return_rects
    
    @property
    def image_objects_and_rects(self):
        x, y = self.x, self.y
        return_objects_and_rects:list[tuple[Surface, Rect]] = []

        for image_object in self.image_objects:
            w, h = image_object.get_size()
            return_objects_and_rects.append((image_object, Rect(x, y, w, h)))
            if self.should_change_x_velocity(x, w):
                self.change_x_velocity()
            x += w

        return return_objects_and_rects
    
    def move(self):
        self.x += self.x_velocity
        self.y += self.y_velocity

    def draw(self):
        big_rect = Rect(self.x-10, self.y-10, 20, 20)
        return big_rect

    def collision_boxes(self):
        return self.image_rects