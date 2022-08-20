
from mpython import *
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
        self.rx = round(self.x)
        self.ry = round(self.y)
        self.vx = vx
        self.vy = vy
        self.size = size  # 0是mini,1是normal,2是large
        self.outranged = False  # 标记越界

    def update_next_move(self):
        #更新下一步位置，标记越界情况
        self.x += self.vx
        self.y += self.vy
        self.rx = round(self.x)
        self.ry = round(self.y)
        if self.x < 16 or self.x > 127 or self.y < 0 or self.y > 63:
            self.outranged = True

    def update_oled(self):
        if not self.outranged:
            if self.size == 0:
                oled.pixel(self.rx, self.ry, 1)
            elif self.size == 1:
                oled.pixel(self.rx, self.ry, 1)
                if self.x + 1 <= 127:
                    oled.pixel(self.rx + 1, self.ry, 1)
                if self.x-1 >= 16:
                    oled.pixel(self.rx-1, self.ry, 1)
                if self.y+1 <= 63:
                    oled.pixel(self.rx, self.ry+1, 1)
                if self.y - 1 >= 0:
                    oled.pixel(self.rx, self.ry - 1, 1)
            elif self.size == 2:
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
                    oled.pixel(self.rx+1, self.ry+1, 1)
                if self.x-1 >= 16 and self.y-1 >= 0:
                    oled.pixel(self.rx-1, self.ry-1, 1)
                if self.y+1 <= 63 and self.x-1 >= 16:
                    oled.pixel(self.rx-1, self.ry+1, 1)
                if self.y - 1 >= 0 and self.x+1 <= 127:
                    oled.pixel(self.rx + 1, self.ry - 1, 1)

#弹幕类型


def half_circle_barrage(x, y, tag_x, tag_y, size=1, speed=1):  # tag为玩家坐标
    global barrage_list
    temp_vec = [tag_x-x, tag_y-y]
    vec_mode = math.sqrt(temp_vec[0]**2+temp_vec[1]**2)
    vel_1 = [speed*temp_vec[0]/vec_mode, speed*temp_vec[1]/vec_mode]  # 正对玩家
    vel_2 = [speed*0.707*(vel_1[0]+vel_1[1]),
             speed*0.707*(vel_1[0]-vel_1[1])]  # 玩家角度+45^o
    vel_3 = [speed*0.707*(vel_1[0]-vel_1[1]),
             speed*0.707*(vel_1[0]+vel_1[1])]  # 玩家角度-45^o
    vel_4 = [speed*vel_1[1], -speed*vel_1[0]]  # 玩家角度+90^o
    vel_5 = [-speed*vel_1[1], speed*vel_1[0]]  # 玩家角度-90^o
    barrage_list.append(barrage(x, y, vel_1[0], vel_1[1], size))
    barrage_list.append(barrage(x, y, vel_2[0], vel_2[1], size))
    barrage_list.append(barrage(x, y, vel_3[0], vel_3[1], size))
    barrage_list.append(barrage(x, y, vel_4[0], vel_4[1], size))
    barrage_list.append(barrage(x, y, vel_5[0], vel_5[1], size))


def oth_deg_barrage(x, y, tag_x, tag_y, size=1, speed=1):
    global barrage_list
    temp_vec = [tag_x-x, tag_y-y]
    vec_mode = math.sqrt(temp_vec[0]**2+temp_vec[1]**2)
    vel_1 = [speed*temp_vec[0]/vec_mode, speed*temp_vec[1]/vec_mode]  # 正对玩家
    vel_2 = [speed*0.707*(vel_1[0]+vel_1[1]),
             speed*0.707*(vel_1[0]-vel_1[1])]  # 玩家角度+45^o
    vel_3 = [speed*0.707*(vel_1[0]-vel_1[1]),
             speed*0.707*(vel_1[0]+vel_1[1])]  # 玩家角度-45^o
    barrage_list.append(barrage(x, y, vel_1[0], vel_1[1], size))
    barrage_list.append(barrage(x, y, vel_2[0], vel_2[1], size))
    barrage_list.append(barrage(x, y, vel_3[0], vel_3[1], size))


