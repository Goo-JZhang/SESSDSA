class Player:
    def __init__(self, isFirst, array):
        self.isFirst=isFirst
        self.array=array
        self.currentRound=0
        self.round_mode=self.set_round_mode()
        self.answer=None
        self.end_depth=0

    def set_round_mode(self):
        if self.isFirst is True:
            return ['my_position','your_position','my_direction','your_direction']
        else:
            return ['my_position','your_direction','my_direction','your_postion']


    def get_next_mode(self,current_mode):
        return self.round_mode[(self.round_mode.index(current_mode)+1)%4]


    def output(self, currentRound, board, mode):
        self.currentRound=currentRound


    def switch(self,my_chessboard,direction,chessman):
        '''
        传入一个bytearray棋盘并返回滑动后的bytearray棋盘
        '''
        pass


    def get_available(self,my_chessboard,player_move_mode):
        '''
        对一个给定的bytearray棋盘获取可以落子的所有位置，包括己方地盘上的位置和对方底盘上的位置
        player_move_mode可为己方或对方
        将棋盘上的位置按
        0 4 8 ...
        1 5 9 ...
        2 6 10 ...
        3 8 12 ...
        排序，返回一个包含所有可能落子位置的int列表
        '''
        available_list=[]
        null_list=[]
        if (player_move_mode is 'my_position' and self.isFirst) or (player_move_mode is 'your_position' and not self.isFirst):
            #先手方
            for i in range(4):
                for j in range(4):
                    index=2*i+8*j+1 #找己方空格，按先行后列的顺序
                    if my_chessboard[index] is 0:
                        null_list.append((index-1)/2) #空格加入null_list记录，编号按照先列后行的顺序
            if null_list is not None:
                available_list.append(null_list[self.array[self.currentRound]%len(null_list)])
            for i in range(16,32):
                index=2*i+1
                if my_chessboard[index] is 0:
                    available_list.append(i)
            return available_list
        else:
            #后手方
            for i in range(4):
                for j in range(4,8):
                    index=2*i+8*j+1 #找对方空格，按先行后列的顺序
                    if my_chessboard[index] is 0:
                        null_list.append((index-1)/2) #空格加入null_list记录，编号按照先列后行的顺序
            if null_list is not None:
                if self.isFirst is True: #非先手需转置列表
                    null_list.reverse()
                available_list.append(null_list[self.array[self.currentRound]%len(null_list)])
            for i in range(16):
                index=2*i+1
                if my_chessboard[index] is 0:
                    available_list.append(i)
            return available_list


    def move_search(self,my_chessboard,player_move_mode,depth,last_max_min):
        '''
        搜索函数
        传入目前的棋盘的bytearray形式my_chessboard, 目前要执行的走棋类型move_mode, 搜索层数depth, 上一级的max_min
        函数本身只会返回局面的value值
        搜索判断的结果存放在self.answer中
        初始调用depth为0, last_max_min float('inf')
        '''

        if depth == self.end_depth:
            #到底获取估值函数
            if player_move_mode in ('my_position', 'your_position'):
                return self.Get_Evl(my_chessboard,0)
            else:
                return self.Get_Evl(my_chessboard,1)

        if player_move_mode is 'my_position':
            max_min=float('-inf')
            available_list=self.get_available(my_chessboard,player_move_mode)
            for place in available_list:
                #copy一个来传递就不用回溯棋盘了...
                next_chessboard=my_chessboard.copy()
                if self.isFirst: #先手 左边为己方
                    if place < 16:
                        next_chessboard[2*place]=0 #0己方1对方
                        next_chessboard[2*place+1]=1 #放在己方的2
                    else:
                        next_chessboard[2*place]=1
                        next_chessboard[2*place+1]=1 #放在对方的2
                else: #后手 右边为己方
                    if place>=16:
                        next_chessboard[2*place]=0
                        next_chessboard[2*place+1]=1 #放在己方的2
                    else:
                        next_chessboard[2*place]=1
                        next_chessboard[2*place+1]=1 #放在对方的2
                self.currentRound+=1
                new_value=self.move_search(next_chessboard,self.get_next_mode(player_move_mode),depth+1,max_min) #recurse
                self.currentRound-=1 #backtrack
                if not depth:  
                    max_min=max(max_min,new_value)
                elif (new_value>max_min): #首层决策
                    max_min=new_value
                    col=place//4
                    row=place%4
                    self.answer=(row,col)
                if max_min>last_max_min:
                    return max_min
            if max_min == float('-inf'):
                return self.Get_Evl(my_chessboard,0)


        if player_move_mode is 'your_position':
            max_min=float('inf')
            available_list=self.get_available(my_chessboard,player_move_mode)
            for place in available_list:
                #copy一个来传递就不用回溯棋盘了...
                next_chessboard=my_chessboard.copy()
                if self.isFirst: #对方为后手 右边为限制域
                    if place >= 16:
                        next_chessboard[2*place]=1 #0己方1对方
                        next_chessboard[2*place+1]=1 #对方在自己的右边下2
                    else:
                        next_chessboard[2*place]=0
                        next_chessboard[2*place+1]=1 
                else: #对方为先手
                    if place<16:
                        next_chessboard[2*place]=1
                        next_chessboard[2*place+1]=1 
                    else:
                        next_chessboard[2*place]=0
                        next_chessboard[2*place+1]=1 #放在对方的2
                self.currentRound+=1
                new_value=self.move_search(next_chessboard,self.get_next_mode(player_move_mode),depth+1,max_min) #recurse
                self.currentRound-=1 #backtrack
                max_min=min(max_min,new_value)
                if max_min<=last_max_min:
                    return max_min
            if max_min==float('inf'):
                return self.Get_Evl(my_chessboard,0)

        if player_move_mode is 'my_direction':
            max_min=float('-inf')
            for direction in range(4): #0~3代表上下左右
                next_chessboard=my_chessboard.copy()
                next_chessboard=self.switch(next_chessboard,direction,self.isFirst)#调用滑动函数
                self.currentRound+=1
                new_value=self.move_search(next_chessboard,self.get_next_mode(player_move_mode),depth+1,max_min) #recurse
                self.currentRound-=1 #backtrack
                if not depth:  
                    max_min=max(max_min,new_value)
                elif (new_value>max_min):
                    max_min=new_value
                    self.answer=direction
                if max_min>last_max_min:
                    return max_min
            if max_min == float('-inf'):
                return self.Get_Evl(my_chessboard,1)

        if player_move_mode is 'your_direction':
            max_min=float('inf')
            for direction in range(4): #0~3代表上下左右
                next_chessboard=my_chessboard.copy()
                next_chessboard=self.switch(next_chessboard,direction,not self.isFirst) #调用滑动函数
                self.currentRound+=1
                new_value=self.move_search(next_chessboard,self.get_next_mode(player_move_mode),depth+1,max_min) #recurse
                self.currentRound-=1 #backtrack
                max_min=min(max_min,new_value)
                if max_min<=last_max_min:
                    return max_min
            if max_min==float('inf'):
                return self.Get_Evl(my_chessboard,1)

        return max_min


    def make_move_decision(self,chessboard,player_move_mode,time_remain):
        #后续再调
        '''
        调用此函数以获得走棋策略
        传入棋盘、己方走棋模式、剩余时间
        函数本身无返回值，结果请读入self.answer
        '''
        self.answer=None
        if time_remain/(200-self.currentRound)>0.025:
            self.end_depth=8
        else:
            self.end_depth=5
        self.move_search(chessboard,player_move_mode,0,float('inf'))


'''
05.23
更新了第162、180行的传入参数
添加了make_move_decision的注释
更正了第201行
'''