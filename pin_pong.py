from pygame import *

WIN_WIDTH = 900
WIN_HEIGHT = 800
FPS = 60

display.set_caption('Ping-pong')
window = display.set_mode((WIN_WIDTH, WIN_HEIGHT))

class Sprite(sprite.Sprite):
    def __init__(self, x, y, width, height, image_file,):
        self.image = transform.scale(image.load(image_file),(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
        
timer = time.Clock()

font.init() 

game = True

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    window.fill((50, 64, 112))
    display.update()
    timer.tick(FPS)
