
from pygame import *
from random import randint







window = display.set_mode((700, 500))

game = True
mixer.init()
mixer.music.load('butyrka-taet-sneg.ogg')
mixer.music.play()
background = transform.scale(image.load('background.jpg'), (700, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, image1, speed, rect_x, rect_y):
        super().__init__()
        self.image = transform.scale(image.load(image1), (42, 42))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0: 
            self.kill()

class Enemy(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randint(80,420)
            lost = lost + 1

font.init()           
lost = 0
font1 = font.Font(None, 36)
font2 = font.Font(None, 36)

monsters = sprite.Group()
bullets = sprite.Group()
for i in range(1,6):
    monster = Enemy('ufo.png', randint(1,5), randint(0,400),30)
    monsters.add(monster)

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 700 - 80:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet("bullet.png", 10, self.rect.centerx, self.rect.top)
        bullets.add(bullet)


      
player = Player("rocket.png", 20, 100, 400)

while game:
    window.blit(background,(0,0))
    clock = time.Clock()
    FPS = 60
    clock.tick(FPS)

    

    
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()
            
  
    text_lose = font1.render('пропущена:' + str(lost),1,(255,255,255))
    window.blit(text_lose,(2,2))
    text_lose1 = font2.render('проиграл' + str(lost),1,(255,255,255))
    window.blit(text_lose,(2,2))
    player.update()
    monsters.update()
    monsters.draw(window)
    player.reset()
    bullets.draw(window)
    bullets.update()
    
    display.update()
    

        

            
        








