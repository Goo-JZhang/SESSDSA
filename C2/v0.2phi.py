from mpython import *
import audio
import urequests
import json
import machine
import ubinascii
import time
import network
#my_wifi = wifi()
#my_wifi.connectWiFi('123', '20001103')

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


class player():
    global barrage_list

    def __init__(self, x, y, hp=5, mp=0):
        self.x = x
        self.y = y

    def move(self):  # 通过按键实现四个方向移动
        #p左y右o上n下
        if touchPad_P.read() < 100 and self.x >= 16:
            self.x -= 1
        if touchPad_Y.read() < 100 and self.x <= 127:
            self.x += 1
        if touchPad_O.read() < 100 and self.y >= 0:
            self.y -= 1
        if touchPad_N.read() < 100 and self.y <= 63:
            self.y += 1

    def update_oled(self):
        oled.pixel(self.x, self.y, 1)


def player_ui(p):
    global barrage_list
    oled.fill(0)
    for bar in barrage_list:  # 弹幕更新一步
        bar.update_oled()
    p.move()  # 玩家移动，是否要加条件？
    p.update_oled()  # 玩家更新

    #time.sleep(???) #要不要控制帧率

    oled.show()


def ZPW():
    global barrage_list
    barrage_list.clear()
    barrage_list.append(barrage(40, 40, 1, -1))
    p = player(58, 32)  # 玩家初始放哪？
    rgb[0] = (int(255), int(0), int(0))  # for test
    rgb.write()
    while 1:
        player_ui(p)


def countdown(t):
    #倒计时界面
    while t >= 0:
        if t == 0:
            oled.fill(0)
            oled.DispChar('开始', 56, 28, 1)
            oled.show()
            break
        oled.fill(0)
        oled.circle(64, 32, 7, 1)
        oled.DispChar(str(t), 60, 28, 1)
        time.sleep(1)
        t -= 1
        oled.show()


def show_game():
    oled.fill(0)
    oled.DispChar('欢迎来到嘴炮王！', 0, 0, 1)
    oled.DispChar('按a键以开始游戏', 0, 8, 1)
    oled.show()
    while button_a.value():
        pass
    countdown(3)
    ZPW()


if __name__ == '__main__':
    show_game()

'''
加self
改if
改开关
outrange()
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
