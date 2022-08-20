Evl_Mat_1_1 = [16, 15, 12, 4,
               14, 13, 11, 3,
               10, 9, 8, 2,
               7, 6, 5, 1]  # SPD
Evl_Mat_1_2 = [4, 3, 2, 1,
               12, 11, 8, 5,
               15, 13, 9, 6,
               16, 14, 10, 7]  # SPD
Evl_Mat_1_3 = [1, 5, 6, 7,
               2, 8, 9, 10,
               3, 11, 13, 14,
               4, 12, 15, 16]  # SPD
Evl_Mat_1_4 = [7, 10, 14, 16,
               6, 9, 13, 15,
               5, 8, 11, 12,
               1, 2, 3, 4]  # SPD
Evl_Mat_1 = [Evl_Mat_1_1, Evl_Mat_1_2,
             Evl_Mat_1_3, Evl_Mat_1_4]
Evl_Mat_1_Trans_1 = [16, 14, 10, 7,
                     15, 13, 9, 6,
                     12, 11, 8, 5,
                     4, 3, 2, 1]  # SPD_Transpose
Evl_Mat_1_Trans_2 = [7, 6, 5, 1,
                     10, 9, 8, 2,
                     14, 13, 11, 3,
                     16, 15, 12, 4]  # SPD_Transpose
Evl_Mat_1_Trans_3 = [1, 2, 3, 4,
                     5, 8, 11, 12,
                     6, 9, 13, 15,
                     7, 10, 14, 16]  # SPD_Transpose
Evl_Mat_1_Trans_4 = [4, 12, 15, 16,
                     3, 11, 13, 14,
                     2, 8, 9, 10,
                     1, 5, 6, 7]  # SPD_Transpose
Evl_Mat_1_Trans = [Evl_Mat_1_Trans_1, Evl_Mat_1_Trans_2,
                   Evl_Mat_1_Trans_3, Evl_Mat_1_Trans_4]
Evl_Mat_2_1 = [16, 15, 14, 4,
               13, 12, 11, 3,
               10, 9, 8, 2,
               7, 6, 5, 1]  # ZSL
Evl_Mat_2_2 = [4, 3, 2, 1,
               14, 11, 8, 5,
               15, 12, 9, 6,
               16, 13, 10, 7]  # ZSL
Evl_Mat_2_3 = [1, 5, 6, 7,
               2, 8, 9, 10,
               3, 11, 12, 13,
               4, 14, 15, 16]  # ZSL
Evl_Mat_2_4 = [7, 10, 13, 16,
               6, 9, 12, 15,
               5, 8, 11, 14,
               1, 2, 3, 4]  # ZSL
Evl_Mat_2 = [Evl_Mat_2_1, Evl_Mat_2_2,
             Evl_Mat_2_3, Evl_Mat_2_4]
Evl_Mat_2_Trans_1 = [16, 13, 10, 7,
                     15, 12, 9, 6,
                     14, 11, 8, 5,
                     4, 3, 2, 1]  # ZSL_Transpose
Evl_Mat_2_Trans_2 = [7, 6, 5, 1,
                     10, 9, 8, 2,
                     13, 12, 11, 3,
                     16, 15, 14, 4]  # ZSL_Transpose
Evl_Mat_2_Trans_3 = [1, 2, 3, 4,
                     5, 8, 11, 14,
                     6, 9, 12, 15,
                     7, 10, 13, 16]  # ZSL_Transpose
Evl_Mat_2_Trans_4 = [4, 14, 15, 16,
                     3, 11, 12, 13,
                     2, 8, 9, 10,
                     1, 5, 6, 7]  # ZSL_Transpose
Evl_Mat_2_Trans = [Evl_Mat_2_Trans_1, Evl_Mat_2_Trans_2,
                   Evl_Mat_2_Trans_3, Evl_Mat_2_Trans_4]
Evl_Mat_3_R = [1, 8, 9, 16,
               2, 7, 10, 15,
               3, 6, 11, 14,
               4, 5, 12, 13]  # S_shape
