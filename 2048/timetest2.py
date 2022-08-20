import time
import timeit
import random

MAXTIME = 5     # 最大时间限制
ROUNDS = 500    # 总回合数
REPEAT = 10     # 单循环轮数

ROWS = 4        # 行总数
COLUMNS = 8     # 列总数
MAXLEVEL = 14   # 总级别数

SLEEP = 0.3       # 直播等待时间

ARRAY = list(range(ROUNDS))  # 随机(?)列表

NAMES = {_: str(2 ** _).zfill(4) for _ in range(MAXLEVEL)}  # 将内在级别转换为显示对象的字典
NAMES[0] = '0000'

class _DIRECTIONS(list):
    def __init__(self):
        super().__init__(['up', 'down', 'left', 'right'])
    def __getitem__(self, key):
        return super().__getitem__(key) if key in range(4) else 'unknown'
DIRECTIONS = _DIRECTIONS()      # 换算方向的字典

PLAYERS = {True: 'player 0', False: 'player 1'}  # 换算先后手名称的字典

PICTURES = ['nanami', 'ayase']  # 游戏图片名称
LENGTH = 100                    # 格子的边长
PADX = PADY = 10                # 边界填充的距离
WORD_SIZE = (5, 2)              # 标签大小
FONT = ('Verdana', 40, 'bold')  # 文字字体

COLOR_BACKGROUND = '#92877d'    # 全局背景色
COLOR_NONE = '#9e948a'          # 初始界面方格色

COLOR_CELL = {'+': '#eee4da', '-': '#f2b179'}  # 双方的方格色
COLOR_WORD = {'+': '#776e65', '-': '#f9f6f2'}  # 双方的文字色

KEY_BACKWARD = "\'[\'"  # 回退
KEY_FORWARD = "\']\'"   # 前进


# 棋子

from collections import namedtuple
'''
-> 初始化棋子
-> 参数: belong   归属, 为bool, True代表先手
-> 参数: position 位置, 为tuple
-> 参数: value    数值, 为int
'''

Chessman = namedtuple('Chessman', 'belong position value')

# 棋盘

