class Player():
    def __init__(self, isFirst, array) -> None:
        '''
        self: Player, isFirst: bool, array: List[int]
        AI初始化
        '''
        self.ROWS = 4
        self.COLLUMS = 8
        self.isFirst=isFirst
        self.array=array
        self.where=1   # 为我方位置，1说明我方在左，0说明我方在右,非调试状态应该取1
        self.val_matrixs=[]
        self.used_matrix=[]
        self.currentRound = 0
        '''
        val_matrixs内为不同的val_m,是4*4的二维列表，设计自理
        used_matrix是正在使用的静态估值矩阵
        '''
    def output(self, currentRound, board, mode):
        '''
        self: Player, currentRound: int, board: Chessboard, mode: str) -> Union[Tuple[int, int], int]
        输出函数
        '''
        myboard = chessborad2mine(currentRound,board)
        self.currentRound = currentRound
        if self.currentRound <= 10:
            decision=self.beginfun(myboard, currentRound, mode)
        elif timeup(board.getTime()):
            decision= self.search(myboard, currentRound, board.getTime(), mode)
        else:
            decision = self.search(myboard, currentRound, board.getTime(), mode) # 这里的5是临时占位的,表示搜索深度
        return decision
        
        #最后把拉闸玩意丢进去就好
        pass
 
    def chessborad2mine(self,currentRound,board):
        if board.getBlong((0,0))!=self.isFirst and currentRound==1:
            self.where=0
        #以上为修改方位的，只在第一局使用
        '''
        return bytearray
        返回一个mychessboard=bytearray()对象，长为64
        偶数位为棋子归属先后手方，先手为True，后手为False
        奇数位为棋子大小1，2，3，4...，若棋子大小为0，说明该位置无棋子，棋子归属=棋盘归属
        第一行为mychessboard[0~15]，第二行为16~31...
        '''
        pass
     
    def get_jingtai(self,my_chessboard: bytearray()):
        '''
        返回静态期望
        注意己方位置和己方属于先手后哪一方
        '''
        pass
     
    def get_dongtai(self,my_chessboard: bytearray()):
        '''
        返回动态期望,比如连续性之类的
        初步考虑己方棋子连续性和边界连续性?
        '''
        pass
 
    def beginfun(self ,my_chessboard: bytearray() ,currentRound: int ,mode):
        '''
        开局策略 'kaiju'
        '''
        pass
     
    def search(self,my_borad: bytearray(),currentRound: int,depth_or_time ,mode):
        '''
        bzd深搜还是广搜，看情况用depth或者time 'sousuo'
        '''
        pass
 
 
    def switch(self,my_board:bytearray(),direction: int,chessman : bool) ->bytearray():
        def changeformat(mybls:bytearray(), lenth) -> bytearray():
        # 格式间的相互转换
            if len(mybls)==self.ROWS*self.COLLUMS==lenth:
                changedarray = bytearray(mybls[i + j*self.ROWS +m*lenth//2]<0x80 if n==0 else 
                                    mybls[i + j*self.ROWS +m*lenth//2]%0x80
                                    for m in [0,1] for i in range(self.ROWS)
                                    for j in range(self.COLLUMS//2) for n in [0,1])
            elif len(mybls) == self.ROWS*self.COLLUMS*2 == lenth:
                changedarray = bytearray(0x80*(1-mybls[ 2 * (i + self.COLLUMS//2*j) + m * lenth//2])
                    + mybls[1 + 2 * (i + self.COLLUMS//2*j) + m * lenth//2]
                    for m in [0,1] for i in range(self.COLLUMS//2) for j in range(self.ROWS))
            else: changedarray = mybls
            return changedarray
        my_board = changeformat(my_board, self.COLLUMS * self.ROWS * 2)
        # 这时棋盘转化为函数中的调用形式
        
        
        #  调试
        self.where = 1 if self.isFirst == (my_board[0]<0x80) else 0
        print('self.isFirst:',self.isFirst,'; self.where:',['右','左'][self.where],
              '; chessman:',chessman,'; move_direction',['上','下','左','右'][direction],'\n')
        #  0，8代表先后手
        #  调试结束
        self._where = self.where if chessman == self.isFirst else 1-self.where
        movedict = {
            0:self.move_up,
            1:self.move_down,
            2:self.move_left,
            3:self.move_right
            }
        if direction in [0,1]:   # 0,1,2,3  ->  上下左右
            lst = [my_board[i*self.ROWS:(i+1)*self.ROWS] for i in range(self.COLLUMS)]
            lst = movedict[direction](lst,chessman)
            #for i in range(len(lst)):
            #    print(lst[i])
            changedarray = bytearray(lst[i][j] for i in range(self.COLLUMS)\
               for j in range(self.ROWS))
        else:
            lst = [my_board[i::self.ROWS] for i in range(self.ROWS)]
            lst = movedict[direction](lst,chessman)
            #for i in range(len(lst)):
            #    print(lst[i])
            changedarray = bytearray(lst[i][j] for j in range(self.COLLUMS)\
                for i in range(self.ROWS))
        #return changedarray
        return changeformat(changedarray,self.ROWS * self.COLLUMS)
    # 返回时用到建霖的规范
         
 
    def move_row(self,mybyte:bytearray(),side: str,chessman : bool) -> bytearray():
            protectnum = []
            def move_one(i,mybyte,side):
                isFriend = mybyte[i] // 0x80
                if chessman != (isFriend==0):
                    return
                #if isFriend != 0:
                #    return
                while i > 0:
                    if mybyte[i]/0x80 == isFriend: 
                        #print(i,0)
                        return
                    if mybyte[i-1]/0x80 == isFriend:  #  这是我方空格
                        #print(i,1)
                        mybyte[i-1],mybyte[i]=mybyte[i],mybyte[i-1]
                        if (side == 'left' and i >= self.COLLUMS//2) or\
                           (side == 'right' and i < self.COLLUMS//2):
                            mybyte[i] = (1-isFriend) * 0x80
                        i-=1
                    elif mybyte[i-1]%0x80 == mybyte[i]%0x80 and i-1 not in protectnum:#  这是敌方或我方同量棋子
                        #print(i,2)
                        mybyte[i-1],mybyte[i]=mybyte[i]+1,isFriend * 0x80
                        if side == 'change'or (side == 'left' and i >= self.COLLUMS//2) or \
                           (side == 'right' and i < self.COLLUMS//2):
                                #我方在左与我方在右
                            mybyte[i] = (1-isFriend) * 0x80
                        protectnum.append(i-1)
                        return
                    elif mybyte[i-1]%0x80 != mybyte[i]%0x80 or mybyte[i-1]//0x80 != isFriend\
                       or i-1 in protectnum:#  不能前进或受保护
                        return
            for i in range(1,len(mybyte)):
                move_one(i,mybyte,side)
            return mybyte
             
 
    def move_up(self,lst:[bytearray(),...],chessman : bool) -> [bytearray(),...]:
        for i in range(len(lst)):
            if self._where == 1 and i < self.COLLUMS//2 or\
               self._where == 0 and i >= self.COLLUMS//2:  #  1代表我方在左
                lst[i] = self.move_row(lst[i],'',chessman)
            else:
                lst[i] = self.move_row(lst[i],'change',chessman)
        return lst
 
    def move_down(self,lst:[bytearray(),...],chessman : bool) -> [bytearray(),...]:
        for i in range(len(lst)):
            if self._where == 1 and i < self.COLLUMS//2 or\
               self._where == 0 and i >= self.COLLUMS//2:  #  1代表移动方在左
                lst[i].reverse()
                lst[i] = self.move_row(lst[i],'',chessman)
                lst[i].reverse()
            else:
                lst[i].reverse()
                lst[i] = self.move_row(lst[i],'change',chessman)
                lst[i].reverse()
        return lst
 
    def move_left(self,lst:[bytearray(),...],chessman : bool) -> [bytearray(),...]:
        if self._where == 1:   # 移动方在左
            for i in range(len(lst)):
                lst[i] = self.move_row(lst[i],'left',chessman)
        else:
            for i in range(len(lst)):
                lst[i] = self.move_row(lst[i],'right',chessman)
        return lst
 
    def move_right(self,lst:[bytearray(),...],chessman : bool) -> [bytearray(),...]:
        if self._where == 0:   # 倒置后移动方在左
            for i in range(len(lst)):
                lst[i].reverse()
                lst[i] = self.move_row(lst[i],'left',chessman)
                lst[i].reverse()
        else:
            for i in range(len(lst)):
                lst[i].reverse()
                lst[i] = self.move_row(lst[i],'right',chessman)
                lst[i].reverse()
        return lst




test1=bytearray(           [1,0,0,0,0x80,128,128,128,
                            1,0,0,130,128,128,128,128,
                            1,0,0,2,128,128,128,128,
                            1,0,0,0,128,129,128,128 ]
                            [i*8+j] for j in range(8) for i in range(4))
test2 = bytearray(         [0,0,1,1,0x80,128,128,128,
                            0,1,0,1,128,128,128,128,
                            0,0,0,1,129,128,128,128,
                            0,1,0,0,129,128,128,128 ]
                            [i*8+j] for j in range(8) for i in range(4))
test3 = bytearray(         [0,1,1,1,0x80,128,128,128,
                            1,1,1,1,128,128,128,128,
                            0,0,0,1,129,130,128,128,
                            0,2,1,1,128,128,128,128 ]
                            [i*8+j] for j in range(8) for i in range(4))
test4 = bytearray(         [0,0,0,0,1,128,128,128,
                            0,0,0,0,128,1,128,128,
                            0,0,0,0,129,1,128,128,
                            0,0,0,129,1,128,128,128 ]
                            [i*8+j] for j in range(8) for i in range(4))

'''
print('首位是0表示先手棋子,首位是8表示后手棋子\n')

outcome = test4
outcome =  [outcome[i::4] for i in range(4)]
for member in outcome:
    print(member)

print()

outcome = Player(False , 1).switch(test4,2,True)
#outcome =  [outcome[i::4] for i in range(4)]

outcome = [bytearray(outcome[i + 8 *j + 32 * m] for m in range(2) for i in range(8)) for j in range(4) ]
for member in outcome:
    print(member)

'''
def pre64(alist):
    for y in range(4):
        s=''
        for x in range(4):
            if alist[8*y+2*x]==1:
                s+='+'
            else:
                s+='-'
            s+=str(alist[8*y+2*x+1])+' '
        for x in range(4):
            if alist[8*y+2*x+32]==1:
                s+='+'
            else:
                s+='-'
            s+=str(alist[8*y+2*x+33])+' '
        print(s)

def pre32(alist):
    for y in range(4):
        s=''
        for x in range(8):
            if alist[8*y+x]<128:
                s=s+'+'+str(alist[8*y+x])+' '
            else:
                s=s+'-'+str(alist[8*y+x]-128)+' '
        print(s)

p=Player(True,1)
alist=[1,1,1,2,1,3,1,4,1,1,1,2,1,3,1,1,1,1,1,2,1,3,1,4,1,1,1,2,1,3,1,4]+[0,1,0,2,0,3,0,4,1,1,1,2,1,2,0,3,0,1,0,2,0,3,0,4,0,1,0,2,0,3,0,4]
b=bytearray(alist)
pre64(b)
c=p.switch(b,1,0)
pre64(c)