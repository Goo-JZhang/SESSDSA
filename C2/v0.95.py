from mpython import *
import audio
import urequests
import json
import machine
import ubinascii
import time
import network
import math
import random

barrage_list = []


#x：0~15为蓝条
#x: 16~127  y: 1~63

class barrage():
    global barrage_list

    def __init__(self, x, y, vx, vy, size=1):
        self.x = x
        self.y = y
        self.rx=round(self.x)
        self.ry=round(self.y)
        #vx,vy: -1,0,1，弹幕每次只能向八个方向中的一个走一步
        self.vx = vx
        self.vy = vy
        self.size=size#0是mini,1是normal,2是large
        self.outranged = False

    def update_next_move(self):
        #更新下一步位置，标记越界情况
        self.x += self.vx
        self.y += self.vy
        self.rx=round(self.x)
        self.ry=round(self.y)
        if self.x < 16 or self.x > 127 or self.y < 0 or self.y > 63:
            self.outranged = True

    def update_oled(self):
        #self.update_next_move()
        if not self.outranged:
            #十字弹幕
            if self.size==0:
                oled.pixel(self.rx, self.ry, 1)
            elif self.size==1:
                oled.pixel(self.rx, self.ry, 1)
                if self.x + 1 <= 127:
                    oled.pixel(self.rx + 1, self.ry, 1)
                if self.x-1 >= 16:
                    oled.pixel(self.rx-1, self.ry, 1)
                if self.y+1 <= 63:
                    oled.pixel(self.rx, self.ry+1, 1)
                if self.y - 1 >= 0:
                    oled.pixel(self.rx, self.ry - 1, 1)
            elif self.size==2:
                #3*3实心方形弹幕
                oled.pixel(self.rx, self.ry, 1)
                if self.x + 1 <= 127:
                    oled.pixel(self.rx + 1, self.ry, 1)
                if self.x-1 >= 16:
                    oled.pixel(self.rx-1, self.ry, 1)
                if self.y+1 <= 63:
                    oled.pixel(self.rx, self.ry+1, 1)
                if self.y - 1 >= 0:
                    oled.pixel(self.rx, self.ry - 1, 1)
                if self.x+1 <= 127 and self.y+1 <= 63:
                    oled.pixel(self.x+1, self.y+1, 1)
                if self.x-1 >= 16 and self.y-1 >= 0:
                    oled.pixel(self.x-1, self.y-1, 1)
                if self.y+1 <= 63 and self.x-1 >= 16:
                    oled.pixel(self.x-1, self.y+1, 1)
                if self.y - 1 >= 0 and self.x+1 <= 127:
                    oled.pixel(self.x + 1, self.y - 1, 1)
        '''else:
            barrage_list.remove(self)'''#这里不需要了，在移动的时候就可以附加，参看update_barrages()


#弹幕类型
def half_circle_barrage(x,y,tag_x,tag_y,size=1,speed=1):#tag为玩家坐标
    global barrage_list
    temp_vec=[tag_x-x,tag_y-y]
    vec_mode=math.sqrt(temp_vec[0]**2+temp_vec[1]**2)
    vel_1=[speed*temp_vec[0]/vec_mode,speed*temp_vec[1]/vec_mode]#正对玩家
    vel_2=[speed*0.707*(vel_1[0]+vel_1[1])/vec_mode,speed*0.707*(vel_1[0]-vel_1[1])/vec_mode]#玩家角度+45^o
    vel_3=[speed*0.707*(vel_1[0]-vel_1[1])/vec_mode,speed*0.707*(vel_1[0]+vel_1[1])/vec_mode]#玩家角度-45^o
    vel_4=[speed*vel_1[1],-speed*vel_1[0]]#玩家角度+90^o
    vel_5=[-speed*vel_1[1],speed*vel_1[0]]#玩家角度-90^o
    barrage_list.append(barrage(x,y,vel_1[0],vel_1[1],size))
    barrage_list.append(barrage(x,y,vel_2[0],vel_2[1],size))
    barrage_list.append(barrage(x,y,vel_3[0],vel_3[1],size))
    barrage_list.append(barrage(x,y,vel_4[0],vel_4[1],size))
    barrage_list.append(barrage(x,y,vel_5[0],vel_5[1],size))

