from pygame import *
from random import *
from time import time as timer

#250,40,80 это идеальный цвет

window = display.set_mode((700,500))
display.set_caption('Шутер')
background = transform.scale(
        image.load('galaxy.jpg'),
        (700,500)
    )

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

fire = mixer.Sound('fire.ogg')

font.init()
font = font.SysFont('Arial', 70)

#font2 = font.SysFont('Arial',20)

win = font.render(
    'YOU WIN', True, (255,215,0)
)

ower = font.render(
    'GAME OWER', True, (255,215,0)
)


lost = 0
chet = 0


class Labamba_a(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_w,player_h,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_w,player_h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(Labamba_a):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_RIGHT] and self.rect.x < 645:
            self.rect.x += self.speed
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
    def fire(self):
        pulka = Pula('bullet.png',self.rect.centerx,self.rect.top,15,20,-15)
        puly.add(pulka)

class Enemy(Labamba_a):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >= 500:
            self.rect.y = 0
            self.rect.x = randint(50,650)
            lost += 1

class Pula(Labamba_a):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()



vragi = sprite.Group()

puly = sprite.Group()

steroidy = sprite.Group()

fafa = Player('rocket.png',500,450,50,50,5)
for v in range(5):
    viva = Enemy('ufo.png',randint(50,650),0,50,50,randint(1,5))
    vragi.add(viva)

finish = False

for j in range(3):
    stero = Enemy('asteroid.png',randint(50,650),0,50,50,randint(2,6))
    steroidy.add(stero)

liver_htfu = 3
num_fire = 0
rel_time = False
FPS = 60
clock = time.Clock()
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                if num_fire < 5 and rel_time == False:
                    fafa.fire()
                    fire.play()
                    num_fire += 1
                if num_fire >= 5 and rel_time == False:
                    rel_time = True
                    lest_time = timer()




    if finish != True:

        window.blit(background,(0,0))
        
        
        fafa.update()
        fafa.reset()
        
        vragi.update()
        vragi.draw(window)

        puly.update()
        puly.draw(window)

        steroidy.update()
        steroidy.draw(window)
        
        if rel_time == True:
            new_time = timer()
            if new_time - lest_time < 3:
                reload1 = font.render(
                    'Перезарядка:', True, (255,215,0)
                )
                window.blit(reload1,(50,150))
            else:
                num_fire = 0
                rel_time = False 

        sprite_list = sprite.groupcollide(
            vragi, puly, True, True
        )
        for g in sprite_list:
            chet += 1
            viva = Enemy('ufo.png',randint(50,650),0,50,50,randint(1,5))
            vragi.add(viva)

        if sprite.spritecollide(fafa,vragi,False) or lost >= 3 or sprite.spritecollide(fafa,steroidy,False):
            finish = True
            window.blit(ower,(200,200))

        if chet >= 10:
            finish = True
            window.blit(win,(200,200))


        text_lose = font.render('Пропущено: '+ str(lost),1,(255,255,255))
        window.blit(text_lose,(50,50))

        text_chee = font.render('Уничтожено: '+ str(chet),1,(255,255,255))
        window.blit(text_chee,(50,100))




    clock.tick(FPS)
    display.update()