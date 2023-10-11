from pygame.time import Clock
from core.models.tile_models import Plank
from pygame import Surface, Rect
from pygame.display import update

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