def oth_deg_barrage(x,y,tag_x,tag_y,size=1,speed=1):
    global barrage_list
    temp_vec=[tag_x-x,tag_y-y]
    vec_mode=math.sqrt(temp_vec[0]**2+temp_vec[1]**2)
    vel_1=[speed*temp_vec[0]/vec_mode,speed*temp_vec[1]/vec_mode]#正对玩家
    vel_2=[speed*0.707*(vel_1[0]+vel_1[1])/vec_mode,speed*0.707*(vel_1[0]-vel_1[1])/vec_mode]#玩家角度+45^o
    vel_3=[speed*0.707*(vel_1[0]-vel_1[1])/vec_mode,speed*0.707*(vel_1[0]+vel_1[1])/vec_mode]#玩家角度-45^o
    barrage_list.append(barrage(x,y,vel_1[0],vel_1[1],size))
    barrage_list.append(barrage(x,y,vel_2[0],vel_2[1],size))
    barrage_list.append(barrage(x,y,vel_3[0],vel_3[1],size))

def wh_circle_barrage(x,y,tag_x,tag_y,size=1,speed=1):
    global barrage_list
    half_circle_barrage(x,y,tag_x,tag_y,size,speed,size)
    half_circle_barrage(x,y,2*x-tag_x,2*y-tag_y,size,speed,size)

def shoot_barrage(x,y,tag_x,tag_y,size=1,speed=1):
    global barrage_list
    temp_vec=[tag_x-x,tag_y-y]
    vec_mode=math.sqrt(temp_vec[0]**2+temp_vec[1]**2)
    vel_1=[speed*temp_vec[0]/vec_mode,speed*temp_vec[1]/vec_mode]#正对玩家
    barrage_list.append(barrage(x,y,vel_1[0],vel_1[1],size))

def cross_barrage(x,y,size=1,speed=1):
    global barrage_list
    barrage_list.append(barrage(x,y,speed,0,size))
    barrage_list.append(barrage(x,y,-speed,0,size))
    barrage_list.append(barrage(x,y,0,speed,size))
    barrage_list.append(barrage(x,y,0,-speed,size))

def op_ang_barrage(x,y,size=1,speed=1):
    global barrage_list
    barrage_list.append(barrage(x,y,0.707*speed,0.707*speed,size))
    barrage_list.append(barrage(x,y,-0.707*speed,0.707*speed,size))
    barrage_list.append(barrage(x,y,0.707*speed,-0.707*speed,size))
    barrage_list.append(barrage(x,y,-0.707*speed,-0.707*speed,size))

def full_ang_barrage(x,y.size=1,speed=1):
    global barrage_list
    cross_barrage(x,y,speed,size)
    op_ang_barrage(x,y,speed,size)
#弹幕类型结束
'''
弹幕类型：
半圆波，会瞄准玩家,0
直角散射波，会瞄准玩家,1
全圆波，会瞄准玩家,2
狙击弹，会瞄准玩家,3
十字波,4
对角波,5
圆波,6
'''

#越界检查和更新

def checkNpop(num):
    global barrage_list
    if barrage_list[num].outranged:
        barrage_list.pop[num]
        return True
    else:
        return False
def update_barrages():
    global barrage_list
    i=0
    while i<len(barrage_list):
        barrage_list[i].update_next_move()
        if checkNpop(i):
            pass
        else:#不越界就说明存在，存在就画
            barrage_list[i].update_oled()
            i=i+1

#越界检查和更新结束

#种子预备

def threshold(difficulty):
    if difficulty=="Easy":
        return 2
    elif difficulty=="Normal":
        return 4
    else:
        return 6

'''
给定一个地图种子生成一个list,格式为[[[barragetype,x,y,size,speed],[...],[...]],[...],...]，list[i]的长度为该步骤的弹幕源数目
地图种子为一个长为10，全部由0-9的数字组成的str
只做90步，因为最后的时间生成弹幕没有意义
'''
def seed2seed(aseed):
    aseed=str(int(aseed)**2-1)[0:10]
    aseed[0]=str((int(aseed[0])+2*int(aseed[3])+3*int(aseed[6]))%10)
    aseed[1]=str((int(aseed[1])+2*int(aseed[4])+3*int(aseed[7]))%10)
    aseed[2]=str((int(aseed[2])+2*int(aseed[5])+3*int(aseed[8]))%10)
    aseed[3]=str((int(aseed[3])+2*int(aseed[6])+3*int(aseed[9]))%10)
    aseed[4]=str((int(aseed[4])+2*int(aseed[7])+3*int(aseed[0]))%10)
    aseed[5]=str((int(aseed[5])+2*int(aseed[8])+3*int(aseed[1]))%10)
    aseed[6]=str((int(aseed[6])+2*int(aseed[9])+3*int(aseed[2]))%10)
    aseed[7]=str((int(aseed[7])+2*int(aseed[0])+3*int(aseed[3]))%10)
    aseed[8]=str((int(aseed[8])+2*int(aseed[1])+3*int(aseed[4]))%10)
    aseed[9]=str((int(aseed[9])+2*int(aseed[2])+3*int(aseed[5]))%10)
    return aseed

