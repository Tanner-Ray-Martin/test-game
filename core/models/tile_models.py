from pydantic import BaseModel, validator, model_validator, root_validator
from typing import Literal
from pygame.image import load
from pygame import Surface, surface, Rect
from pygame.display import update
from pygame.time import Clock
import os

TILES_PATH = "C:\\Users\\tanner.martin\\Desktop\\test-game\\resources\\Tiles"
tile_images: dict[str, Surface] = dict()

for image_name in os.listdir(TILES_PATH):
    try:
        tile_images.update({image_name: load(os.path.join(TILES_PATH, image_name))})
    except:
        ...


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
        self.x_velocity = randint(-10, 10)
        self.window = window
        self.size = size
        self.surface_type = surface_type
        self.img_config = {
            "small": ["CliffLeft", "Mid", "CliffRight"],
            "medium": ["CliffLeft", "Mid", "Mid", "CliffRight"],
            "big": ["CliffLeft", "Mid", "Mid", "Mid", "CliffRight"],
        }
        self.image_names:list[str] = self.generate_image_names()

    def generate_image_names(self):
        return [self.surface_type+i+'.png' for i in self.img_config.get(self.size)]
    
    @property
    def image_objects(self):
        return [tile_images.get(i) for i in self.image_names]
    
    @property
    def image_rects(self):
        change_x_velocity = False
        x, y = self.x, self.y
        ww = self.window.get_size()[0]
        return_rects:list[Rect] = []
        for image in self.image_objects:
            w, h = image.get_size()
            return_rects.append(Rect(x, y, w, h))
            if x < 0 or x+w > ww:
                change_x_velocity = True
            x += w
        if change_x_velocity:
            self.x_velocity *= -1
        return return_rects
    
    def move(self):
        self.x += self.x_velocity

    def draw(self):
        big_rect = Rect(self.x-10, self.y-10, 20, 20)
        for image_obj, image_rect in list(zip(self.image_objects, self.image_rects)):
            self.window.blit(image_obj, image_rect)
            big_rect.width += image_rect.width
            big_rect.height = image_rect.height + 20
        return big_rect

    def collision_box(self):
        ...


class PlankImageModel(BaseModel):
    type_1: Literal["castle", "dirt", "grass", "sand", "snow", "stone"]
    small: list[str] = ["CliffLeft", "Mid", "CliffRight"]
    medium: list[str] = ["CliffLeft", "Mid", "Mid", "CliffRight"]
    big: list[str] = ["CliffLeft", "Mid", "Mid", "Mid", "CliffRight"]
    size_str: Literal["small", "medium", "big"] = "small"
    size_list: list[str] = []
    image_names: list = []

    @model_validator(mode="after")
    def generate_images(self):
        if self.size_str == "small":
            self.size_list = [i for i in self.small]
        elif self.size_str == "medium":
            self.size_list = [i for i in self.medium]
        elif self.size_str == "big":
            self.size_list = [i for i in self.big]
        self.image_names = [self.type_1 + i + ".png" for i in self.size_list]
        return self


if __name__ == "__main__":
    import pygame
    def events():
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return False
        return True
    pygame.init()
    window = pygame.display.set_mode((1300, 750))
    running = True
    planks:list[Plank] = []
    from random import choice, randint
    for i in range(50):
        st = choice(["castle", "dirt", "grass", "sand", "snow", "stone"])
        s = choice(["small", "big", "medium"])
        rx = randint(0, 700)
        ry = randint(0, 700)
        planks.append(Plank(surface_type=st, size=s, window=window, x=rx, y=ry))
    clock = Clock()
    while running:
        window.fill((0, 0, 0))
        bgs:list[Rect] = []
        for plank in planks:
            plank.move()
            br = plank.draw()
            bgs.append(br)
        update(bgs)
        
        running = events()
        clock.tick(60)
        

