import pygame
import time
import random
pygame.init()

width = 800
height = 600
window = pygame.display.set_mode((564,900))
pygame.display.set_caption("CAPTAIN GAME")

interphase = pygame.display.set_mode((564,900))
bg = [pygame.image.load('homebg0.png'),pygame.image.load('homebg0.png'),pygame.image.load('homebg0.png'),pygame.image.load('homebg0.png'),pygame.image.load('homebg.png'),pygame.image.load('homebg.png'),pygame.image.load('homebg.png'),pygame.image.load('homebg.png'),]
captain = [pygame.image.load('captain.png'),pygame.image.load('captain.png'),pygame.image.load('captain.png'),pygame.image.load('captain.png'),pygame.image.load('captain2.png'),pygame.image.load('captain2.png'),pygame.image.load('captain2.png'),pygame.image.load('captain2.png')]
thing = pygame.image.load('bomb.png')
thing2 = pygame.image.load('cap.png')
thing3 = pygame.image.load('thor.png')
thing4 = pygame.image.load('spider.png')
heart  = [pygame.image.load('3life.png'),pygame.image.load('2life.png'),pygame.image.load('1life.png'),pygame.image.load('0life.png')] 
bgplay = pygame.image.load('bg.png')
bghowto = pygame.image.load('howto.png')

gameover = pygame.display.set_mode((564,900))
over = True
go = pygame.image.load('gameover.png')

how_to_play = pygame.display.set_mode((564,900))
how = True

score = 0
x = 50
y = 700
width_cha = 40
height_cha = 60
vel = 20
inf = True
run = True
# clock = time.clock()
c= 0
v = 0
fall = []
life = 0

class falleiei(object):
    def __init__(self):
        self.d = random.choice([0,1,2,3,1,1,2,1,2,2,2,0,3,3,0])   
        
        self.y = 0
        self.uu = random.choice([50,150,250,350,450])
        self.x = self.uu
    def draw(self,window):
        
        if self.d == 0:
            window.blit(thing,(self.x,self.y))
        if self.d == 1:
            window.blit(thing2,(self.x,self.y))
        if self.d == 2:
            window.blit(thing3,(self.x,self.y))
        if self.d == 3:
            window.blit(thing4,(self.x,self.y))    
        self.move()
    def move(self):
        self.y += 5
        
        
while inf :
    
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inf = False
            run = False
            over = False  
            how = False
            
    # time.clock
    interphase.blit(bg[c%8],(0,0))
    c+=1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        inf = False
        
        pygame.time.delay(100)
    print(c)
    pygame.display.update()
    
       
c = 0
while how:
    how_to_play.blit(bghowto,(0,0))
    c += 1
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            how = False 
            run = False
            over = False  
                    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        how = False  
        pygame.time.delay(100)    
        
    pygame.display.update()
    
    
c=0
while run:
    window.blit(bgplay,(0,0)) 
    c += 1
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            over = False    
            
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 510 - width_cha - vel:
        x += vel
  
    
    window.blit(captain[v%8],(x,y))    
    v+=1
    
    if v < 300:
        if v% 100 == 0 :
            fall.append(falleiei())
        if v > 50:
            for ee in fall:
                ee.draw(window)
    if v > 300:
        if v% 80 == 0 :
            fall.append(falleiei())
    
            
  
    print(score)
    for ee in fall:
        ee.draw(window)
        
        if ee.y > 700 and ee.y < 800 and ee.x > x - 100 and ee.x < x + 100:
            if ee.d == 0:
                life += 1
            if ee.d == 1:
                score += 5
            if ee.d == 2:
                score -=3
            if ee.d == 3:
                score -=2
            fall.remove(ee)
        if ee.y > 1000 :
            fall.remove(ee)
    if life == 3:
        run = False
    window.blit(heart[life],(-10,-10))
    font = pygame.font.SysFont('comicsans',48)
    text = font.render('Score: '+ str(score ),1,(176,48,96))
    window.blit(text,(400,50))
    pygame.display.update()

while over:
    gameover.blit(go,(70,250))
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            over = False            
            
        
        
                
      
        
    
   # pygame.draw.rect(window, (255,0,0),(x,y,width_cha,height_cha))
    pygame.display.update()

pygame.quit()