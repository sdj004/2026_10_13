from pico2d import *
import random

class Ball:
    def __init__(self, size):
        self.x = random.randint(50, 750)
        self.y = random.randint(100, 500)
        self.size = size
        if size == 1 : self.image = load_image("ball21x21.png")
        else : self.image = load_image("ball41x41.png")

    def draw_ball(self):
        if self.size == 1 : self.image.draw(41, 41)   
        else : self.image.draw(41, 41)   

class Boy:
    def __init__(self):
        self.x = random.randint(50, 700)
        self.image = load_image("run_animation.png")
    
    def draw_boy(self, left, bottom):
        self.image.clip_draw(left, bottom, 100, 100, self.x, 50)

def programInit():
    team = []
    balls = []
    for _ in range(11):
        boy = Boy()
        team.append(boy)

    for _ in range(20):
        size = random.randint(0, 1)
        ball = Ball(size)
        balls.append(ball)

def handle_events():
    global running

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def drawScene():
    pass

running = True

open_canvas(800, 600)

programInit()

while running:
    clear_canvas()

    handle_events()

    drawScene()

    delay(0.01)

close_canvas()