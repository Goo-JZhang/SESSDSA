from mpython import *
import audio
import urequests
import json
import machine
import ubinascii
import time
import network

'''
界面字体大小pass
蓝条样式
充能速度
点的范围
回到开始界面

语音识别
'''

barrage_list = []

#x：0~15为蓝条
#x: 16~127  y: 0~63


class barrage():
    def __init__(self, x, y, vx, vy, large=False):
        self.x = x
        self.y = y
        #vx,vy: -1,0,1，弹幕每次只能向八个方向中的一个走一步
        self.vx = vx
        self.vy = vy
        self.large = large
        self.outranged = False

    def update_next_move(self):
        #更新下一步位置，标记越界情况
        self.x += self.vx
        self.y += self.vy
        if self.x < 16 or self.x > 127 or self.y < 0 or self.y > 63:
            self.outranged = True

    def update_oled(self):
        self.update_next_move()
        if not self.outranged:
            #十字弹幕
            oled.pixel(self.x, self.y, 1)
            if self.x + 1 <= 127:
                oled.pixel(self.x + 1, self.y, 1)
            if self.x-1 >= 16:
                oled.pixel(self.x-1, self.y, 1)
            if self.y+1 <= 63:
                oled.pixel(self.x, self.y+1, 1)
            if self.y - 1 >= 0:
                oled.pixel(self.x, self.y - 1, 1)
            if self.large:
                #3*3实心方形弹幕
                if self.x+1 <= 127 and self.y+1 <= 63:
                    oled.pixel(self.x+1, self.y+1, 1)
                if self.x-1 >= 16 and self.y-1 >= 0:
                    oled.pixel(self.x-1, self.y-1, 1)
                if self.y+1 <= 63 and self.x-1 >= 16:
                    oled.pixel(self.x-1, self.y+1, 1)
                if self.y - 1 >= 0 and self.x+1 <= 127:
                    oled.pixel(self.x+1, self.y - 1, 1)


def generate_barrages(x, y, l=False):  # xy别越界, 产生同心的8个弹幕,l for large
    global barrage_list
    barrage_list.append(barrage(x, y, 0, 1, l))
    barrage_list.append(barrage(x, y, 1, 0, l))
    barrage_list.append(barrage(x, y, 1, 1, l))
    barrage_list.append(barrage(x, y, 0, -1, l))
    barrage_list.append(barrage(x, y, -1, -1, l))
    barrage_list.append(barrage(x, y, -1, 0, l))
    barrage_list.append(barrage(x, y, -1, 1, l))
    barrage_list.append(barrage(x, y, 1, -1, l))


def generate_waves():
    generate_barrages(30, 30)  # 后续完善


class player():
    global barrage_list

    def __init__(self, x, y, hp=5, mp=0):
        self.x = x
        self.y = y
        self.hp = hp
        self.mp = mp
        self.score = 0

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
            if (self.x == bar.x and self.y == bar.y) or \
                (self.x == bar.x+1 and self.y == bar.y) or \
                (self.x == bar.x-1 and self.y == bar.y) or \
                (self.x == bar.x and self.y == bar.y+1) or \
                    (self.x == bar.x and self.y == bar.y - 1):
                self.hp -= 1
                barrage_list.remove(bar)
            if bar.large:
                if (self.x == bar.x+1 and self.y == bar.y+1) or \
                        (self.x == bar.x+1 and self.y == bar.y-1) or \
                        (self.x == bar.x-1 and self.y == bar.y-1) or \
                        (self.x == bar.x-1 and self.y == bar.y + 1):
                    self.hp -= 1
                    barrage_list.remove(bar)

    def update_mp(self):  # 攒够蓝可语音开大？
        global mp_time
        delta = get_time() - mp_time
        mp_time = get_time()
        self.mp += 50*delta
        if self.mp >= 601:  # 蓝量上限
            self.mp = 601

    def update_score(self):
        self.score = get_time()  # 一秒一分

    def update_oled(self):
        oled.pixel(self.x, self.y, 0)
        oled.pixel(self.x+1,self.y,1)
        oled.pixel(self.x-1,self.y,1)
        oled.pixel(self.x,self.y+1,1)
        oled.pixel(self.x,self.y-1,1)#frame of player

    def update_hp_bar(self):
        if self.hp<5:
            for i in range(self.hp):
                oled.pixel(3*i+1,18,1)
                oled.pixel(3*i,17,1)
                oled.pixel(3*i+2,17,1)
        else:
            for i in range(5):
                oled.pixel(3*i+1,18,1)
                oled.pixel(3*i,17,1)
                oled.pixel(3*i+2,17,1)
            for i in range(self.hp-5):
                oled.pixel(3*i+1,20,1)
                oled.pixel(3*i,19,1)
                oled.pixel(3*i+2,19,1) 
    
    def update_power_bar(self):
        if self.mp >= 100:
            oled.fill_rect(2, 55, 10, 7, 1)
        if self.mp >= 200:
            oled.fill_rect(2, 47, 10, 7, 1)
        if self.mp >= 300:
            oled.fill_rect(2, 39, 10, 7, 1)
        if self.mp >= 400:
            oled.fill_rect(2, 31, 10, 7, 1)
        if self.mp >= 500:
            oled.fill_rect(2, 23, 10, 7, 1)