Evl_Mat_3_R_Trans = [4, 5, 12, 13,
                     3, 6, 11, 14,
                     2, 7, 10, 15,
                     1, 8, 9, 16]  # S_shape_Transpose
Evl_Mat_3_L = [13, 12, 5, 4,
               14, 11, 6, 3,
               15, 10, 7, 2,
               16, 9, 8, 1]  # S_shape
Evl_Mat_3_L_Trans = [16, 9, 8, 1,
                     15, 10, 7, 2,
                     14, 11, 6, 3,
                     13, 12, 5, 4]  # S_shape_Transpose
Evl_Mat_3 = [Evl_Mat_3_R, Evl_Mat_3_L]
Evl_Mat_3_Trans = [Evl_Mat_3_R_Trans, Evl_Mat_3_L_Trans]


def Evl(my_chessboard, L_atk=0, R_atk=0, v1=1.0, v2=1.0, v3=1.0) -> float:
    '''
    棋盘评估结果以先手方为正，后手方为负，side默认为1（代表先手），取-1可反号；
    L_atk选择先手方是否使用进攻策略，R_atk选择后手方是否使用进攻策略，两者默认为0；
    参数 v1 v2 v3 分别对应 SPD ZSL S_Shape 的权重（float）；
    '''
    if (len(my_chessboard) != 64):
        raise ValueError
    else:
        evl = 0.0  # 评估值
        evl_1 = 0.0
        evl_2 = 0.0
        for i in range(4):
            tevl_1 = 0.0  # temp1
            for j in range(16):  # 对左半边评估
                if(my_chessboard[2*j] == 1):
                    tevl_1 += (float(int(my_chessboard[2*j+1])) *
                               ((Evl_Mat_1[i][j] + Evl_Mat_1_Trans[i][j]) * v1 +
                                (Evl_Mat_2[i][j] + Evl_Mat_2_Trans[i][j]) * v2 +
                                (Evl_Mat_3[1-L_atk][j] + Evl_Mat_3_Trans[1-L_atk][j]) * v3))
                elif(my_chessboard[2*j] == 0):
                    tevl_1 -= (float(int(my_chessboard[2*j+1])) *
                               ((Evl_Mat_1[i][j] + Evl_Mat_1_Trans[i][j]) * v1 +
                                (Evl_Mat_2[i][j] + Evl_Mat_2_Trans[i][j]) * v2 +
                                (Evl_Mat_3[1-L_atk][j] + Evl_Mat_3_Trans[1-L_atk][j]) * v3))
                else:
                    raise ValueError
            evl_1 = tevl_1 if (i == 0 or tevl_1 > evl_1) else evl_1  # 四个方向取最大
        for i in range(4):
            tevl_2 = 0.0  # temp2
            for j in range(16):  # 对右半边评估
                if(my_chessboard[2*j] == 0):
                    tevl_2 += (float(int(my_chessboard[2*j+33])) *
                               ((Evl_Mat_1[i][j] + Evl_Mat_1_Trans[i][j]) * v1 +
                                (Evl_Mat_2[i][j] + Evl_Mat_2_Trans[i][j]) * v2 +
                                (Evl_Mat_3[R_atk][j] + Evl_Mat_3_Trans[R_atk][j]) * v3))
                elif(my_chessboard[2*j] == 1):
                    tevl_2 -= (float(int(my_chessboard[2*j+33])) *
                               ((Evl_Mat_1[i][j] + Evl_Mat_1_Trans[i][j]) * v1 +
                                (Evl_Mat_2[i][j] + Evl_Mat_2_Trans[i][j]) * v2 +
                                (Evl_Mat_3[R_atk][j] + Evl_Mat_3_Trans[R_atk][j]) * v3))
                else:
                    raise ValueError
            evl_2 = tevl_2 if (i == 0 or tevl_2 > evl_2) else evl_2  # 四个方向取最大
        evl = evl_1 - evl_2
        return evl