def num2speed(num):
    if num==0:
        return 0.5
    elif num in [1,2]:
        return 0.7
    elif num in [3,5]:
        return 0.9
    else:
        return 1

def seed2list(aseed,difficulty="Normal"):
    result=[]
    for i in range(90):
        temp=[]
        fre=threashold(difficulty)
        mua=random.randint(0,9)
        if mua in range(fre+1):
            num=int(aseed[0]%3)+1#弹幕源数目
            for i in range(num):
                cord_x=16+int(aseed[1:3])%48
                cord_y=1+int(aseed[3:6])%62
                size=int(aseed[6])%3
                speed=num2speed(int(aseed[7])%10)
                btype=int(aseed[7:10])%7
                temp.append([btype,cord_x,cord_y,size,speed])
                aseed=seed2seed(aseed)
        else:
            temp=[[]]
        result.append(temp)
    return result


def generate_barrages(result,player):
    global barstep
    if round(get_time())>step:#时间跳跃之后才有弹幕
        barstep=round(get_time())#立刻更新step免得爆炸，理论上是一秒一弹幕
        astep=result.pop()
        for bar in astep:
            if len(bar)==0:
                pass#该步骤没有弹幕生成
            else:#bar=[barragetype,x,y,size,speed] or []
                if bar[0]==0:
                    half_circle_barrage(bar[1],bar[2],player.x,player.y,bar[3],bar[4])
                elif bar[0]==1:
                    oth_deg_barrage(bar[1],bar[2],player.x,player.y,bar[3],bar[4])
                elif bar[0]==2:
                    wh_circle_barrage(bar[1],bar[2],player.x,player.y,bar[3],bar[4])
                elif bar[0]==3:
                    shoot_barrage(bar[1],bar[2],player.x,player.y,bar[3],bar[4])
                elif bar[0]==4:
                    cross_barrage(bar[1],bar[2],bar[3],bar[4])
                elif bar[0]==5:
                    op_ang_barrage(bar[1],bar[2],bar[3],bar[4])
                else:
                    full_ang_barrage(bar[1],bar[2],bar[3],bar[4])

#种子结束，弹幕生成结束

"""def generate_waves():
    global f1, f2, f3
    if get_time() is 3 and f1:
        generate_barrages(30, 30)  # 后续完善
        f1 = 0
    if get_time() is 6 and f2:
        generate_barrages(90, 32, True)
        generate_barrages(30, 30)
        f2 = 0
    if get_time() is 9 and f3:
        generate_barrages(72, 48)
        generate_barrages(90, 32, True)
        generate_barrages(30, 30)
        f3 = 0"""


def draw_heart(x, y, filled=False):
    oled.pixel(x + 1, y, 1)
    oled.pixel(x + 3, y, 1)
    oled.pixel(x, y + 1, 1)
    oled.pixel(x + 2, y + 1, 1)
    oled.pixel(x + 4, y + 1, 1)
    oled.pixel(x, y + 2, 1)
    oled.pixel(x + 4, y + 2, 1)
    oled.pixel(x + 1, y + 3, 1)
    oled.pixel(x + 3, y + 3, 1)
    oled.pixel(x + 2, y + 4, 1)
    if filled is True:
        oled.pixel(x + 1, y + 1, 1)
        oled.pixel(x + 3, y + 1, 1)
        oled.pixel(x + 1, y + 2, 1)
        oled.pixel(x + 2, y + 2, 1)
        oled.pixel(x + 3, y + 2, 1)
        oled.pixel(x + 2, y + 3, 1)