def wh_circle_barrage(x, y, tag_x, tag_y, size=1, speed=1):
    global barrage_list
    half_circle_barrage(x, y, tag_x, tag_y, size, speed)
    half_circle_barrage(x, y, 2*x-tag_x, 2*y-tag_y, size, speed)


def shoot_barrage(x, y, tag_x, tag_y, size=1, speed=1):
    global barrage_list
    temp_vec = [tag_x-x, tag_y-y]
    vec_mode = math.sqrt(temp_vec[0]**2+temp_vec[1]**2)
    vel_1 = [speed*temp_vec[0]/vec_mode, speed*temp_vec[1]/vec_mode]  # 正对玩家
    barrage_list.append(barrage(x, y, vel_1[0], vel_1[1], size))


def cross_barrage(x, y, size=1, speed=1):
    global barrage_list
    barrage_list.append(barrage(x, y, speed, 0, size))
    barrage_list.append(barrage(x, y, -speed, 0, size))
    barrage_list.append(barrage(x, y, 0, speed, size))
    barrage_list.append(barrage(x, y, 0, -speed, size))


def op_ang_barrage(x, y, size=1, speed=1):
    global barrage_list
    barrage_list.append(barrage(x, y, 0.707*speed, 0.707*speed, size))
    barrage_list.append(barrage(x, y, -0.707*speed, 0.707*speed, size))
    barrage_list.append(barrage(x, y, 0.707*speed, -0.707*speed, size))
    barrage_list.append(barrage(x, y, -0.707*speed, -0.707*speed, size))


def full_ang_barrage(x, y, size=1, speed=1):
    global barrage_list
    cross_barrage(x, y, speed, size)
    op_ang_barrage(x, y, speed, size)


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


def check_and_pop(index):
    global barrage_list
    if barrage_list[index].outranged:
        barrage_list.pop(index)
        return True
    else:
        return False


def update_barrages():
    global barrage_list
    index = 0
    print(len(barrage_list))
    while index < len(barrage_list):
        barrage_list[index].update_next_move()
        if check_and_pop(index):
            pass
        else:  # 不越界就说明存在，存在就画
            barrage_list[index].update_oled()
            index += 1

#越界检查和更新结束


#种子预备

def threshold(difficulty):
    if difficulty is "Easy":
        return 4
    elif difficulty is "Normal":
        return 6
    else:  # Hard
        return 8


'''
给定一个地图种子返回一个弹幕源
地图种子为一个长为11，全部由0-9的数字组成的list
'''


def seed_to_speed(num):
    if num == 0:
        return 1
    elif num in [1, 2]:
        return 3
    elif num in [3, 5]:
        return 1.5
    else:
        return 2


def seed_to_list(aseed, difficulty="Normal"):
    temp = []
    fre = threshold(difficulty)
    mua = random.randint(0, 9)
    if mua in range(fre+1):
        num = int(aseed[0]) % 3+1  # 弹幕源数目
        for i in range(num):
            cord_x = 16+(10*aseed[1]+aseed[2]) % 48
            cord_y = 1+(100*aseed[3]+10*aseed[4]+aseed[5]) % 62
            size = int(aseed[6]) % 3
            speed = seed_to_speed(int(aseed[7]) % 10)
            btype = int(100*aseed[8]+10*aseed[9]+aseed[10]) % 7
            temp.append([btype, cord_x, cord_y, size, speed])
    else:
        temp = [[]]
    return temp


