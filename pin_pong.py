from pygame import *

WIN_WIDTH = 900
WIN_HEIGHT = 800
FPS = 60

display.set_caption('Ping-pong')
window = display.set_mode((WIN_WIDTH, WIN_HEIGHT))

class Sprite(sprite.Sprite):
    def __init__(self, x, y, width, height, image_file,):
        super().__init__()
        self.image = transform.scale(image.load(image_file),(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Racket(Sprite):
    def __init__(self, x, y, width, height, image_file, speed, k_up, k_down):
        super().__init__(x, y, width, height, image_file)
        self.speed = speed
        self.k_up = k_up
        self.k_down = k_down
    def update(self):
        keys = key.get_pressed()
        if keys[self.k_up] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[self.k_down] and self.rect.y < 800-self.rect.height:
            self.rect.y += self.speed

racket_left = Racket(10,300,50,200,'racket.png',8,K_w,K_s)
racket_right = Racket(840,300,50,200,'racket.png',8,K_UP,K_DOWN)

timer = time.Clock()

rackets = sprite.Group(racket_left,racket_right)

class Ball(Sprite):
    def __init__(self, x, y, width, height, image_file,speed):
        super().__init__(x, y, width, height, image_file)
        self.speed_x = speed
        self.speed_y = speed
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y < 0 or self.rect.y > 750:
            self.speed_y *= -1
        if sprite.spritecollide(self, rackets, False):
            self.speed_x *= -1

font.init() 

font_1 = font.Font(None, 50)
left_win = font_1.render('Победил левый игрок',True,(100,255,100))
right_win = font_1.render('Победил правый игрок',True,(100,255,100))

finish = False

game = True

ball = Ball(475,325,50,50,'ball.png',5)

left_lose = False
right_lose = False

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    window.fill((50, 64, 112))

    rackets.draw(window)
    ball.reset()

    if not finish:
        rackets.update()
        ball.update()
        if ball.rect.x < -50:
            left_lose = True
            finish = True
        if ball.rect.x > 900:
            right_lose = True
            finish = True

    if left_lose:
        window.blit(right_win,(250,350))
    if right_lose:
        window.blit(left_win,(250,350))

    display.update()
    timer.tick(FPS)
