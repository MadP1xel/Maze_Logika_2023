from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, width, height, player_speed):
        self.image = transform.scale(image.load(player_image),(width,height))
        self.speed = player_speed

        self.rect =self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))



class Player(GameSprite):

    def update(self):
        keys = key.get_pressed()

        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed



class Monster(GameSprite):
    direction = "left"
    def update(self):

        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= win_width- 85:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


class Wall(sprite.Sprite):
    def __init__(self,color1,color2,color3,wall_x,wall_y,wall_width,wall_height):
        super().__init__()
        self.image = Surface((wall_width,wall_height))
        self.image.fill((color1,color2,color3))

        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y


    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))




win_width = 800
win_height= 600
window = display.set_mode((win_width,win_height))

background = transform.scale(image.load("background.jpg"),(win_width,win_height))

game = True
clock = time.Clock()
FPS = 60


#Блок отвецяющий за музыку
mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()



player = Player("hero.png",5, win_height-80,60,60, 4)
monster = Monster("cyborg.png",win_width-120,280,60,60, 4)
gold = GameSprite("treasure.png", win_width-120, win_height-80, 50,50,0)



w1 = Wall(255, 255, 255, 100, 20, 450, 10)
w2 = Wall(255, 255,255, 100, 580, 350, 10)
w3 = Wall(255, 255,255, 100, 20, 20, 380)
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background,(0,0))
    player.update()
    player.reset()

    monster.update()
    monster.reset()
    gold.reset()
    w1.reset()
    w2.reset()
    w3.reset()



    display.update()
    clock.tick(FPS)