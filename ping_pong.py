from pygame import *

wind = display.set_mode((700, 500))
display.set_caption('PiPo')
background = transform.scale(image.load('background_city.png'), (700, 500))


class Gamesprite(sprite.Sprite):
    def __init__(self, player_im, player_x, player_y, player_speed, wid, hei):
        super().__init__()
        self.image = transform.scale(image.load(player_im), (wid, hei))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        wind.blit(self.image, (self.rect.x, self.rect.y))

class Player(Gamesprite):
    def update(self):
        keys = key.get_pressed()
        '''if (keys[K_UP] or keys[K_w]) and self.rect.x > 10:
            self.rect.y +=self.speed
        if (keys[K_DOWN] or keys[K_s]) and self.rect.x < 650:
            self.rect.x -=self.speed'''

   

pl_1 = Player('green_line.png', 100, 175, 10, 20, 150)
pl_2 = Player('blue_line.png', 600, 175, 10, 20, 150)



game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    wind.blit(background, (0,0))

    pl_1.update()
    pl_1.reset()
    pl_2.update()
    pl_2.reset()


    display.update()   