class player():
    global barrage_list

    def __init__(self, x, y, hp=4, mp=0):
        self.x = x
        self.y = y
        self.hp = hp
        self.mp = mp
        self.score = 0
        self.aura = False
        self.aura_radius = 0
        self.aura_skill_type = 0

    def move(self):  # 通过按键实现四个方向移动
        #p左y右o上n下
        if touchPad_P.read() < 100 and self.x > 16:
            self.x -= 1
        if touchPad_Y.read() < 100 and self.x < 127:
            self.x += 1
        if touchPad_O.read() < 100 and self.y > 0:
            self.y -= 1
        if touchPad_N.read() < 100 and self.y < 63:
            self.y += 1

    def update_hp(self):
        #检查碰撞并扣血
        for bar in barrage_list:
            if bar.size==0:
                if self.x==bar.rx and self.y==bar.ry:
                    self.hp=self.hp-0.5
                    barrage_list.remove(bar)
            elif bar.size==1:
                if self.x==bar.rx:
                    if self.y in [bar,ry-1.bar.ry+1,bar.ry]:
                        self.hp=self.hp-1
                        barrage_list.remove(bar)
                elif self.y==bar.ry:
                    if self.x in [bar.rx-1,bar.rx,bar.rx+1]:
                        self.hp=self.hp-1
                        barrage_list.remove(bar)
            elif bar.size==3:
                elif self.x in [bar.rx-1,bar.rx,bar.rx+1]:
                    if self.y in [bar.ry-1,bar.ry,bar.ry+1]:
                        self.hp=self.hp-1.5
                        barrage_list.remove(bar)

    def update_mp(self):  # 攒够蓝可语音开大？
        global mp_time
        delta = get_time() - mp_time
        mp_time = get_time()
        self.mp += 100*delta  # 每秒回蓝速度100
        if self.mp >= 501:  # 蓝量上限
            self.mp = 501

    def update_score(self):
        self.score = round(get_time())  # 一秒一分

    def update_oled(self):
        oled.pixel(self.x, self.y, 0)
        oled.pixel(self.x+1, self.y, 1)
        oled.pixel(self.x-1, self.y, 1)
        oled.pixel(self.x, self.y+1, 1)
        oled.pixel(self.x, self.y-1, 1)  # frame of player

    def update_hp_bar(self):
        if self.hp >= 0.5:
            draw_heart(1, 15, False)
        if self.hp >= 1:
            draw_heart(1, 15, True)
        if self.hp >= 1.5:
            draw_heart(7, 15, False)
        if self.hp >= 2:
            draw_heart(7, 15, True)
        if self.hp >= 2.5:
            draw_heart(1, 21, False)
        if self.hp >= 3:
            draw_heart(1, 21, True)
        if self.hp >= 3.5:
            draw_heart(7, 21, False)
        if self.hp >= 4:
            draw_heart(7, 21, True)

    def update_mp_bar(self):
        if self.mp >= 100:
            oled.fill_rect(1, 56, 11, 6, 1)
        if self.mp >= 200:
            oled.fill_rect(1, 49, 11, 6, 1)
        if self.mp >= 300:
            oled.fill_rect(1, 42, 11, 6, 1)
        if self.mp >= 400:
            oled.fill_rect(1, 35, 11, 6, 1)
        if self.mp >= 500:
            oled.fill_rect(1, 28, 11, 6, 1)

    def aura_skill(self):
        if self.aura is True:
            self.aura_radius += 1
            oled.circle(self.x, self.y, self.aura_radius, 1)
            for bar in barrage_list:
                if (bar.x - self.x) ** 2 + (bar.y - self.y) ** 2 <= self.aura_radius ** 2:
                    barrage_list.remove(bar)
            if self.aura_radius is 6*self.aura_skill_type:
                self.aura = False
                self.aura_radius = 0
                self.aura_skill_type = 0


def update_data_bar(p):
    oled.line(15, 0, 15, 63, 1)  # 画线
    oled.DispChar(str(p.score), 0, 0, 1)  # 0~7分数
    p.update_hp_bar()
    p.update_mp_bar()


def skill_trigger(p, skill_type):
    p.mp -= (200+100*skill_type)
    p.aura = True
    p.aura_skill_type = skill_type


def player_ui(p,result):
    global barrage_list
    oled.fill(0)
    generate_barrages(result,p)
    for bar in barrage_list:  # 弹幕更新一步
        update_barrages()
    p.move()  # 玩家移动，是否要加条件？
    p.update_hp()
    p.update_mp()
    p.update_score()
    p.aura_skill()
    p.update_oled()  # 玩家更新
    update_data_bar(p)
    #time.sleep(???) #要不要控制帧率
    oled.show()


