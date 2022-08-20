from mpython import *
import math
import time
import music

def tune2list(tune):
    astack=[]
    result=[]
    i=0
    while i<len(tune):
        astack.append(tune[i])
        if astack[-1]=='(':
            astack.pop()
            i=i+1
            while tune[i]!=')':
                result.append(tune[i]+tune[i+1]+':'+astack[0])
                i=i+2
            astack.pop()
        i=i+1
    return result

def charm(origin):
    result=origin.split(',')
    return result

def framw():
    oled.line(4,60,124,60,1)
    for i in range(7):
        oled.line(4+20*i,59,4+20*i,60,1)

class Brick():
    def __init__(self,position,posty=0):
        self.pos=position
        self.posy=posty
    def draw(self):
        oled.line(5+20*self.pos,self.posy,5+18+20*self.pos,self.posy,1)
    def getpos(self):
        return self.pos,self.posy
    def move(self,v):
        self.posy=self.posy+v

class Block():
    def __init__(self):
        self.v=1
        self.bricks=[]
        self.point=0
    def disappear(self):
        i=0
        while i<len(self.bricks):
            x,y=self.bricks[i].getpos()
            if y>63:
                self.bricks.pop(i)
            i=i+1
    def destory(self,pos):
        i=0
        while i<len(self.bricks):
            x,y=self.bricks[i].getpos()
            if x==pos:
                self.bricks.pop(i)
                if y==60:
                    self.point=self.point+2
                elif y in [59,61]:
                    self.point=self.point+1
                break
            i=i+1
    def newbrick(self,charm):
        if charm=='-1':
            pass
        else:
            for i in range(len(charm)):
                self.bricks.append(Brick(int(charm[i])))
    def move(self):
        for brick in self.bricks:
            brick.move(self.v)
    def draw(self):
        for brick in self.bricks:
            brick.draw()
    def score(self):
        oled.DispChar(str(self.point), 0, 0)

def buttn(agame):
    if touchPad_P.read()<100:
        agame.destory(0)
    if touchPad_Y.read()<100:
        agame.destory(1)
    if touchPad_T.read()<100:
        agame.destory(2)
    if touchPad_H.read()<100:
        agame.destory(3)
    if touchPad_O.read()<100:
        agame.destory(4)
    if touchPad_N.read()<100:
        agame.destory(5)
        

def run(tunes,charms,fre=5):
    turn=0
    game=Block()
    oled.fill(0)
    framw()
    game.score()
    oled.show()
    start=False
    while button_a.value()==1:
        pass
    while button_b.value()==1:
        turn=turn%len(tunes)
        #if turn>50//fre or start:
            #music.play(tunes[turn-50//fre])
            #start=True
        game.newbrick(charms[turn])
        for i in range(fre):
            oled.fill(0)
            framw()
            game.disappear()
            game.move()
            buttn(game)
            game.score()
            game.draw()
            oled.show()
        turn=turn+1

acharm=charm("01,-1,-1,-1,01,-1,-1,-1,01,-1,-1,-1,01,-1,-1,-1,12,-1,-1,-1,12,-1,-1,-1,12,-1,-1,-1,12,-1,-1,-1,23,-1,-1,-1,23,-1,-1,-1,23,-1,-1,-1,23,-1,-1,-1,34,-1,-1,-1,05,-1,-1,-1,14,-1,-1,-1,45,-1,-1,-1,13,-1,-1,-1,13,-1,-1,-1,13,-1,-1,-1,5,4,3,1,0,0,3,4,3,2,23,-1,4,34,-1,0,0,5,23,-1,23,-1,0,0,5,23,-1,23,-1,0,0,3,4,3,2,23,-1,4,34,-1,0,0,5,23,-1,23,-1,0,0,5,23,-1,23,-1,34,-1,-1,-1,05,-1,-1,-1,14,-1,-1,-1,45,-1,-1,-1,13,-1,-1,-1,13,-1,-1,-1,13,-1,-1,-1,5,4,3,1,0,0,3,4,3,2,23,-1,4,34,-1,0,0,5,23,-1,23,-1,0,0,5,23,-1,23,-1,0,0,3,4,3,2,23,-1,4,34,-1,0,0,5,23,-1,23,-1,0,0,5,23,-1,23,-1")
atune=tune2list("1(G4G4G4G4)1(G4G4G4G4)1(G4G4G4G4)1(G4G4G4G4)1(B4B4B4B4)1(B4B4B4B4)1(B4B4B4B4)1(B4B4B4B4)1(B4B4B4B4)1(B4B4B4B4)1(B4B4B4B4)1(B4B4B4B4)1(B4B4B4B4)1(D5D5D5D5)1(C5C5C5C5)1(F5F5F5F5)1(G5G5G5G5)1(G5G5G5G5)1(G5G5G5G5)1(C5B4A4F4)2(G4)1(G4D5)2(C5B4)2(A4)1(A4A4)2(D5)1(B4A4)2(G4)1(G4C6)1(A5B5A5B5)2(G4)1(G4B5)1(A5B5A5B5)2(G4)1(G4D5)2(C5B4)2(A4)1(A4A4)2(C5)1(B4A4)2(G4)1(G4C6)1(A5B5A5B5)2(G4)1(G4B5)1(A5B5A5B5)1(B4B4B4B4)1(D5D5D5D5)1(C5C5C5C5)1(F5F5F5F5)1(G5G5G5G5)1(G5G5G5G5)1(G5G5G5G5)1(C5B4A4F4)2(G4)1(G4D5)2(C5B4)2(A4)1(A4A4)2(D5)1(B4A4)2(G4)1(G4C6)1(A5B5A5B5)2(G4)1(G4B5)1(A5B5A5B5)2(G4)1(G4D5)2(C5B4)2(A4)1(A4A4)2(C5)1(B4A4)2(G4)1(G4C6)1(A5B5A5B5)2(G4)1(G4B5)1(A5B5A5B5)")

run(atune,acharm)

