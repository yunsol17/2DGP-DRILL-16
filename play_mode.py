import random

from pico2d import *
import game_framework

import game_world
from grass import Grass
from boy import Boy
from ball import Ball
from zombie import Zombie

# boy = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global boy
    global zombie
    grass = Grass()
    game_world.add_object(grass, 0)
    zombie = Zombie()
    game_world.add_object(zombie, 1)
    boy = Boy()
    boy.zombie=zombie
    game_world.add_object(boy, 1)


    game_world.add_collision_pair('zombie:ball', zombie, None)
    game_world.add_collision_pair('boy:zombie', boy, zombie)
def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    game_world.handle_collisions()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