def generate_barrages(astep, player):
    for bar in astep:
        if len(bar) == 0:
            pass  # 该步骤没有弹幕生成
        else:  # bar=[barragetype,x,y,size,speed] or []
            if bar[0] == 0:
                half_circle_barrage(
                    bar[1], bar[2], player.x, player.y, bar[3], bar[4])
            elif bar[0] == 1:
                oth_deg_barrage(bar[1], bar[2], player.x,
                                player.y, bar[3], bar[4])
            elif bar[0] == 2:
                wh_circle_barrage(
                    bar[1], bar[2], player.x, player.y, bar[3], bar[4])
            elif bar[0] == 3:
                shoot_barrage(bar[1], bar[2], player.x,
                              player.y, bar[3], bar[4])
            elif bar[0] == 4:
                cross_barrage(bar[1], bar[2], bar[3], bar[4])
            elif bar[0] == 5:
                op_ang_barrage(bar[1], bar[2], bar[3], bar[4])
            else:
                full_ang_barrage(bar[1], bar[2], bar[3], bar[4])


#种子结束，弹幕生成结束

#玩家属性模块


class player():
    global barrage_list

    def __init__(self, x, y, hp=4, mp=0):
        self.x = x
        self.y = y
        self.hp = hp
        self.mp = mp
        self.score = 0
        self.aura = False  # 技能开启属性
        self.aura_radius = 0
        self.aura_skill_type = 0

    def move(self):  # 通过按键实现四个方向移动
        #p左y右o上n下
        if touchPad_P.read() < 400 and self.x > 16:
            self.x -= 1
        if touchPad_Y.read() < 400 and self.x < 127:
            self.x += 1
        if touchPad_O.read() < 400 and self.y > 0:
            self.y -= 1
        if touchPad_N.read() < 400 and self.y < 63:
            self.y += 1

    def update_hp(self):
        #检查碰撞并扣血
        for bar in barrage_list:
            if bar.size == 0:
                if bar.rx in [self.x - 2, self.x - 1, self.x, self.x + 1, self.x + 2] and bar.ry in [self.y - 2, self.y - 1, self.y, self.y + 1, self.y + 2]:
                    self.hp = self.hp-0.5
                    barrage_list.remove(bar)
            elif bar.size == 1:
                for (x, y) in [(bar.rx, bar.ry), (bar.rx - 1, bar.ry), (bar.rx, bar.ry - 1), (bar.rx + 1, bar.ry), (bar.rx, bar.ry + 1)]:
                    if x in [self.x - 2, self.x - 1, self.x, self.x + 1, self.x + 2] and y in [self.y - 2, self.y - 1, self.y, self.y + 1, self.y + 2]:
                        self.hp = self.hp - 0.75
                        barrage_list.remove(bar)
                        break
            elif bar.size == 2:
                for (x, y) in [(bar.rx, bar.ry), (bar.rx - 1, bar.ry), (bar.rx, bar.ry - 1), (bar.rx + 1, bar.ry), (bar.rx, bar.ry + 1), (bar.rx+1, bar.ry + 1), (bar.rx-1, bar.ry + 1), (bar.rx-1, bar.ry - 1), (bar.rx+1, bar.ry - 1)]:
                    if x in [self.x - 2, self.x - 1, self.x, self.x + 1, self.x + 2] and y in [self.y - 2, self.y - 1, self.y, self.y + 1, self.y + 2]:
                        self.hp = self.hp - 1
                        barrage_list.remove(bar)
                        break

    def update_mp(self):  # 攒够蓝可语音开大
        global mp_time
        delta = get_time() - mp_time
        mp_time = get_time()
        self.mp += 50*delta  # 每秒回蓝速度50
        if self.mp >= 501:  # 蓝量上限
            self.mp = 501

    def update_score(self):
        self.score = round(get_time())  # 一秒一分

    def update_oled(self):
        for x in [self.x - 2, self.x - 1, self.x, self.x + 1, self.x + 2]:
            for y in [self.y - 2, self.y - 1, self.y, self.y + 1, self.y + 2]:
                oled.pixel(x, y, 1)
        oled.pixel(self.x, self.y, 0)

    def update_hp_bar(self):  # 显示血量，实心2血，空心1血
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

    def update_mp_bar(self):  # 显示蓝量，100蓝一格
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

    def aura_skill(self):  # 检查技能开启
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


def draw_heart(x, y, filled=False):  # 画实心、空心心形代表血量
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