def update_data_bar(p):
    oled.line(15, 0, 15, 63, 1)  # 画线
    oled.DispChar(str(p.score), 0, 0, 1)  # 0~7分数
    p.update_hp_bar()
    p.update_power_bar()

def player_ui(p):
    global barrage_list
    oled.fill(0)
    for bar in barrage_list:  # 弹幕更新一步
        bar.update_oled()
    p.move()  # 玩家移动，是否要加条件？
    p.update_hp()
    p.update_mp()
    p.update_score()
    p.update_oled()  # 玩家更新
    update_data_bar(p)
    #time.sleep(???) #要不要控制帧率
    oled.show()


def get_time():
    global t0
    return time.time()-t0


def Get_asr_start():
    audio.recorder_init()
    audio.record("temp.mp3", 1)
    audio.recorder_deinit()


def Get_asr_result_discern(filename):
    _response = urequests.post("http://119.23.66.134:8085/file_upload",
                               files={"file": (filename, "audio/mp3")},
                               params={"appid": "1", "mediatype": "2", "deviceid": ubinascii.hexlify(machine.unique_id()).decode().upper()})
    rsp_json = _response.json()
    _response.close()
    if "text" in rsp_json:
        return rsp_json["text"]
    elif "Code" in rsp_json:
        return "."
    else:
        return rsp_json


def speech_recognition():
    rgb[0] = (0, 255, 0)
    rgb.write()
    Get_asr_start()
    get_asr_result_discern = Get_asr_result_discern("temp.mp3")[0:-1]
    return get_asr_result_discern

def ZPW():
    global t0
    global barrage_list
    global mp_time
    mp_time = 0
    barrage_list.clear()
    t0 = int(time.time())  # 计时零点
    generate_waves()  # 这里只生成了一波弹幕，以后要加弹幕产生机制
    p = player(72, 32)  # 玩家初始放哪？
    while p.hp > 0:
        player_ui(p)
        if p.mp >= 400:
            if not button_b.value():
                sound_input = speech_recognition()
                oled.DispChar(str(sound_input), 0, 0, 1)
                oled.show()
                #if '西红柿' in speech_recognition():


    if p.hp <= 0:
        show_death()


def show_death():
    oled.fill(0)
    oled.DispChar('GG！', 0, 0, 1)
    oled.DispChar('按a重新开始', 0, 16, 1)
    oled.show()
    while button_a.value():
        pass
    countdown(3)
    ZPW()


def countdown(t):
    #倒计时界面
    while t >= 0:
        if t == 0:
            oled.fill(0)
            oled.DispChar('开始', 56, 28, 1)
            oled.show()
            time.sleep(1)
            break
        oled.fill(0)
        oled.circle(64, 32, 9, 1)
        oled.DispChar(str(t), 62, 24, 1)
        oled.show()
        time.sleep(1)
        t -= 1


def show_game():
    oled.fill(0)
    oled.DispChar('欢迎来到嘴炮王！', 0, 0, 1)
    oled.DispChar('按a键以开始游戏', 0, 16, 1)
    oled.show()
    while button_a.value():
        pass
    countdown(3)
    ZPW()


if __name__ == '__main__':
    my_wifi = wifi()
    my_wifi.connectWiFi('HONOR V20', '12345687')
    if my_wifi.sta.isconnected():
        rgb[2] = (0, 255, 0)
        rgb.write()
    else:
        rgb[2] = (255, 0, 0)
        rgb.write()
    show_game()

'''
更新了mp、score算法
'''

#语音模块
'''
def Get_asr_start():
    audio.recorder_init()
    audio.record("temp.mp3", 1)
    audio.recorder_deinit()


def Get_asr_result_discern(filename):
    _response = urequests.post("http://119.23.66.134:8085/file_upload",
                               files={"file": (filename, "audio/mp3")},
                               params={"appid": "1", "mediatype": "2", "deviceid": ubinascii.hexlify(machine.unique_id()).decode().upper()})
    rsp_json = _response.json()
    _response.close()
    if "text" in rsp_json:
        return rsp_json["text"]
    elif "Code" in rsp_json:
        return "."
    else:
        return rsp_json


def speech_recognition():
    rgb[0] = (int(0), int(0), int(255))
    rgb.write()
    Get_asr_start()
    get_asr_result_discern = Get_asr_result_discern("temp.mp3")[0:-1]
    rgb[0] = (int(0), int(0), int(0))
    rgb.write()
    return get_asr_result_discern

'''