def Smooth_Evl(my_chessboard) -> float:
    """
    光滑度评估函数，光滑度越高越可能重合；
    评估结果以先手方更光滑为正，后手方更光滑为负，先后手同样光滑取0；
    """
    if (len(my_chessboard) != 64):
        raise ValueError
    else:
        smt = 0.0
        for i in range(4):
            for j in range(3):
                smt -= abs(int(my_chessboard[8*i+2*j+1]) -
                           int(my_chessboard[8*i+2*j+3]))
                smt -= abs(int(my_chessboard[8*j+2*i+1]) -
                           int(my_chessboard[8*j+2*i+9]))
                smt += abs(int(my_chessboard[8*i+2*j+33]) -
                           int(my_chessboard[8*i+2*j+35]))
                smt += abs(int(my_chessboard[8*j+2*i+33]) -
                           int(my_chessboard[8*j+2*i+41]))
        return smt


def Free_Evl(my_chessboard) -> float:
    """
    空余空间评估函数，越多越好；
    评估结果以先手方为正，后手方为负；
    """
    if (len(my_chessboard) != 64):
        raise ValueError
    else:
        free = 0.0
        for i in range(32):
            if (my_chessboard[2*i+1] == 0):
                if (my_chessboard[2*i] == 1 and i < 16):
                    free += 1.0
                elif (my_chessboard[2*i] == 0 and i >= 16):
                    free -= 1.0
                else:
                    raise ValueError
        return free


def Threat_Evl(my_chessboard, state, side=1, v1=1.0, v2=1.0, v3=1.0) -> float:
    '''
    棋盘评估结果以先手方为正，数值越大则先手方对于后手方的威胁度越大；
    考虑边界上相邻的两个位置，参数 v1 v2 v3 分别对应 属于同一方 属于不同方且相等 属于不同方且不等 的权重（float）；
    ###小心送人头的情况###
    '''
    if (len(my_chessboard) != 64):
        raise ValueError
    else:
        threat = 0.0
        for i in range(12, 16):
            if (my_chessboard[2*i] == 1 and my_chessboard[2*i+8] == 1):
                threat += v1 * (float(int(my_chessboard[2*i+1])) +
                                float(int(my_chessboard[2*i+9])))
            elif (my_chessboard[2*i] == 0 and my_chessboard[2*i+8] == 0):
                threat -= v1 * (float(int(my_chessboard[2*i+1])) +
                                float(int(my_chessboard[2*i+9])))
            elif (my_chessboard[2*i+1] == my_chessboard[2*i+9]):
                # 可能需要乘以 float(my_chessboard[2*i] - my_chessboard[2*i+8])
                threat += (v2 * float(2*int(my_chessboard[2*i+1])) if (not state)
                           else (-1) * v2 * side * float(2*int(my_chessboard[2*i+1])))
            else:
                threat += v3 * (float(2*(my_chessboard[2*i]-0.5) * int(my_chessboard[2*i+1])) +
                                float(2*(my_chessboard[2*i+8]-0.5) * int(my_chessboard[2*i+9])))
        return threat


def Get_Evl(my_chessboard, state, side=1, L_atk=0, R_atk=0, v1=1.0, v2=1.0, v3=1.0, v4=1.0) -> float:
    '''
    棋盘评估结果以先手方为正，后手方为负;
    state取0或1，0代表落子阶段，1代表合并阶段，side默认为1（代表评估先手），取-1可使返回值反号；
    L_atk选择先手方是否使用进攻策略，R_atk选择后手方是否使用进攻策略，两者默认为0；
    参数 v1 v2 v3 v4 分别对应 Evl Smooth_Evl Free_Evl Threat_Evl 的权重（float）；
    '''
    return float(side *
                 (v1 * Evl(my_chessboard, L_atk, R_atk) +
                  v2 * Smooth_Evl(my_chessboard) +
                  v3 * Free_Evl(my_chessboard) +
                  v4 * Threat_Evl(my_chessboard, state, side)))


