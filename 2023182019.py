from pico2d import *

class Ball:
    pass

class Boy:
    def __init__(self, x):
        self.x = x
        self.image = load_image("run_animation.png")
    
    def draw_boy(self, left, bottom):
        self.image.clip_draw(left, bottom, 100, 100, self.x, 50)

def programInit():
    pass

def handle_events():
    pass

running = True

open_canvas(800, 600)

programInit()

handle_events()

delay(5)

close_canvas()