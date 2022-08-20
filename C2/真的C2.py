from mpython import *
import random
class Bullet():
    def __init__(self,pos,vel):
        self.posx=pos[0]
        self.posy=pos[1]
        self.rx=round(self.posx)
        self.ry=round(self.posy)
        self.v=vel
    def draw(self):
        oled.line(self.rx,self.ry,self.rx,self.ry,1)
    def getX(self):
        return self.rx
    def getY(self):
        return self.ry
    def move(self):
        self.posx=self.posx+self.v
        self.rx=round(self.posx)
    
class player():
    def __init__(self):
        self.v=0.8
        self.top=[1,0]
        self.right=[0,1]
        self.left=[0,-1]
        self.posx=8
        self.posy=32
        self.rx=8
        self.ry=32
        self.bullets=[]
        self.health=10
        self.bv=1#子弹速度
    def emit(self):
        self.bullets.append(Bullet([self.posx+self.top[0],self.posy+self.top[1]],self.bv))
    def draw(self):
        oled.line(self.rx,self.ry,self.rx+self.top[0],self.ry+self.top[1],1)
        oled.line(self.rx,self.ry+self.right[1],self.rx,self.ry+self.left[1],1)
        for bullet in self.bullets:
            bullet.draw()
    def hurt(self,abullet):#受伤判定
        if abullet.ry==self.ry:
            if abullet.rx in [self.rx+self.top[0],self.rx]:
                self.health=self.health-1
        if abullet.ry in [self.ry+self.right[1],self.ry+self.left[1]]:
            if abullet.rx==self.rx:
                self.health=self.health-1
    def move(self,direction):
        if direction=="front":
            if self.pos[0]+self.v<=128:
                self.pos[0]=self.pos[0]+self.v
        elif direction=="back":
            if self.pos[0]-self.v>=0:
                self.pos[0]=self.pos[0]-self.v
        elif direction=="left":
            if self.pos[1]+self.left[1]>=0:
                self.pos[1]=self.pos[1]+self.left[1]
        elif direction=="right":
            if self.pos[1]+self.right[1]<=64:
                self.pos[1]=self.pos[1]+self.right[1]
    
class Enemy():
    def __init__(self,pos,heal):
        self.v=-0.8
        self.top=[-1,0]
        self.right=[0,1]
        self.left=[0,-1]
        self.pos=pos
        self.bullets=[]
        self.health=heal
        self.bv=-1
    def emit(self):
        t=random.randint(0,10)
        if t <3:
            self.bullets.append(Bullet([self.pos[0]+self.top[0],self.pos[1]+self.top[1]],self.ev))
    def draw(self):
        oled.line(self.pos[0],self.pos[1],self.pos[0]+self.top[0],self.pos[1]+self.top[1],1)
        oled.line(self.pos[0],self.pos[1]+self.right[1],self.pos[0],self.pos[1]+self.left[1],1)
        for bullet in self.bullets:
            bulle.draw()
    def hurt(self,pos):
        if pos in [self.pos,[self.pos[0]+self.top[0],self.pos[1]+self.top[1]],[self.pos[0]+self.right[0],self.pos[1]+self.right[1]], \\
        [self.pos[0]+self.left[0],self.pos[1]+self.left[1]]:
            self.health=health-1
            return 1
        else:
            return 0
    def getDirection(self):
        t=random.randint(0,7):
            if t in [0,1]:
                return "front"
            elif t in [2,3]:
                return "left"
            elif t in [4,5]:
                return "right"
            else:
                return "back"
    def move(self,direction):
        if self.pos[0]-self.v>=0:
            self.pos[0]=self.pos[0]+self.v
        if direction=="front":
            if self.pos[0]-self.v>=0:
                self.pos[0]=self.pos[0]+self.v
        elif direction=="back":
            if self.pos[0]+self.v<=128:
                self.pos[0]=self.pos[0]-self.v
        elif direction=="left":
            if self.pos[1]+self.left[1]>=0:
                self.pos[1]=self.pos[1]-self.v
        elif direction=="right":
            if self.pos[1]+self.right[1]<=64:
                self.pos[1]=self.pos[1]+self.v
                
