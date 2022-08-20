
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
        self.where=isFirst   # 为我方位置，1说明我方在左，0说明我方在右,非调试状态应该取1
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
        '''
        switch 需要传入参数：棋盘 ； 移动方向 ； 移动方是否为先手
        返回移动后的棋盘
        '''
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
        return changedarray
        #return changeformat(changedarray,self.ROWS * self.COLLUMS)
    # 返回时用到建霖的规范
         
 
    def move_row(self,mybyte:bytearray(),side: str,chessman : bool) -> bytearray():
            '''
            可以移动一行棋子 ， 参数是棋盘，side用来判断是否为我方领地 ，以及移动方是否为先手
            '''
            protectnum = []
            boundary = 0x10
            def move_one(i,mybyte,side):
                isFriend = mybyte[i] // boundary
                if chessman != (isFriend==0):
                    return
                #if isFriend != 0:
                #    return
                while i > 0:
                    if mybyte[i] % boundary == 0: 
                        #print(i,0)
                        return
                    if mybyte[i-1]/boundary == isFriend:  #  这是我方空格
                        #print(i,1)
                        mybyte[i-1],mybyte[i]=mybyte[i],mybyte[i-1]
                        if (side == 'left' and i >= self.COLLUMS//2) or\
                           (side == 'right' and i < self.COLLUMS//2):
                            mybyte[i] = (1-isFriend) * boundary
                        i-=1
                    elif mybyte[i-1]%boundary == mybyte[i]%boundary and i-1 not in protectnum:#  这是敌方或我方同量棋子
                        #print(i,2)
                        mybyte[i-1],mybyte[i]=mybyte[i]+1,isFriend * boundary
                        if side == 'change'or (side == 'left' and i >= self.COLLUMS//2) or \
                           (side == 'right' and i < self.COLLUMS//2):
                                #我方在左与我方在右
                            mybyte[i] = (1-isFriend) * boundary
                        protectnum.append(i-1)
                        return
                    elif mybyte[i-1]%boundary != mybyte[i]%boundary or mybyte[i-1]//boundary != isFriend\
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




test1=bytearray(           [1,0,0,0,128,128,128,128,
                            1,0,0,130,128,128,128,128,
                            1,0,0,2,128,128,128,128,
                            1,0,0,0,128,129,128,128 ]
                            [i*8+j] for j in range(8) for i in range(4))
test2 = bytearray(         [0,0,1,1,128,128,128,128,
                            0,1,0,1,128,128,128,128,
                            0,0,0,1,129,128,128,128,
                            0,1,0,0,129,128,128,128 ]
                            [i*8+j] for j in range(8) for i in range(4))
test3 = bytearray(         [0,1,1,1,128,128,128,128,
                            1,1,1,1,128,128,128,128,
                            0,0,0,1,129,130,128,128,
                            0,2,1,1,128,128,128,128 ]
                            [i*8+j] for j in range(8) for i in range(4))
test4 = bytearray(         [0,0,0,0,1,128,128,128,
                            0,0,0,0,128,1,128,128,
                            0,0,0,0,129,1,128,128,
                            0,0,0,129,1,128,128,128 ]
                            [i*8+j] for j in range(8) for i in range(4))


