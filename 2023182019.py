from pico2d import *
import random

class Ball:
    def __init__(self, size):
        self.x = random.randint(50, 750)
        self.y = 599
        self.size = size
        if size == 1 : self.image = load_image("ball21x21.png")
        else : self.image = load_image("ball41x41.png")

    def draw_ball(self):
        if self.size == 1 : self.image.draw(self.x, self.y, 21, 21)   
        else : self.image.draw(self.x, self.y, 41, 41)   

class Boy:
    def __init__(self):
        self.x = random.randint(50, 700)
        self.image = load_image("run_animation.png")
    
    def draw_boy(self, left, bottom):
        self.image.clip_draw(left, bottom, 100, 100, self.x, 50)

class Grass:
    pass

def programInit():
    global team
    global balls
    global frame

    frame = 0
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
    global team
    global balls

    for index in range(len(team)):
        team[index].draw_boy(left, bottom)

    for index in range(len(balls)):
        balls[index].draw_ball()

def caculatePosition():
    global left
    global bottom
    global frame
    global team

    frame = (frame + 1) % 8
    
    bottom = 0
    left = frame * 100

    for index in range(len(team)):
        team[index].x += 5

    for index in range(len(balls)):
        move = random.randint(3, 7)
        if balls[index].y - move > 25 : balls[index].y -= move


running = True

open_canvas(800, 600)

programInit()

while running:
    clear_canvas()

    caculatePosition()

    handle_events()

    drawScene()

    update_canvas()

    delay(0.05)

close_canvas()