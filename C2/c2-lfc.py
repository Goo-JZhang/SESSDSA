from mpython import *

barrage_list = []

class barrage():
    def __init__(self, x, y, vx, vy, large=False):
        self.x = x
        self.y = y
        #vx,vy: -1,0,1，弹幕每次只能向八个方向中的一个走一步
        self.vx = vx
        self.vy = vy
        self.large = large
        self.outranged=False
        
    def update_next_move(self):
        #更新下一步位置，标记越界情况
        self.x += self.vx
        self.y += self.vy
        if x < 0 or x > 128 or y < 0 or y > 64:
            self.outranged=True

    def update_oled(self):
        self.update_next_move()
        if not self.outranged():
            #十字弹幕
            oled.pixel(self.x, self.y, 1)
            oled.pixel(self.x+1, self.y, 1) if self.x+1<=128
            oled.pixel(self.x-1, self.y, 1) if self.x-1>=0
            oled.pixel(self.x, self.y+1, 1) if self.y+1<=64
            oled.pixel(self.x, self.y - 1, 1) if self.y - 1 >= 0
            if large:
                #大十字弹幕
                oled.pixel(self.x + 2, self.y, 1) if self.x + 2 <= 128
                oled.pixel(self.x - 2, self.y, 1) if self.x - 2 >= 0
                oled.pixel(self.x, self.y+2, 1) if self.y + 2 <= 64
                oled.pixel(self.x, self.y - 2, 1) if self.y - 2 >= 0

def generate_barrages(x, y): #xy别越界, 产生同心的8个弹幕
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
    def __init__(self, x, y, hp=5):
        self.x = x
        self.y = y
        self.hp = hp
        
    def move(self):  #通过按键实现四个方向移动
        #p左y右o上n下
        if touchPad_P.read() < 100 and self.x>=1:
            self.x -= 1
        if touchPad_Y.read() < 100 and self.x <= 127:
            self.x += 1
        if touchPad_O.read() < 100 and self.y >= 1:
            self.y -= 1
        if touchPad_N.read() < 100 and self.y <= 63:
            self.y += 1

    def hurt(self): #在在oled内存更新了弹幕状况，算出了玩家即将走的位置但还没有更新玩家对应oled内存时，读oled状态判断玩家是否与弹幕发生了碰撞
        pass

    def update_oled(self):
        oled.pixel(self.x, self.y, 1)

def player_ui():
    global barrage_list
    oled.fill(0)
    for bar in barrage_list: #弹幕更新一步
        bar.update_oled()
    player.move()  #玩家移动，是否要加条件？
    player.update_oled() #玩家更新
    #time.sleep(???) #要不要控制帧率
    oled.show()

def show_game():
    global barrage_list
    if touchPad_P.read() < 100:
    
    pass

def countdown(t):
    oled.fill(0)
    oled.circle(64, 32, 15, 1)
    while t >= 0:
        oled.DispChar(str(t), 64, 32, 1)
        time.sleep(1)
        t -= 1
        oled.show()

def show_game():
    oled.fill(0)
    oled.DispChar('欢迎来到嘴炮王！', 0, 0, 1)
    #加一些规则说明
    #oled.DispChar('按a键以开始游戏',,,)
    oled.show()
    if button_a.value():
        countdown(3)
        ZPW()

if __name__ == '__main__':
    show_game()