class Player():
    def __init__(self, isFirst, array):
        '''
        self: Player, isFirst: bool, array: List[int]
        AI初始化
        '''
        self.isFirst=isFirst
        self.array=array
        self.currentRound=0
        self.round_mode=self.set_round_mode()
        self.answer=None
        self.end_depth=5
        self.ROWS = 4
        self.COLLUMS = 8
        self.array=array
        self.where=isFirst
        self._where=isFirst   # 为我方位置，1说明我方在左，0说明我方在右,非调试状态应该取1

    def able(self,index,my_chessboard):
        '''
    己方可合并的移动方向，上下左右——>[0,1,2,3]
    '''
        row=(index%8)//2
        column=(index-2*row)//8
        flag=-1
        for i in range(row):
            if row==0:
                break
            if my_chessboard[index+1]==my_chessboard[i*2+column*8+1]:
                #print(index,i*2+column*8)
                flag=0
            if flag==0 and my_chessboard[i*2+column*8+1]!=0 and my_chessboard[index+1]!=my_chessboard[i*2+column*8+1]:
                flag=-1
                break
        if flag==0:
            return flag
        for i in range(row+1,4):
            if my_chessboard[index+1]!=my_chessboard[i*2+column*8+1] and my_chessboard[i*2+column*8+1]!=0:
                break
            if my_chessboard[index+1]==my_chessboard[i*2+column*8+1]:
                #print(index,i*2+column*8)
                flag=0
                break
        if flag==0:
            return flag
        for j in range(column):
            if column==0:
                break
            if my_chessboard[index+1]==my_chessboard[row*2+j*8+1]:
                flag=-2
            if flag==-2 and my_chessboard[row*2+j*8+1]!=0 and my_chessboard[index+1]!=my_chessboard[row*2+j*8+1]:
                flag=-1
                break
        if flag==-2:
            if self.isFirst:
                flag=2
                return flag
            else:
                flag=3
                return flag
        for j in range(column+1,4):
            if my_chessboard[index+1]!=my_chessboard[row*2+j*8+1] and my_chessboard[row*2+j*8+1]!=0:
                break
            if my_chessboard[index+1]==my_chessboard[row*2+j*8+1]:
                flag=-2
                break
        if flag==-2:
            if self.isFirst:
                flag=2
                return flag
            else:
                flag=3
                return flag
        return flag

    def able_attack(self,index,my_chessboard):
        '''
        己方可在对面边界放置棋子的位置
        '''
        row=(index%8)//2
        column=(index-2*row)//8
        for j in range(column+1,8):
            if my_chessboard[2*row+8*j]!=my_chessboard[index] and my_chessboard[2*row+8*j]!=0:
                break
            if my_chessboard[2*row+8*j]!=my_chessboard[index] and my_chessboard[2*row+8*j+1]==0 and my_chessboard[index+1]==1:
                target=2*row+8*j
                return target
        return False

    def Beginning(self,my_chessboard,board,currentRound,mode):
        position=-1
        direction=-1
        for i in range(4):#在当前局面下可合并
            if direction>=0:
                break
            if self.isFirst:
                for j in range(4):
                    index=2*i+8*j
                    #print(my_chessboard[index],my_chessboard[index+1],index)
                    if my_chessboard[index]==0:
                        #print(my_chessboard[index])
                        break
                    if my_chessboard[index]==1 and my_chessboard[index+1]!=0:
                        if self.able(index,my_chessboard)!=-1:#可合并
                            #self.able(index,my_chessboard)
                            direction=self.able(index,my_chessboard)
                            #print(direction)
                            i=board.getNext(self.isFirst,currentRound)[0]
                            j=board.getNext(self.isFirst,currentRound)[1]
                            position=i*2+8*j
                            #print(position)
                            break
            else:
                for j in range(4,8):
                    index=2*i+8*j
                    if my_chessboard[index]==1:
                        break
                    if my_chessboard[index]==0 and my_chessboard[index+1]!=0:
                        if self.able(index,my_chessboard)!=-1:#可合并
                            direction=self.able(index,my_chessboard)
                            i=board.getNext(self.isFirst,currentRound)[0]
                            j=board.getNext(self.isFirst,currentRound)[1]
                            position=i*2+8*j                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                            break
        if direction==-1:#在当前局面下不可合并，但可以通过占领领地进行合并
            for i in range(4):
                if position>0:
                    break
                if self.isFirst:
                    for j in range(4):
                        index=2*i+8*j
                        if my_chessboard[index]==1 and my_chessboard[index+1]!=0:
                            if self.able_attack(index,my_chessboard):
                                position=self.able_attack(index,my_chessboard)
                                direction=3
                else:
                    for j in range(4,8):
                        index=2*i+8*j
                        if my_chessboard[index]==0 and my_chessboard[index+1]!=0:
                            if self.able_attack(index,my_chessboard):
                                position=self.able_attack(index,my_chessboard)
                                direction=2
        else:#以上两种情况皆不满足，自保种田
            if self.isFirst:
                direction=2
            else:
                direction=3
            i=board.getNext(self.isFirst,currentRound)[0]
            j=board.getNext(self.isFirst,currentRound)[1]
            position=i*2+8*j
            
        if mode=='position':
            #print(position)
            row=(position%8)//2
            column=(position-2*row)//8
            #print(row,column)
            return (row,column)
        elif mode=='direction':
            #print(direction)
            return direction

    def set_round_mode(self):
        if self.isFirst is True:
            return ['my_position','your_position','my_direction','your_direction']
        else:
            return ['my_position','your_direction','my_direction','your_postion']


    def get_next_mode(self,current_mode):
        return self.round_mode[(self.round_mode.index(current_mode)+1)%4]

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
        if (player_move_mode == 'my_position' and self.isFirst) or (player_move_mode == 'your_position' and not self.isFirst):
            #先手方
            for i in range(4):
                for j in range(4):
                    index=2*i+8*j+1 #找己方空格，按先行后列的顺序
                    if my_chessboard[index] == 0:
                        null_list.append(int((index-1)/2)) #空格加入null_list记录，编号按照先列后行的顺序
            if null_list is not None:
                available_list.append(null_list[self.array[self.currentRound]%len(null_list)])
            for i in range(16,32):
                index=2*i+1
                if my_chessboard[index] == 0:
                    available_list.append(i)
            return available_list
        else:
            #后手方
            for i in range(4):
                for j in range(4,8):
                    index=2*i+8*j+1 #找对方空格，按先行后列的顺序
                    if my_chessboard[index] == 0:
                        null_list.append(int((index-1)/2)) #空格加入null_list记录，编号按照先列后行的顺序
            if null_list is not None:
                if self.isFirst is True: #非先手需转置列表
                    null_list.reverse()
                available_list.append(null_list[self.array[self.currentRound]%len(null_list)])
            for i in range(16):
                index=2*i+1
                if my_chessboard[index] == 0:
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
                return Get_Evl(my_chessboard,0)
            else:
                return Get_Evl(my_chessboard,1)

        if player_move_mode == 'my_position':
            max_min=float('-inf')
            available_list=self.get_available(my_chessboard,player_move_mode)
            for place in available_list:
                #print(place)
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
                return Get_Evl(my_chessboard,0)


        if player_move_mode == 'your_position':
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
                return Get_Evl(my_chessboard,0)

        if player_move_mode == 'my_direction':
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
                return Get_Evl(my_chessboard,1)

        if player_move_mode == 'your_direction':
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
                return Get_Evl(my_chessboard,1)

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

    def chessboard2mine(self,board):
        myboard=bytearray([0 for _ in range(64)])
        for x in range(8):
            for y in range(4):
                myboard[8*x+2*y]=board.getBelong((y,x))
                myboard[8*x+2*y+1]=board.getValue((y,x))
        return myboard

    def output(self, currentRound, board, mode):
        '''
        self: Player, currentRound: int, board: Chessboard, mode: str) -> Union[Tuple[int, int], int]
        输出函数
        '''
        myboard = self.chessboard2mine(board)
        print('----')
        pre(myboard)
        self.currentRound = currentRound
        if mode=='_position' or mode=='_direction':
            return None
        elif self.currentRound <= 8:
            decision=self.Beginning(myboard,board,currentRound,mode)
            print(decision,currentRound,mode)
            return decision
        elif timeup(board.getTime()):
            decision= self.search(myboard, currentRound, board.getTime(), mode)
        else:
            if mode=='position':
                move_mode="my_position"
            else:
                move_mode="my_direction"
            print('start')
            self.make_move_decision(myboard, move_mode, board.getTime()) # 这里的5是临时占位的,表示搜索深度
            print(self.answer,currentRound,move_mode)
            return self.answer
 
    def switch(self,my_board,direction,chessman):
        '''
        switch 需要传入参数：棋盘 ； 移动方向 ； 移动方是否为先手
        返回移动后的棋盘
        '''
        def changeformat(mybls, lenth):
            ''' 格式间的相互转换    '''
            boundary = 0x10
            if len(mybls)==self.ROWS*self.COLLUMS==lenth:
                changedarray = bytearray(mybls[i]<boundary if n==0 else mybls[i]%boundary
                                    for i in range(lenth) for n in [0,1])
            elif len(mybls) == self.ROWS*self.COLLUMS*2 == lenth:
                changedarray = bytearray(boundary*( 1 - mybls[2 * i] ) + mybls[1 + 2 * i] for i in range(lenth//2) )
            else: changedarray = mybls
            return changedarray
        my_board = changeformat(my_board, self.COLLUMS * self.ROWS * 2)
        # 这时棋盘转化为函数中的调用形式

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
            changedarray = bytearray(lst[i][j] for i in range(self.COLLUMS)\
               for j in range(self.ROWS))
        else:
            lst = [my_board[i::self.ROWS] for i in range(self.ROWS)]
            lst = movedict[direction](lst,chessman)
            changedarray = bytearray(lst[i][j] for j in range(self.COLLUMS)\
                for i in range(self.ROWS))
        return changeformat(changedarray,self.ROWS * self.COLLUMS)
    # 返回时用到建霖的规范
    
 
    def move_row(self,mybyte,side,chessman):
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
             
 
    def move_up(self,lst,chessman):
        for i in range(len(lst)):
            if self._where == 1 and i < self.COLLUMS//2 or\
               self._where == 0 and i >= self.COLLUMS//2:  #  1代表我方在左
                lst[i] = self.move_row(lst[i],'',chessman)
            else:
                lst[i] = self.move_row(lst[i],'change',chessman)
        return lst
 
    def move_down(self,lst,chessman):
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
 
    def move_left(self,lst,chessman):
        if self._where == 1:   # 移动方在左
            for i in range(len(lst)):
                lst[i] = self.move_row(lst[i],'left',chessman)
        else:
            for i in range(len(lst)):
                lst[i] = self.move_row(lst[i],'right',chessman)
        return lst
 
    def move_right(self,lst,chessman):
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

def pre(b):
    for y in range(4):
        s=''
        for x in range(8):
            if b[8*x+2*y]==1:
                s=s+'+'
            else:
                s=s+'-'
            s=s+str(b[8*x+2*y+1])+' '
        print(s)

alist=[1,0,1,1,1,2,1,3,1,3,1,2,1,1,1,0,1,0,1,1,1,2,1,0,1,1,1,2,1,1,1,0]+[0,0,0,1,0,2,0,3,0,3,0,2,0,1,0,0,0,0,0,1,0,2,0,3,0,3,0,2,0,1,0,0]
b=bytearray(alist)
print(b)
p=Player(True,[_ for _ in range(500)])
print(p.answer)
pre(b)
print("----")
p.make_move_decision(b,"my_position",5)
print(p.answer)
print(p.Beginning(bytearray(alist),None,1,'position'))
print(p.Beginning(bytearray(alist),None,1,'direction'))