def update_data_bar(p):  # 更新状态栏
    oled.line(15, 0, 15, 63, 1)  # 画线
    oled.DispChar(str(p.score), 0, 0, 1)  # 0~7分数
    p.update_hp_bar()
    p.update_mp_bar()


def skill_trigger(p, skill_type):  # 触发技能
    p.mp -= (200+100*skill_type)
    p.aura = True
    p.aura_skill_type = skill_type


def player_ui(p):  # 更新一次状态
    global barrage_list
    oled.fill(0)
    p.aura_skill()
    update_barrages()  # 弹幕更新
    p.move()
    p.update_hp()
    p.update_mp()
    p.update_score()
    p.update_oled()  # 玩家更新
    update_data_bar(p)
    oled.show()


def get_time():  # 获得从游戏开始计时的时间
    global t0
    return time.time()-t0


def main_game(difficulty):
    global t0
    t0 = int(time.time())  # 计时零点
    global barrage_list
    barrage_list.clear()
    global mp_time
    mp_time = 0
    global barstep
    barstep = 0
    p = player(72, 32)
    fps = 60  # 实际上并没有到60
    update_time = time.ticks_ms()
    while p.hp > 0:
        if time.ticks_diff(time.ticks_ms(), update_time) > (1000 // fps):  # 一帧更新一次
            if round(get_time()) > barstep:
                seed = []
                for i in range(11):
                    seed.append(random.randint(0, 9))
                result = seed_to_list(seed, difficulty)
                barstep += 1  # 每秒产生一次弹幕
                astep = result
            else:
                astep = []
            generate_barrages(astep, p)
            player_ui(p)
            if not button_a.value():
                show_game()  # 在游戏中按a键可返回开始界面，进度不会保存
            if p.score >= 50:  # 50分获胜
                show_win()
            if sound.read() > 1200 and p.mp >= 500:  # 用麦克风读入音量开启技能
                skill_trigger(p, 5)
            if sound.read() > 800 and p.mp >= 400:
                skill_trigger(p, 3)
            if sound.read() > 500 and p.mp >= 300:
                skill_trigger(p, 2)
            update_time = time.ticks_ms()
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
    oled.DispChar('Easy', 48, 8, 1)
    oled.DispChar('Normal', 32, 28, 1)
    oled.DispChar('Hard', 48, 48)


def writeChoice(choice):
    oled.fill_triangle(46, 12, 40, 8, 40, 16, 0)
    oled.fill_triangle(30, 32, 24, 28, 24, 36, 0)
    oled.fill_triangle(46, 52, 40, 48, 40, 56, 0)
    if choice == 0:
        oled.fill_triangle(46, 12, 40, 8, 40, 16, 1)
    elif choice == 1:
        oled.fill_triangle(30, 32, 24, 28, 24, 36, 1)
    elif choice == 2:
        oled.fill_triangle(46, 52, 40, 48, 40, 56, 1)
    oled.show()


def choose():
    oled.fill(0)
    oled.DispChar('按P/Y键进行左/右移动', 0, 0, 1)
    oled.DispChar('按O/N键进行上/下移动', 0, 16, 1)
    oled.DispChar('按a键确定难度', 0, 32, 1)
    oled.DispChar('>>>按a继续', 0, 48, 1)
    oled.show()
    while button_a.value():
        pass
    time.sleep(1)
    choice = 1
    oled.fill(0)
    while button_a.value():
        if touchPad_O.read() < 400:
            choice = (choice+1) % 3
        if touchPad_N.read() < 400:
            choice = (choice+2) % 3
        writeDifficulty()
        writeChoice(choice)
    return choice


def show_game():
    oled.fill(0)
    oled.DispChar('《如何躲避弹幕》', 0, 0, 1)
    oled.DispChar('按a键以开始游戏', 0, 16, 1)
    oled.show()
    while button_a.value():
        pass
    choice = choose()
    if choice == 0:
        difficulty = "Easy"
    elif choice == 1:
        difficulty = "Normal"
    else:
        difficulty = "Hard"
    countdown(3)
    main_game(difficulty)


if __name__ == '__main__':
    show_game()
