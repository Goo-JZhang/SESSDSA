from mpython import *
import audio
import urequests
import json
import machine
import ubinascii
import time
import network
myUI=UI(oled)
#my_wifi = wifi()
#my_wifi.connectWiFi('123', '20001103')

barrage_list = []

#y：59~64为蓝条

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
        if x < 0 or x > 128 or y < 0 or y > 58:
            self.outranged = True

    def update_oled(self):
        self.update_next_move()
        if not self.outranged():
            #十字弹幕
            oled.pixel(self.x, self.y, 1)
            oled.pixel(self.x+1, self.y, 1) if self.x+1 < 128
            oled.pixel(self.x-1, self.y, 1) if self.x-1 > 0
            oled.pixel(self.x, self.y+1, 1) if self.y+1 < 58
            oled.pixel(self.x, self.y - 1, 1) if self.y - 1 >= 0
            if large:
                #3*3实心方形弹幕
                oled.pixel(self.x+1, self.y+1, 1) if self.x+1 < 128 and self.y+1 < 58
                oled.pixel(self.x-1, self.y-1, 1) if self.x-1 > 0 and self.y-1 > 0
                oled.pixel(self.x-1, self.y+1, 1) if self.y+1 < 58 and self.x-1 > 0
                oled.pixel(self.x+1, self.y - 1, 1) if self.y - 1 > 0 and self.x+1 < 128


def generate_barrages(x, y):  # xy别越界, 产生同心的8个弹幕
    global barrage_list
    barrage_list.append(barrage(x, y, 0, 1))
    barrage_list.append(barrage(x, y, 1, 0))
    barrage_list.append(barrage(x, y, 1, 1))
    barrage_list.append(barrage(x, y, 0, -1))
    barrage_list.append(barrage(x, y, -1, -1))
    barrage_list.append(barrage(x, y, -1, 0))
    barrage_list.append(barrage(x, y, -1, 1))
    barrage_list.append(barrage(x, y, 1, -1))


class player():
    global barrage_list

    def __init__(self, x, y, hp=5,mp=0):
        self.x = x
        self.y = y
        self.hp = hp
        self.mp=mp

    def move(self):  # 通过按键实现四个方向移动
        #p左y右o上n下
        if touchPad_P.read() < 100 and self.x >= 1:
            self.x -= 1
        if touchPad_Y.read() < 100 and self.x <= 127:
            self.x += 1
        if touchPad_O.read() < 100 and self.y >= 1:
            self.y -= 1
        if touchPad_N.read() < 100 and self.y <= 58:
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
            if bar.large:
                if (self.x == bar.x+1 and self.y == bar.y+1) or \
                        (self.x == bar.x+1 and self.y == bar.y-1) or \
                        (self.x == bar.x-1 and self.y == bar.y-1) or \
                        (self.x == bar.x-1 and self.y == bar.y + 1):
                    self.hp -= 1

    def update_mp(self): #攒够蓝可语音开大？
        self.mp+=5

    def update_oled(self):
        oled.pixel(self.x, self.y, 1)
        oled.ProgressBar(0,59,128,5,self.mp) #这个按说明书写的进度条不知道能不能用，不能可手动写



def player_ui(p):
    global barrage_list
    oled.fill(0)
    for bar in barrage_list:  # 弹幕更新一步
        bar.update_oled()
    p.move()  # 玩家移动，是否要加条件？
    p.update_hp()
    p.update_mp()
    p.update_oled()  # 玩家更新
    oled.DispChar(str(p.hp), 0, 0, 1)  #显示血量
    
    #time.sleep(???) #要不要控制帧率

    oled.show()


def ZPW():
    global barrage_list
    barrage.clear()
    generate_barrages(25, 25)  # 这里只生成了一波弹幕，以后要加弹幕产生机制
    p = player(58, 32)  # 玩家初始放哪？
    while p.hp > 0:
        player_ui(p)
        if p.mp >= 100:
            pass#语音开大待施工
    if p.hp == 0:
        show_death()


def show_death():
    oled.fill(0)
    oled.DispChar('GG！按a重新开始', 0, 0, 1)
    oled.show()
    if button_a.value():
        countdown(3)
        ZPW()


def countdown(t):
    #倒计时界面
    oled.fill(0)
    oled.circle(58, 32, 15, 1)
    while t >= 0:
        oled.DispChar(str(t), 58, 32, 1)  # 我不知道这会重写第一行还是直接在原来的上面显示。。
        time.sleep(1)
        t -= 1
        oled.show()


def show_game():
    oled.fill(0)
    oled.DispChar('欢迎来到嘴炮王！按a键以开始游戏', 0, 0, 1)
    #加一些规则说明？
    oled.show()
    if button_a.value():
        countdown(3)
        ZPW()


if __name__ == '__main__':
    show_game()



#语音模块

def Get_asr_start():
    audio.recorder_init()
    audio.record("temp.mp3", 1)
    audio.recorder_deinit()

def Get_asr_result_discern(filename):
    _response = urequests.post("http://119.23.66.134:8085/file_upload",
        files={"file": (filename, "audio/mp3")},
        params={"appid": "1", "mediatype":"2", "deviceid":ubinascii.hexlify(machine.unique_id()).decode().upper()})
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