class Chessboard:
    def __init__(self, array):
        '''
        -> 初始化棋盘
        '''
        self.array = array  # 随机序列
        self.board = {}  # 棋盘所有棋子
        self.belongs = {True: [], False: []}  # 双方的棋子位置
        self.decision = {True: (), False: ()}  # 双方上一步的决策
        self.time = {True: 0, False: 0}  # 双方剩余的时长
        self.anime = []  # 动画效果
        

    def add(self, belong, position, value = 1):
        '''
        -> 在指定位置下棋
        '''
        belong = position[1] < COLUMNS // 2  # 重定义棋子的归属
        self.belongs[belong].append(position)
        self.board[position] = Chessman(belong, position, value)

    def move(self, belong, direction):
        '''
        -> 向指定方向合并, 返回是否变化
        '''
        self.anime = []
        def inBoard(position):  # 判断是否在棋盘内
            return position[0] in range(ROWS) and position[1] in range(COLUMNS)
        def isMine(position):   # 判断是否在领域中
            return belong if position[1] < COLUMNS // 2 else not belong
        def theNext(position):  # 返回下一个位置
            delta = [(-1,0), (1,0), (0,-1), (0,1)][direction]
            return (position[0] + delta[0], position[1] + delta[1])
        def conditionalSorted(chessmanList):  # 返回根据不同的条件排序结果
            if direction == 0: return sorted(chessmanList, key = lambda x:x[0], reverse = False)
            if direction == 1: return sorted(chessmanList, key = lambda x:x[0], reverse = True )
            if direction == 2: return sorted(chessmanList, key = lambda x:x[1], reverse = False)
            if direction == 3: return sorted(chessmanList, key = lambda x:x[1], reverse = True )
            return []
        def move_one(chessman, eaten):  # 移动一个棋子并返回是否移动, eaten是已经被吃过的棋子位置
            nowPosition = chessman.position
            nextPosition = theNext(nowPosition)
            while inBoard(nextPosition) and isMine(nextPosition) and nextPosition not in self.board:  # 跳过己方空格
                nowPosition = nextPosition
                nextPosition = theNext(nextPosition)
            if inBoard(nextPosition) and nextPosition in self.board and nextPosition not in eaten \
                    and chessman.value == self.board[nextPosition].value:  # 满足吃棋条件
                self.anime.append(chessman.position + nextPosition)
                self.belongs[belong].remove(chessman.position)
                self.belongs[belong if nextPosition in self.belongs[belong] else not belong].remove(nextPosition)
                self.belongs[belong].append(nextPosition)
                self.board[nextPosition] = Chessman(belong, nextPosition, chessman.value + 1)
                del self.board[chessman.position]
                eaten.append(nextPosition)
                return True
            elif nowPosition != chessman.position:  # 不吃棋但移动了
                self.anime.append(chessman.position + nowPosition)
                self.belongs[belong].remove(chessman.position)
                self.belongs[belong].append(nowPosition)
                self.board[nowPosition] = Chessman(belong, nowPosition, chessman.value)
                del self.board[chessman.position]
                return True
            else:  # 未发生移动
                return False
        eaten = []
        change = False
        for _ in conditionalSorted(self.belongs[belong]):
            if move_one(self.board[_], eaten): change = True
        return change

    def getBelong(self, position):
        '''
        -> 返回归属
        '''
        return self.board[position].belong if position in self.board else position[1] < COLUMNS // 2

    def getValue(self, position):
        '''
        -> 返回数值
        '''
        return self.board[position].value if position in self.board else 0

    def getScore(self, belong):
        '''
        -> 返回某方的全部棋子数值列表
        '''
        return sorted(map(lambda x: self.board[x].value, self.belongs[belong]))

    def getNone(self, belong):
        '''
        -> 返回某方的全部空位列表
        '''
        return [(row, column) for row in range(ROWS) for column in range(COLUMNS) \
                if ((column < COLUMNS // 2) == belong) and (row, column) not in self.board]
    
    def getNext(self, belong, currentRound):
        '''
        -> 根据随机序列得到在本方领域允许下棋的位置
        '''
        available = self.getNone(belong)
        if not belong: available.reverse()  # 后手序列翻转
        return available[self.array[currentRound] % len(available)] if available != [] else ()

    def updateDecision(self, belong, decision):
        '''
        -> 更新决策
        '''
        self.decision[belong] = decision

    def getDecision(self, belong):
        '''
        -> 返回上一步的决策信息
        -> 无决策为(), 位置决策为position, 方向决策为(direction,)
        -> 采用同类型返回值是为了和优化库统一接口
        '''
        return self.decision[belong]

    def updateTime(self, belong, time):
        '''
        -> 更新剩余时间
        '''
        self.time[belong] = time

    def getTime(self, belong):
        '''
        -> 返回剩余时间
        '''
        return self.time[belong]

    def getAnime(self):
        '''
        -> 返回动画效果辅助信息
        '''
        return self.anime

    def copy(self):
        '''
        -> 返回一个对象拷贝
        '''
        new = Chessboard(self.array)
        new.board = self.board.copy()
        new.belongs[True] = self.belongs[True].copy()
        new.belongs[False] = self.belongs[False].copy()
        new.decision = self.decision.copy()
        new.time = self.time.copy()
        new.anime = self.anime.copy()
        return new

    def __repr__(self):
        '''
        -> 打印棋盘, + 代表先手, - 代表后手
        '''       
        return '\n'.join([' '.join([('+' if self.getBelong((row, column)) else '-') + str(self.getValue((row, column))).zfill(2) \
                                   for column in range(COLUMNS)]) \
                         for row in range(ROWS)])
    __str__ = __repr__




class Player1:
    def __init__(self, isFirst, array):
        self.isFirst = isFirst
        self.array=array
        self.currentRound=0
        self.answer=None
        self.end_depth=0
        self.round_mode=self.set_round_mode()
        self.answer=None

    def output(self, currentRound, board, mode):
        self.currentRound = currentRound
        if mode=='_position' or mode=='_direction':
            return None
        else:
            if mode=='position':
                move_mode="my_position"
            else:
                move_mode="my_direction"
            self.make_move_decision(board.copy(), move_mode) 
            return self.answer

    def set_round_mode(self):
        if self.isFirst == True:
            return ['my_position','your_position','my_direction','your_direction']
        else:
            return ['my_position','your_direction','my_direction','your_position']

    def get_next_mode(self,current_mode):
        return self.round_mode[(self.round_mode.index(current_mode)+1)%4]

    def make_move_decision(self,chessboard,player_move_mode):
        self.answer = None
        if self.currentRound<=150:
            self.end_depth=7
        elif self.currentRound<=280:
            self.end_depth=8
        else:
            self.end_depth=9
        self.move_search(chessboard, player_move_mode, 0, float('inf'))

    def evl(self,board):
        val=0
        my_sc=board.getScore(self.isFirst)
        your_sc=board.getScore(not self.isFirst)
        my_weight=2.5
        your_weight=2
        for me in my_sc:
            if len(my_sc)>0 and me==my_sc[-1]:
                val+=(my_weight**me)**2.5
            elif len(my_sc)>1 and me==my_sc[-2]:
                val+=(my_weight**me)**2
            elif len(my_sc)>2 and me==my_sc[-3]:
                val+=(my_weight**me)**1.6
            else:
                val+=(my_weight**me)**1.2
        for you in your_sc:
            if len(your_sc)>0 and you==your_sc[-1]:
                val-=(your_weight**you)**2.4
            elif len(your_sc)>1 and you==your_sc[-2]:
                val-=(your_weight**you)**1.9
            elif len(your_sc)>2 and you==your_sc[-3]:
                val-=(your_weight**you)**1.5
            else:
                val-=(your_weight**you)**1.1
        return val

    def move_search(self,chessboard,player_move_mode,depth,last_max_min):
        max_min=0

        if depth == self.end_depth:
            return self.evl(chessboard)

        if player_move_mode == 'my_position':
            max_min=float('-inf')
            pos=chessboard.getNext(self.isFirst,self.currentRound)
            if  pos != ():
                next_chessboard=chessboard.copy()
                next_chessboard.add(self.isFirst,pos)
                new_value=self.move_search(next_chessboard,self.get_next_mode(player_move_mode),depth+1,max_min)
                if depth!=0:  
                    max_min=max(max_min,new_value)
                elif (new_value>max_min): #首层决策
                    max_min=new_value
                    self.answer=pos
                if max_min>last_max_min:
                    return max_min
            else:
                for row in range(4):
                    for col in range(8):
                        pos=(row,col)
                        if chessboard.getValue(pos)==0 and chessboard.getBelong(pos)!=self.isFirst:
                            next_chessboard=chessboard.copy()
                            next_chessboard.add(not self.isFirst,pos)
                            new_value=self.move_search(next_chessboard,self.get_next_mode(player_move_mode),depth+1,max_min)
                        else:
                            new_value=float('-inf')
                        if depth!=0:  
                            max_min=max(max_min,new_value)
                        elif (new_value>max_min): #首层决策
                            max_min=new_value
                            self.answer=pos
                        if max_min>last_max_min:
                            return max_min
            if max_min == float('-inf'):
                return self.evl(chessboard)

        if player_move_mode == 'your_position':
            max_min=float('inf')
            pos=chessboard.getNext(not self.isFirst,self.currentRound)
            if  pos != ():
                next_chessboard=chessboard.copy()
                next_chessboard.add(not self.isFirst,pos)
                new_value=self.move_search(next_chessboard,self.get_next_mode(player_move_mode),depth+1,max_min)
                max_min=min(max_min,new_value)
                if max_min<=last_max_min:
                    return max_min
            else:
                for row in range(4):
                    for col in range(8):
                        pos=(row,col)
                        if chessboard.getValue(pos)==0 and chessboard.getBelong(pos)==self.isFirst:
                            next_chessboard=chessboard.copy()
                            next_chessboard.add(self.isFirst,pos)
                            new_value=self.move_search(next_chessboard,self.get_next_mode(player_move_mode),depth+1,max_min)
                        else:
                            new_value=float('inf')
                        max_min=min(max_min,new_value)
                        if max_min<=last_max_min:
                            return max_min
            if max_min == float('inf'):
                return self.evl(chessboard)


            
        if player_move_mode == 'my_direction':
            max_min=float('-inf')
            for direction in range(4):
                next_chessboard=chessboard.copy()
                if next_chessboard.move(self.isFirst,direction):
                    if not self.isFirst:
                        self.currentRound+=1
                    new_value=self.move_search(next_chessboard,self.get_next_mode(player_move_mode),depth+1,max_min)
                    if not self.isFirst:
                        self.currentRound-=1
                else:
                    new_value=float('-inf')
                if depth != 0:  
                    max_min = max(max_min, new_value)
                elif (new_value>max_min):
                    max_min=new_value
                    self.answer=direction
                if max_min>last_max_min:
                    return max_min
            if max_min == float('-inf'):
                return self.evl(chessboard)


        if player_move_mode == 'your_direction':
            max_min=float('inf')
            for direction in range(4):
                next_chessboard=chessboard.copy()
                if next_chessboard.move(not self.isFirst,direction):
                    if self.isFirst:
                        self.currentRound+=1
                    new_value=self.move_search(next_chessboard,self.get_next_mode(player_move_mode),depth+1,max_min)
                    if self.isFirst:
                        self.currentRound-=1
                else:
                    new_value=float('inf')
                max_min = min(max_min, new_value)
                if max_min<=last_max_min:
                    return max_min
            if max_min == float('inf'):
                return self.evl(chessboard)

        return max_min


class Player2:
    def __init__(self, isFirst, array):
        self.isFirst = isFirst
        self.array=array
        self.currentRound=0
        self.answer=None
        self.end_depth=0
        self.round_mode=self.set_round_mode()
        self.answer=None

    def output(self, currentRound, board, mode):
        self.currentRound = currentRound
        if mode=='_position' or mode=='_direction':
            return None
        else:
            if mode=='position':
                move_mode=1
            else:
                move_mode=3
            self.make_move_decision(board.copy(), move_mode,board.getTime(self.isFirst)) 
            return self.answer

    def set_round_mode(self):
        if self.isFirst == True:
            return [1,2,3,4] #mypos,yourpos,mydir,yourdir
        else:
            return [1,4,3,2]

    def get_next_mode(self,current_mode):
        return self.round_mode[(self.round_mode.index(current_mode)+1)%4]

    def make_move_decision(self,chessboard,player_move_mode,time_left):
        self.answer = None
        if time_left <= 0.1:
            self.end_depth = 6
        elif time_left <= 0.2:
            self.end_depth = 8
        else:
            if self.currentRound <= 80:
                self.end_depth=6
            elif self.currentRound<=150:
                self.end_depth=7
            elif self.currentRound<=280:
                self.end_depth=8
            elif self.currentRound<=400:
                self.end_depth = 9
            else:
                self.end_depth = 10
            if 500 - self.currentRound <= 10:
                self.end_depth = 500 - self.currentRound
        self.move_search(chessboard, player_move_mode, 0, float('inf'))

    def evl(self,board):
        val=0
        my_sc=board.getScore(self.isFirst)
        your_sc=board.getScore(not self.isFirst)
        my_weight=2.5
        your_weight=2
        for me in my_sc:
            if len(my_sc)>0 and me==my_sc[-1]:
                val+=(my_weight**me)**2.5
            elif len(my_sc)>1 and me==my_sc[-2]:
                val+=(my_weight**me)**2
            elif len(my_sc)>2 and me==my_sc[-3]:
                val+=(my_weight**me)**1.6
            else:
                val+=(my_weight**me)**1.2
        for you in your_sc:
            if len(your_sc)>0 and you==your_sc[-1]:
                val-=(your_weight**you)**2.4
            elif len(your_sc)>1 and you==your_sc[-2]:
                val-=(your_weight**you)**1.9
            elif len(your_sc)>2 and you==your_sc[-3]:
                val-=(your_weight**you)**1.5
            else:
                val-=(your_weight**you)**1.1
        return val

    def move_search(self,chessboard,player_move_mode,depth,last_max_min):
        max_min=0

        if depth == self.end_depth:
            return self.evl(chessboard)

        if player_move_mode == 1:
            max_min=float('-inf')
            pos=chessboard.getNext(self.isFirst,self.currentRound)
            if  pos != ():
                next_chessboard=chessboard.copy()
                next_chessboard.add(self.isFirst,pos)
                new_value=self.move_search(next_chessboard,self.get_next_mode(player_move_mode),depth+1,max_min)
                if depth!=0:  
                    max_min=max(max_min,new_value)
                elif (new_value>max_min): #�ײ����
                    max_min=new_value
                    self.answer=pos
                if max_min>last_max_min:
                    return max_min
            else:
                for row in range(4):
                    for col in range(8):
                        pos=(row,col)
                        if chessboard.getValue(pos)==0 and chessboard.getBelong(pos)!=self.isFirst:
                            next_chessboard=chessboard.copy()
                            next_chessboard.add(not self.isFirst,pos)
                            new_value=self.move_search(next_chessboard,self.get_next_mode(player_move_mode),depth+1,max_min)
                        else:
                            new_value=float('-inf')
                        if depth!=0:  
                            max_min=max(max_min,new_value)
                        elif (new_value>max_min): #�ײ����
                            max_min=new_value
                            self.answer=pos
                        if max_min>last_max_min:
                            return max_min
            if max_min == float('-inf'):
                return self.evl(chessboard)

        if player_move_mode == 2:
            max_min=float('inf')
            pos=chessboard.getNext(not self.isFirst,self.currentRound)
            if  pos != ():
                next_chessboard=chessboard.copy()
                next_chessboard.add(not self.isFirst,pos)
                new_value=self.move_search(next_chessboard,self.get_next_mode(player_move_mode),depth+1,max_min)
                max_min=min(max_min,new_value)
                if max_min<=last_max_min:
                    return max_min
            else:
                for row in range(4):
                    for col in range(8):
                        pos=(row,col)
                        if chessboard.getValue(pos)==0 and chessboard.getBelong(pos)==self.isFirst:
                            next_chessboard=chessboard.copy()
                            next_chessboard.add(self.isFirst,pos)
                            new_value=self.move_search(next_chessboard,self.get_next_mode(player_move_mode),depth+1,max_min)
                        else:
                            new_value=float('inf')
                        max_min=min(max_min,new_value)
                        if max_min<=last_max_min:
                            return max_min
            if max_min == float('inf'):
                return self.evl(chessboard)


            
        if player_move_mode == 3:
            max_min=float('-inf')
            for direction in range(4):
                next_chessboard=chessboard.copy()
                if next_chessboard.move(self.isFirst,direction):
                    if not self.isFirst:
                        self.currentRound+=1
                    new_value=self.move_search(next_chessboard,self.get_next_mode(player_move_mode),depth+1,max_min)
                    if not self.isFirst:
                        self.currentRound-=1
                else:
                    new_value=float('-inf')
                if depth != 0:  
                    max_min = max(max_min, new_value)
                elif (new_value>max_min):
                    max_min=new_value
                    self.answer=direction
                if max_min>last_max_min:
                    return max_min
            if max_min == float('-inf'):
                return self.evl(chessboard)


        if player_move_mode == 4:
            max_min=float('inf')
            for direction in range(4):
                next_chessboard=chessboard.copy()
                if next_chessboard.move(not self.isFirst,direction):
                    if self.isFirst:
                        self.currentRound+=1
                    new_value=self.move_search(next_chessboard,self.get_next_mode(player_move_mode),depth+1,max_min)
                    if self.isFirst:
                        self.currentRound-=1
                else:
                    new_value=float('inf')
                max_min = min(max_min, new_value)
                if max_min<=last_max_min:
                    return max_min
            if max_min == float('inf'):
                return self.evl(chessboard)

        return max_min


class Player3:
    def __init__(self, isFirst, array):
        self.isFirst = isFirst
        self.array = array
        self.currentRound = 0
        self.answer = None
        self.end_depth = 0
        self.round_mode = [1, 2, 3, 4]
        self.mode_offset = 2*isFirst-2
        self.answer = None

    def output(self, currentRound, board, mode):
        self.currentRound = currentRound
        if mode == '_position' or mode == '_direction':
            return None
        else:
            if mode == 'position':
                move_mode = 1
            else:
                move_mode = 3
            self.make_move_decision(
                board.copy(), move_mode, board.getTime(self.isFirst))
            return self.answer

    def make_move_decision(self, chessboard, player_move_mode, time_left):
        self.answer = None
        if time_left <= 0.1:
            self.end_depth = 6
        elif time_left <= 0.2:
            self.end_depth = 8
        elif 500 - self.currentRound <= 10:
            self.end_depth = 500 - self.currentRound
        elif self.currentRound <= 80:
            self.end_depth = 6
        elif self.currentRound <= 150:
            self.end_depth = 7
        elif self.currentRound <= 280:
            self.end_depth = 8
        elif self.currentRound <= 400:
            self.end_depth = 9
        else:
            self.end_depth = 10
        self.move_search(chessboard, player_move_mode, 0, float('inf'))

    def evl(self, board):
        val = 0
        my_sc = board.getScore(self.isFirst)
        your_sc = board.getScore(not self.isFirst)
        my_weight = 2.5
        your_weight = 2
        for me in my_sc:
            if len(my_sc) > 0 and me == my_sc[-1]:
                val += (my_weight**me)**2.5
            elif len(my_sc) > 1 and me == my_sc[-2]:
                val += (my_weight**me)**2
            elif len(my_sc) > 2 and me == my_sc[-3]:
                val += (my_weight**me)**1.6
            else:
                val += (my_weight**me)**1.2
        for you in your_sc:
            if len(your_sc) > 0 and you == your_sc[-1]:
                val -= (your_weight**you)**2.4
            elif len(your_sc) > 1 and you == your_sc[-2]:
                val -= (your_weight**you)**1.9
            elif len(your_sc) > 2 and you == your_sc[-3]:
                val -= (your_weight**you)**1.5
            else:
                val -= (your_weight**you)**1.1
        return val

    def move_search(self, chessboard, player_move_mode, depth, last_max_min):
        max_min = 0

        if depth == self.end_depth:
            return self.evl(chessboard)

        if player_move_mode == 1:
            max_min = float('-inf')
            pos = chessboard.getNext(self.isFirst, self.currentRound)
            if pos != ():
                next_chessboard = chessboard.copy()
                next_chessboard.add(self.isFirst, pos)
                new_value = self.move_search(
                    next_chessboard, self.round_mode[(player_move_mode+self.mode_offset) % 4], depth+1, max_min)
                if depth != 0:
                    max_min = max(max_min, new_value)
                elif (new_value > max_min):  # 首层决策
                    max_min = new_value
                    self.answer = pos
                if max_min > last_max_min:
                    return max_min
            else:
                for row in range(4):
                    for col in range(8):
                        pos = (row, col)
                        if chessboard.getValue(pos) == 0 and chessboard.getBelong(pos) != self.isFirst:
                            next_chessboard = chessboard.copy()
                            next_chessboard.add(not self.isFirst, pos)
                            new_value = self.move_search(
                                next_chessboard, self.round_mode[(player_move_mode+self.mode_offset) % 4], depth+1, max_min)
                        else:
                            new_value = float('-inf')
                        if depth != 0:
                            max_min = max(max_min, new_value)
                        elif (new_value > max_min):  # 首层决策
                            max_min = new_value
                            self.answer = pos
                        if max_min > last_max_min:
                            return max_min
            if max_min == float('-inf'):
                return self.evl(chessboard)

        if player_move_mode == 2:
            max_min = float('inf')
            pos = chessboard.getNext(not self.isFirst, self.currentRound)
            if pos != ():
                next_chessboard = chessboard.copy()
                next_chessboard.add(not self.isFirst, pos)
                new_value = self.move_search(
                    next_chessboard, self.round_mode[(player_move_mode+self.mode_offset) % 4], depth+1, max_min)
                max_min = min(max_min, new_value)
                if max_min <= last_max_min:
                    return max_min
            else:
                for row in range(4):
                    for col in range(8):
                        pos = (row, col)
                        if chessboard.getValue(pos) == 0 and chessboard.getBelong(pos) == self.isFirst:
                            next_chessboard = chessboard.copy()
                            next_chessboard.add(self.isFirst, pos)
                            new_value = self.move_search(
                                next_chessboard, self.round_mode[(player_move_mode+self.mode_offset) % 4], depth+1, max_min)
                        else:
                            new_value = float('inf')
                        max_min = min(max_min, new_value)
                        if max_min <= last_max_min:
                            return max_min
            if max_min == float('inf'):
                return self.evl(chessboard)
        if player_move_mode == 3:
            max_min = float('-inf')
            for direction in range(4):
                next_chessboard = chessboard.copy()
                if next_chessboard.move(self.isFirst, direction):
                    if not self.isFirst:
                        self.currentRound += 1
                    new_value = self.move_search(
                        next_chessboard, self.round_mode[(player_move_mode+self.mode_offset) % 4], depth+1, max_min)
                    if not self.isFirst:
                        self.currentRound -= 1
                else:
                    new_value = float('-inf')
                if depth != 0:
                    max_min = max(max_min, new_value)
                elif (new_value > max_min):
                    max_min = new_value
                    self.answer = direction
                if max_min > last_max_min:
                    return max_min
            if max_min == float('-inf'):
                return self.evl(chessboard)

        if player_move_mode == 4:
            max_min = float('inf')
            for direction in range(4):
                next_chessboard = chessboard.copy()
                if next_chessboard.move(not self.isFirst, direction):
                    if self.isFirst:
                        self.currentRound += 1
                    new_value = self.move_search(
                        next_chessboard, self.round_mode[(player_move_mode+self.mode_offset) % 4], depth+1, max_min)
                    if self.isFirst:
                        self.currentRound -= 1
                else:
                    new_value = float('inf')
                max_min = min(max_min, new_value)
                if max_min <= last_max_min:
                    return max_min
            if max_min == float('inf'):
                return self.evl(chessboard)

        return max_min


class Player4:
    def __init__(self, isFirst, array):
        self.isFirst = isFirst
        self.array = array
        self.currentRound = 0
        self.answer = None
        self.end_depth = 0
        self.mode_offset = 2*isFirst-1
        self.answer = None

    def output(self, currentRound, board, mode):
        self.currentRound = currentRound
        if mode == '_position' or mode == '_direction':
            return None
        else:
            if mode == 'position':
                move_mode = 0
            else:
                move_mode = 2
            self.make_move_decision(
                board.copy(), move_mode, board.getTime(self.isFirst))
            return self.answer

    def make_move_decision(self, chessboard, player_move_mode, time_left):
        self.answer = None
        if time_left <= 0.1:
            self.end_depth = 6
        elif time_left <= 0.2:
            self.end_depth = 8
        elif 500 - self.currentRound <= 10:
            self.end_depth = 500 - self.currentRound
        elif self.currentRound <= 80:
            self.end_depth = 6
        elif self.currentRound <= 150:
            self.end_depth = 7
        elif self.currentRound <= 280:
            self.end_depth = 8
        elif self.currentRound <= 400:
            self.end_depth = 9
        else:
            self.end_depth = 10
        self.move_search(chessboard, player_move_mode, 0, float('inf'))

    def evl(self, board):
        val = 0
        my_sc = board.getScore(self.isFirst)
        your_sc = board.getScore(not self.isFirst)
        my_weight = 2.5
        your_weight = 2
        for me in my_sc:
            if len(my_sc) > 0 and me == my_sc[-1]:
                val += (my_weight**me)**2.5
            elif len(my_sc) > 1 and me == my_sc[-2]:
                val += (my_weight**me)**2
            elif len(my_sc) > 2 and me == my_sc[-3]:
                val += (my_weight**me)**1.6
            else:
                val += (my_weight**me)**1.2
        for you in your_sc:
            if len(your_sc) > 0 and you == your_sc[-1]:
                val -= (your_weight**you)**2.4
            elif len(your_sc) > 1 and you == your_sc[-2]:
                val -= (your_weight**you)**1.9
            elif len(your_sc) > 2 and you == your_sc[-3]:
                val -= (your_weight**you)**1.5
            else:
                val -= (your_weight**you)**1.1
        return val

    def move_search(self, chessboard, player_move_mode, depth, last_max_min):
        max_min = 0

        if depth == self.end_depth:
            return self.evl(chessboard)

        if player_move_mode == 0:
            max_min = float('-inf')
            pos = chessboard.getNext(self.isFirst, self.currentRound)
            if pos != ():
                next_chessboard = chessboard.copy()
                next_chessboard.add(self.isFirst, pos)
                new_value = self.move_search(
                    next_chessboard, (player_move_mode+self.mode_offset) % 4, depth+1, max_min)
                if depth != 0:
                    max_min = max(max_min, new_value)
                elif (new_value > max_min):  # 首层决策
                    max_min = new_value
                    self.answer = pos
                if max_min > last_max_min:
                    return max_min
            else:
                for row in range(4):
                    for col in range(8):
                        pos = (row, col)
                        if chessboard.getValue(pos) == 0 and chessboard.getBelong(pos) != self.isFirst:
                            next_chessboard = chessboard.copy()
                            next_chessboard.add(not self.isFirst, pos)
                            new_value = self.move_search(
                                next_chessboard, (player_move_mode+self.mode_offset) % 4, depth+1, max_min)
                        else:
                            new_value = float('-inf')
                        if depth != 0:
                            max_min = max(max_min, new_value)
                        elif (new_value > max_min):  # 首层决策
                            max_min = new_value
                            self.answer = pos
                        if max_min > last_max_min:
                            return max_min
            if max_min == float('-inf'):
                return self.evl(chessboard)

        if player_move_mode == 1:
            max_min = float('inf')
            pos = chessboard.getNext(not self.isFirst, self.currentRound)
            if pos != ():
                next_chessboard = chessboard.copy()
                next_chessboard.add(not self.isFirst, pos)
                new_value = self.move_search(
                    next_chessboard, (player_move_mode+self.mode_offset) % 4, depth+1, max_min)
                max_min = min(max_min, new_value)
                if max_min <= last_max_min:
                    return max_min
            else:
                for row in range(4):
                    for col in range(8):
                        pos = (row, col)
                        if chessboard.getValue(pos) == 0 and chessboard.getBelong(pos) == self.isFirst:
                            next_chessboard = chessboard.copy()
                            next_chessboard.add(self.isFirst, pos)
                            new_value = self.move_search(
                                next_chessboard, (player_move_mode+self.mode_offset) % 4, depth+1, max_min)
                        else:
                            new_value = float('inf')
                        max_min = min(max_min, new_value)
                        if max_min <= last_max_min:
                            return max_min
            if max_min == float('inf'):
                return self.evl(chessboard)

        if player_move_mode == 2:
            max_min = float('-inf')
            for direction in range(4):
                next_chessboard = chessboard.copy()
                if next_chessboard.move(self.isFirst, direction):
                    if not self.isFirst:
                        self.currentRound += 1
                    new_value = self.move_search(
                        next_chessboard, (player_move_mode+self.mode_offset) % 4, depth+1, max_min)
                    if not self.isFirst:
                        self.currentRound -= 1
                else:
                    new_value = float('-inf')
                if depth != 0:
                    max_min = max(max_min, new_value)
                elif (new_value > max_min):
                    max_min = new_value
                    self.answer = direction
                if max_min > last_max_min:
                    return max_min
            if max_min == float('-inf'):
                return self.evl(chessboard)

        if player_move_mode == 3:
            max_min = float('inf')
            for direction in range(4):
                next_chessboard = chessboard.copy()
                if next_chessboard.move(not self.isFirst, direction):
                    if self.isFirst:
                        self.currentRound += 1
                    new_value = self.move_search(
                        next_chessboard, (player_move_mode+self.mode_offset) % 4, depth+1, max_min)
                    if self.isFirst:
                        self.currentRound -= 1
                else:
                    new_value = float('inf')
                max_min = min(max_min, new_value)
                if max_min <= last_max_min:
                    return max_min
            if max_min == float('inf'):
                return self.evl(chessboard)

        return max_min

array=[random.randint(0,1000000) for _ in range(5100)]

testplayer1=Player1(True,array)

testplayer2=Player1(False,array)

testplayer3=Player2(True,array)

testplayer4=Player2(False,array)

testplayer5=Player3(True,array)

testplayer6=Player3(False,array)

testplayer7=Player4(True,array)

testplayer8=Player4(False,array)


testlist=[1,1,1,2,1,3,1,4]+[1,3,1,2,1,1,1,0]+[1,2,1,3,1,4,1,5]+[1,5,1,2,1,3,1,2]+[0,1,0,3,0,5,0,1]+[0,3,0,5,0,1,0,1]+[0,2,0,3,0,1,0,4]+[0,1,0,3,0,4,0,2]

testplayers={1:testplayer1,2:testplayer2,3:testplayer3,4:testplayer4,5:testplayer5,6:testplayer6,7:testplayer7,8:testplayer8}

testboard=Chessboard(array)
#index=4*x+y
for i in range(32):
    if testlist[2*i+1]!=0:
        if testlist[2*i]:
            testboard.board[(i%4,i//4)]=Chessman(True, (i%4,i//4), testlist[2*i+1])
            testboard.belongs[True].append((i%4,i//4))
        else:
            testboard.board[(i%4,i//4)]=Chessman(False, (i%4,i//4), testlist[2*i+1])
            testboard.belongs[False].append((i%4,i//4))

def my_search(n):
    if n==1 or n==2:
        for i in range(50):
            testplayers[n].make_move_decision(testboard,"my_direction")
            testplayers[n].currentRound+=10
    elif n<7:
        for i in range(50):
            testplayers[n].make_move_decision(testboard,3,5.0-0.1*i)
            testplayers[n].currentRound+=10
    else:
        for i in range(50):
            testplayers[n].make_move_decision(testboard,2,5.0-0.1*i)
            testplayers[n].currentRound+=10

print("-------test-------")
print("move_mode=my_direction or 3")
print("self.currentRound in range(0,500,10),time_left in range(5.0,0.0,-0.1)")

mstime1=timeit.Timer("my_search(1)","from __main__ import Player1,Player2,Chessboard,Chessman,array,testplayers,testboard,my_search")

mst1=mstime1.timeit(number=1)
print("my search time used totally(lfc version 1,first hand):",mst1)

mstime2=timeit.Timer("my_search(2)","from __main__ import Player1,Player2,Chessboard,Chessman,array,testplayers,testboard,my_search")

mst2=mstime2.timeit(number=1)
print("my search time used totally(lfc version 1,second hand):",mst2)

mstime3=timeit.Timer("my_search(3)","from __main__ import Player1,Player2,Chessboard,Chessman,array,testplayers,testboard,my_search")

mst3=mstime3.timeit(number=1)
print("my search time used totally(lfc version 2,first hand):",mst3)

mstime4=timeit.Timer("my_search(4)","from __main__ import Player1,Player2,Chessboard,Chessman,array,testplayers,testboard,my_search")

mst4=mstime4.timeit(number=1)
print("my search time used totally(lfc version 2,second hand):",mst4)

mstime5=timeit.Timer("my_search(5)","from __main__ import Player1,Player2,Chessboard,Chessman,array,testplayers,testboard,my_search")

mst5=mstime5.timeit(number=1)
print("my search time used totally(ljz version 1,first hand):",mst5)

mstime6=timeit.Timer("my_search(6)","from __main__ import Player1,Player2,Chessboard,Chessman,array,testplayers,testboard,my_search")

mst6=mstime6.timeit(number=1)
print("my search time used totally(ljz version 1,second hand):",mst6)

mstime7=timeit.Timer("my_search(7)","from __main__ import Player1,Player2,Chessboard,Chessman,array,testplayers,testboard,my_search")

mst7=mstime7.timeit(number=1)
print("my search time used totally(ljz version 2,first hand):",mst7)

mstime8=timeit.Timer("my_search(8)","from __main__ import Player1,Player2,Chessboard,Chessman,array,testplayers,testboard,my_search")

mst8=mstime8.timeit(number=1)
print("my search time used totally(ljz version 2,second hand):",mst8)