def get_time():
    global t0
    return time.time()-t0


def ZPW(result):
    global t0
    global barrage_list
    global mp_time
    mp_time = 0
    barrage_list.clear()
    t0 = int(time.time())  # 计时零点
    barstep=0
    p = player(72, 32)  # 玩家初始放哪？
    #global f1, f2, f3
    #f1, f2, f3 = 1, 1, 1
    while p.hp > 0:
        #generate_waves()
        player_ui(p,result)
        if not button_a.value():
            show_game()  # 在游戏中按a键可返回开始界面，进度不会保存
        if p.score >= 100:
            show_win()
        if sound.read() > 1500 and p.mp >= 500:
            skill_trigger(p, 3)
        if sound.read() > 1000 and p.mp >= 400:
            skill_trigger(p, 2)
        if sound.read() > 500 and p.mp >= 300:
            skill_trigger(p, 1)
        '''
        if p.mp >= 400:
            if not button_b.value():
                sound_input = speech_recognition()
                oled.DispChar(str(sound_input), 0, 0, 1)
                oled.show()
                '''
        #if '西红柿' in speech_recognition():

    if p.hp <= 0:
        show_death()


def show_win():
    oled.fill(0)
    oled.DispChar('You Win!', 0, 0, 1)
    oled.DispChar('按a键重新开始', 0, 16, 1)
    oled.show()
    while button_a.value():
        pass
    show_game()


def show_death():
    oled.fill(0)
    oled.DispChar('GG！', 0, 0, 1)
    oled.DispChar('按a键重新开始', 0, 16, 1)
    oled.show()
    while button_a.value():
        pass
    show_game()


def countdown(t):
    #倒计时界面
    while t >= 0:
        if t == 0:
            oled.fill(0)
            oled.DispChar('开始', 54, 26, 1)
            oled.show()
            time.sleep(1)
            break
        oled.fill(0)
        oled.circle(64, 32, 9, 1)
        oled.DispChar(str(t), 62, 24, 1)
        oled.show()
        time.sleep(1)
        t -= 1

def writeDifficulty():
    oled.DispChar('Easy',48,8,1)
    oled.DispChar('Normal',32,28,1)
    oled.DispChar('Hard',48,48)

def writeChoice(choice):
    if choice==0:
        oled.fill_triangle(46,12,40,8,40,16,1)
    elif choice==1:
        oled.fill_triangle(30,32,24,28,24,36,1)
    elif choice==3:
        oled.fill_triangle(46,52,40,48,40,56,1)
    oled.show()


def choose():
    oled.fill(0)
    oled.DispChar('按P/Y键进行左/右移动',0,0,1)
    oled.DispChar('按O/N键进行上/下移动',0,16,1)
    oled.DispChar('按a键确定难度'0,32,1)
    oled.DispChar('>>>按a继续',0,48,1)
    oled.show()
    while button_a.value():
        pass
    choice=1
    oled.fill(0)
    while not button_a.value():
        if touchPad_O<100:
            choice=(choice+1)%3
        if touchPad_N<100:
            choice=(choice+2)%3
        writeDifficulty()
        writeChoice(choice)
    return choice


def show_game():
    oled.fill(0)
    oled.DispChar('欢迎来到嘴炮王！', 0, 0, 1)
    oled.DispChar('按a键以开始游戏', 0, 16, 1)
    oled.show()
    while button_a.value():
        pass
    choice=choose()
    if choice==0:
        difficulty="Easy"
    elif chioce==1:
        difficulty="Normal"
    else:
        difficulty="Hard"
    seed=str(random.randint(1000000000,9999999999))
    result=seed2list(seed,difficulty)
    countdown(3)
    ZPW(result)


if __name__ == '__main__':
    #my_wifi = wifi()
    #my_wifi.connectWiFi('HONOR V20', '12345687')
    #if my_wifi.sta.isconnected():
    #    rgb[2] = (0, 255, 0)
    #    rgb.write()
    #else:
    #    rgb[2] = (255, 0, 0)
    #    rgb.write()
    show_game()


'''
弹幕生成器（t的函数）Z
难度机制 难度选择界面 Z

速度机制 Z

获胜界面 L pass

语音复刻、声音大小 L pass
开大清理周围弹幕的机制 L pass

技术报告 Z
视频 L
'''
