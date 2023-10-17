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
    def move_2(self):
        keys = key.get_pressed()
        if keys[K_UP]  and self.rect.y > 10:
            self.rect.y -=self.speed
        if keys[K_DOWN] and self.rect.y < 340:
            self.rect.y +=self.speed

    def move_1(self):
        keys = key.get_pressed()
        if  keys[K_w] and self.rect.y > 10:
            self.rect.y -=self.speed
        if  keys[K_s] and self.rect.y < 340:
            self.rect.y +=self.speed

class Ball(Gamesprite):
    sp_x = 3
    sp_y = 3
    def update(self):
           
        self.rect.x += sp_x
        self.rect.y += sp_y
        if sprite.collide_rect(pl_1, self) or sprite.collide_rect(pl_2, self):
            sp_x *= -1
        if self.rect.y <= 0 or self.rect.y >= 450:
            sp_y *= -1



pl_1 = Player('green_line.png', 100, 175, 10, 20, 150)
pl_2 = Player('blue_line.png', 600, 175, 10, 20, 150)

ball = Ball('ten_ball_1.png', 300, 175, 4, 50, 50)

font.init()
font1 = font.Font(None, 35)
lose = font1.render('YOU LOSE', True, (180, 0, 0))


game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if !=finish:
        wind.blit(background, (0,0))

        pl_1.move_1()
        pl_1.reset()
        pl_2.move_2()
        pl_2.reset()
        
        ball.update()
        ball.reset()

    if ball.rect.x > 700 :
        finish = True
        wind.blit(lose, (200, 200))


    display.update()   
