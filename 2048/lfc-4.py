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
    ?????????????????????????????????????????????????????????side?????????1????????????????????????-1????????????
    L_atk??????????????????????????????????????????R_atk?????????????????????????????????????????????????????????0???
    ?????? v1 v2 v3 ???????????? SPD ZSL S_Shape ????????????float??????
    '''
    if (len(my_chessboard) != 64):
        raise ValueError
    else:
        evl = 0.0  # ?????????
        evl_1 = 0.0
        evl_2 = 0.0
        for i in range(4):
            tevl_1 = 0.0  # temp1
            for j in range(16):  # ??????????????????
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
            evl_1 = tevl_1 if (i == 0 or tevl_1 > evl_1) else evl_1  # ?????????????????????
        for i in range(4):
            tevl_2 = 0.0  # temp2
            for j in range(16):  # ??????????????????
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
            evl_2 = tevl_2 if (i == 0 or tevl_2 > evl_2) else evl_2  # ?????????????????????
        evl = evl_1 - evl_2
        return evl


def Smooth_Evl(my_chessboard) -> float:
    """
    ?????????????????????????????????????????????????????????
    ?????????????????????????????????????????????????????????????????????????????????????????????0???
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
    ??????????????????????????????????????????
    ???????????????????????????????????????????????????
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
    ???????????????????????????????????????????????????????????????????????????????????????????????????
    ????????????????????????????????????????????? v1 v2 v3 ???????????? ??????????????? ???????????????????????? ???????????????????????? ????????????float??????
    ###????????????????????????###
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
                # ?????????????????? float(my_chessboard[2*i] - my_chessboard[2*i+8])
                threat += (v2 * float(2*int(my_chessboard[2*i+1])) if (not state)
                           else (-1) * v2 * side * float(2*int(my_chessboard[2*i+1])))
            else:
                threat += v3 * (float(2*(my_chessboard[2*i]-0.5) * int(my_chessboard[2*i+1])) +
                                float(2*(my_chessboard[2*i+8]-0.5) * int(my_chessboard[2*i+9])))
        return threat


def Get_Evl(my_chessboard, state, side=1, L_atk=0, R_atk=0, v1=1.0, v2=1.0, v3=1.0, v4=1.0) -> float:
    '''
    ??????????????????????????????????????????????????????;
    state???0???1???0?????????????????????1?????????????????????side?????????1??????????????????????????????-1????????????????????????
    L_atk??????????????????????????????????????????R_atk?????????????????????????????????????????????????????????0???
    ?????? v1 v2 v3 v4 ???????????? Evl Smooth_Evl Free_Evl Threat_Evl ????????????float??????
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
        AI?????????
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
        self._where=isFirst   # ??????????????????1?????????????????????0??????????????????,????????????????????????1

    def able(self,index,my_chessboard):
        '''
    ???????????????????????????????????????????????????>[0,1,2,3]
    '''
        row=(index%8)//2
        column=(index-2*row)//8
        flag=-1
        for i in range(4):
            if my_chessboard[index+1]==my_chessboard[i*2+column*8+1]:
                flag=0
                return flag
        for j in range(4):
            if my_chessboard[index+1]!=my_chessboard[row*2+j*8+1]:
                break
            if my_chessboard[index+1]==my_chessboard[row*2+j*8+1]:
                if self.isFirst:
                    flag=2
                else:
                    flag=3
                return flag
        return flag

    def able_attack(self,index,my_chessboard):
        '''
        ?????????????????????????????????????????????
        '''
        row=(index%8)//2
        for j in range(8):
            if my_chessboard[2*row+8*j]!=my_chessboard[index] and my_chessboard[2*row+8*j+1]==0 and my_chessboard[index+1]==1:
                target=2*row+8*j
                return target
        return False

    def Beginning(self,my_chessboard,board,currentRound,mode):
        position=-1
        direction=-1
        for i in range(4):#???????????????????????????
            if direction>=0:
                break
            if self.isFirst:
                for j in range(4):
                    index=2*i+8*j
                    if my_chessboard[index]==1:
                        break
                    if my_chessboard[index]==0 and my_chessboard[index+1]!=0:
                        if self.able(index,my_chessboard)!=-1:#?????????
                            direction=self.able(index,my_chessboard)
                            i=board.getNext(self.isFirst,currentRound)[0]
                            j=board.getNext(self.isFirst,currentRound)[1]
                            position=i*2+8*j                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                            break
            else:
                for j in range(4,8):
                    index=2*i+8*j
                    if my_chessboard[index]==0:
                        break
                    if my_chessboard[index]==1 and my_chessboard[index+1]!=0:
                        if self.able(index,my_chessboard)!=-1:#?????????
                            direction=self.able(index,my_chessboard)
                            i=board.getNext(self.isFirst,currentRound)[0]
                            j=board.getNext(self.isFirst,currentRound)[1]
                            position=i*2+8*j                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                            break
        if direction==-1:#????????????????????????????????????????????????????????????????????????
            for i in range(4):
                if position>0:
                    break
                if self.isFirst:
                    for j in range(4):
                        index=2*i+8*j
                        if my_chessboard[index]==0 and my_chessboard[index+1]!=0:
                            if self.able_attack(index,my_chessboard):
                                position=self.able_attack(index,my_chessboard)
                                direction=3
                else:
                    for j in range(4,8):
                        index=2*i+8*j
                        if my_chessboard[index]==1 and my_chessboard[index+1]!=0:
                            if self.able_attack(index,my_chessboard):
                                position=self.able_attack(index,my_chessboard)
                                direction=2
        else:#?????????????????????????????????????????????
            if self.isFirst:
                direction=2
            else:
                direction=3
            i=board.getNext(self.isFirst,currentRound)[0]
            j=board.getNext(self.isFirst,currentRound)[1]
            position=i*2+8*j
            
        if mode=='position':
            row=(position%8)//2
            column=(position-2*row)//8
            return (row,column)
        elif mode=='direction':
            return direction

    def set_round_mode(self):
        if self.isFirst == True:
            return ['my_position','your_position','my_direction','your_direction']
        else:
            return ['my_position','your_direction','my_direction','your_postion']


    def get_next_mode(self,current_mode):
        return self.round_mode[(self.round_mode.index(current_mode)+1)%4]

    def get_available(self,my_chessboard,player_move_mode):
        '''
        ??????????????????bytearray???????????????????????????????????????????????????????????????????????????????????????????????????
        player_move_mode?????????????????????
        ????????????????????????
        0 4 8 ...
        1 5 9 ...
        2 6 10 ...
        3 8 12 ...
        ??????????????????????????????????????????????????????int??????
        '''
        available_list=[]
        null_list=[]
        if ((player_move_mode == 'my_position') and self.isFirst) or ((player_move_mode == 'your_position') and not self.isFirst):
            #?????????
            for i in range(4):
                for j in range(4):
                    index=2*i+8*j+1 #??????????????????????????????????????????
                    if my_chessboard[index] == 0:
                        null_list.append(int((index-1)/2)) #????????????null_list??????????????????????????????????????????
            if null_list !=[]:
                available_list.append(null_list[self.array[self.currentRound]%len(null_list)])
            for i in range(16,32):
                index=2*i+1
                if my_chessboard[index] == 0:
                    available_list.append(i)
            return available_list
        else:
            #?????????
            for i in range(4):
                for j in range(4,8):
                    index=2*i+8*j+1 #?????????????????????????????????????????????
                    if my_chessboard[index] == 0:
                        null_list.append(int((index-1)/2)) #????????????null_list??????????????????????????????????????????
            if null_list !=[]:
                null_list.reverse()
                available_list.append(null_list[self.array[self.currentRound]%len(null_list)])
            for i in range(16):
                index=2*i+1
                if my_chessboard[index] == 0:
                    available_list.append(i)
            return available_list


    def move_search(self,my_chessboard,player_move_mode,depth,last_max_min):
        '''
        ????????????
        ????????????????????????bytearray??????my_chessboard, ??????????????????????????????move_mode, ????????????depth, ????????????max_min
        ?????????????????????????????????value???
        ??????????????????????????????self.answer???
        ????????????depth???0, last_max_min float('inf')
        '''
        max_min=0

        if depth == self.end_depth:
            #????????????????????????
            if player_move_mode in ('my_position', 'your_position'):
                return Get_Evl(my_chessboard,0)
            else:
                return Get_Evl(my_chessboard,1)

        if player_move_mode == 'my_position':
            max_min=float('-inf')
            available_list=self.get_available(my_chessboard,player_move_mode)
            for place in available_list:
                #print(place)
                #copy???????????????????????????????????????...
                next_chessboard=my_chessboard.copy()
                if self.isFirst: #?????? ???????????????
                    if place < 16:
                        next_chessboard[2*place]=0 #0??????1??????
                        next_chessboard[2*place+1]=1 #???????????????2
                    else:
                        next_chessboard[2*place]=1
                        next_chessboard[2*place+1]=1 #???????????????2
                else: #?????? ???????????????
                    if place>=16:
                        next_chessboard[2*place]=0
                        next_chessboard[2*place+1]=1 #???????????????2
                    else:
                        next_chessboard[2*place]=1
                        next_chessboard[2*place+1]=1 #???????????????2
                depth+=1
                new_value=self.move_search(next_chessboard,self.get_next_mode(player_move_mode),depth,max_min) #recurse
                depth-=1
                if depth!=0:  
                    max_min=max(max_min,new_value)
                elif (new_value>max_min): #????????????
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
                #copy???????????????????????????????????????...
                next_chessboard=my_chessboard.copy()
                if self.isFirst: #??????????????? ??????????????????
                    if place >= 16:
                        next_chessboard[2*place]=1 #0??????1??????
                        next_chessboard[2*place+1]=1 #???????????????????????????2
                    else:
                        next_chessboard[2*place]=0
                        next_chessboard[2*place+1]=1 
                else: #???????????????
                    if place<16:
                        next_chessboard[2*place]=1
                        next_chessboard[2*place+1]=1 
                    else:
                        next_chessboard[2*place]=0
                        next_chessboard[2*place+1]=1 #???????????????2
                depth+=1
                new_value=self.move_search(next_chessboard,self.get_next_mode(player_move_mode),depth,max_min) #recurse
                depth-=1
                max_min=min(max_min,new_value)
                if max_min<=last_max_min:
                    return max_min
            if max_min==float('inf'):
                return Get_Evl(my_chessboard,0)

        if player_move_mode == 'my_direction':
            max_min=float('-inf')
            for direction in range(4): #0~3??????????????????
                next_chessboard=my_chessboard.copy()
                next_chessboard=self.switch(next_chessboard,direction,self.isFirst)#??????????????????
                if next_chessboard == my_chessboard:
                    continue
                if not self.isFirst:
                    self.currentRound+=1
                depth+=1
                new_value=self.move_search(next_chessboard,self.get_next_mode(player_move_mode),depth,max_min) #recurse
                depth-=1
                if not self.isFirst:
                    self.currentRound-=1
                if depth != 0:  
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
            for direction in range(4): #0~3??????????????????
                next_chessboard=my_chessboard.copy()
                next_chessboard=self.switch(next_chessboard,direction,not self.isFirst) #??????????????????
                if next_chessboard == my_chessboard:
                    continue
                if self.isFirst:
                    self.currentRound+=1
                depth+=1
                new_value=self.move_search(next_chessboard,self.get_next_mode(player_move_mode),depth,max_min) #recurse
                depth-=1
                if self.isFirst:
                    self.currentRound-=1
                max_min=min(max_min,new_value)
                if max_min<=last_max_min:
                    return max_min
            if max_min==float('inf'):
                return Get_Evl(my_chessboard,1)

        return max_min


    def make_move_decision(self,chessboard,player_move_mode,time_remain):
        #????????????
        '''
        ????????????????????????????????????
        ????????????????????????????????????????????????
        ??????????????????????????????????????????self.answer
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
        ????????????
        '''
        myboard = self.chessboard2mine(board)
        print('----')
        pre(myboard)
        self.currentRound = currentRound
        if mode=='_position' or mode=='_direction':
            return None
        #elif self.currentRound <= 8:
        #    decision=self.Beginning(myboard,board,currentRound,mode)
        #    print(decision,currentRound,mode)
        #    return decision
        #elif timeup(board.getTime()):
        #    decision= self.search(myboard, currentRound, board.getTime(), mode)
        else:
            if mode=='position':
                move_mode="my_position"
            else:
                move_mode="my_direction"
            print('start')
            self.make_move_decision(myboard, move_mode, board.getTime()) # ?????????5??????????????????,??????????????????
            print(self.answer,currentRound,move_mode)
            return self.answer
 
    def switch(self,my_board,direction,chessman):
        '''
        switch ??????????????????????????? ??? ???????????? ??? ????????????????????????
        ????????????????????????
        '''
        def changeformat(mybls, lenth):
            ''' ????????????????????????    '''
            boundary = 0x10
            if len(mybls)==self.ROWS*self.COLLUMS==lenth:
                changedarray = bytearray(mybls[i]<boundary if n==0 else mybls[i]%boundary
                                    for i in range(lenth) for n in [0,1])
            elif len(mybls) == self.ROWS*self.COLLUMS*2 == lenth:
                changedarray = bytearray(boundary*( 1 - mybls[2 * i] ) + mybls[1 + 2 * i] for i in range(lenth//2) )
            else: changedarray = mybls
            return changedarray
        my_board = changeformat(my_board, self.COLLUMS * self.ROWS * 2)
        # ?????????????????????????????????????????????

        self._where = self.where if chessman == self.isFirst else 1-self.where
        movedict = {
            0:self.move_up,
            1:self.move_down,
            2:self.move_left,
            3:self.move_right
            }
        if direction in [0,1]:   # 0,1,2,3  ->  ????????????
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
    # ??????????????????????????????
    
 
    def move_row(self,mybyte,side,chessman):
            '''
            ???????????????????????? ??? ??????????????????side????????????????????????????????? ?????????????????????????????????
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
                    if mybyte[i-1]/boundary == isFriend:  #  ??????????????????
                        #print(i,1)
                        mybyte[i-1],mybyte[i]=mybyte[i],mybyte[i-1]
                        if (side == 'left' and i >= self.COLLUMS//2) or\
                           (side == 'right' and i < self.COLLUMS//2):
                            mybyte[i] = (1-isFriend) * boundary
                        i-=1
                    elif mybyte[i-1]%boundary == mybyte[i]%boundary and i-1 not in protectnum:#  ?????????????????????????????????
                        #print(i,2)
                        mybyte[i-1],mybyte[i]=mybyte[i]+1,isFriend * boundary
                        if side == 'change'or (side == 'left' and i >= self.COLLUMS//2) or \
                           (side == 'right' and i < self.COLLUMS//2):
                                #???????????????????????????
                            mybyte[i] = (1-isFriend) * boundary
                        protectnum.append(i-1)
                        return
                    elif mybyte[i-1]%boundary != mybyte[i]%boundary or mybyte[i-1]//boundary != isFriend\
                       or i-1 in protectnum:#  ????????????????????????
                        return
            for i in range(1,len(mybyte)):
                move_one(i,mybyte,side)
            return mybyte
             
 
    def move_up(self,lst,chessman):
        for i in range(len(lst)):
            if self._where == 1 and i < self.COLLUMS//2 or\
               self._where == 0 and i >= self.COLLUMS//2:  #  1??????????????????
                lst[i] = self.move_row(lst[i],'',chessman)
            else:
                lst[i] = self.move_row(lst[i],'change',chessman)
        return lst
 
    def move_down(self,lst,chessman):
        for i in range(len(lst)):
            if self._where == 1 and i < self.COLLUMS//2 or\
               self._where == 0 and i >= self.COLLUMS//2:  #  1?????????????????????
                lst[i].reverse()
                lst[i] = self.move_row(lst[i],'',chessman)
                lst[i].reverse()
            else:
                lst[i].reverse()
                lst[i] = self.move_row(lst[i],'change',chessman)
                lst[i].reverse()
        return lst
 
    def move_left(self,lst,chessman):
        if self._where == 1:   # ???????????????
            for i in range(len(lst)):
                lst[i] = self.move_row(lst[i],'left',chessman)
        else:
            for i in range(len(lst)):
                lst[i] = self.move_row(lst[i],'right',chessman)
        return lst
 
    def move_right(self,lst,chessman):
        if self._where == 0:   # ????????????????????????
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

import random
array=(103734, 362329, 77684, 415739, 453676, 334231, 620245, 168730, 456411, 72700, 658931, 685408, 300953, 520540, 95392, 121093, 246041, 495443, 288992, 356228, 596137, 114764, 307209, 104988, 685304, 364396, 332177, 530882, 140667, 662741, 225349, 125751, 249080, 139846, 237984, 489235, 386242, 404630, 718587, 496129,
145705, 452363, 21808, 443220, 24961, 581869, 659766, 483540, 138451, 658788, 625055, 663100, 52950, 364230, 521940, 579011, 543725, 111202, 592968, 321192, 356221, 266494, 44592, 629499, 94628, 134120, 642835, 139982, 348970, 387484, 58893, 200220, 225606, 447665, 575531, 618620, 36200, 367616, 297731, 365669, 446314, 663459, 719694, 235698, 57018, 160921, 112685, 58631, 78352, 231354, 350240, 178627, 670574, 617986, 86174, 118652, 102737, 489238, 282259, 297967, 268291,
405937, 639772, 317128, 271322, 662255, 501528, 422586, 389592, 51781, 105260, 641498, 633235, 649499, 108271, 38397, 444712, 252276, 638935, 225910, 346547, 349115, 386409, 157522, 92688, 555961, 548187, 332391, 66665, 383199, 34872, 658499, 384098, 342758, 613842, 534580, 6585, 475388, 247890, 440621, 411284, 195652, 84872, 431210, 221741, 88117, 300156, 292478, 413593, 351211, 270032, 76403, 566179, 684126, 547604, 367108, 397450, 570927, 473101, 161727, 3247, 475016, 718867, 690458, 409989, 209090, 507262, 193212, 469938, 420680, 478856, 27364, 481835, 146981, 410070, 469906, 430113, 451222, 162112, 476911, 65425, 516444, 86451, 84360, 402866, 59751, 27480, 551217, 552980, 478101, 372237, 84217, 320739, 302896, 636942, 496897, 490431, 363809, 307879, 628813, 260199, 581243, 141849, 511344, 243921, 673810, 25843, 510063, 399633, 365215, 255183, 324534, 507259, 63978, 246277, 610611, 545086, 467405, 382209, 469718, 309568, 16594, 525717,
548873, 365587, 355076, 529981, 261506, 534761, 537539, 20347, 635735, 126764, 673261, 479420, 669052, 8867, 144271, 155094, 106724, 703303, 299781, 630558, 335154, 677321, 131381, 4656, 149651, 150165, 666275, 129585, 653791, 691593, 399196, 215767, 380556, 514774, 459558, 327597, 542643, 307189, 370376, 697423, 275424, 139162, 253507, 96445, 299928, 240219, 133587, 656696, 610919, 424569, 124826, 54174, 240863, 192409, 443799, 372742, 228358, 55872, 54070, 140155, 596253, 555492, 237484, 495519, 322677, 637580, 552412, 332729, 340535, 226667, 160740, 341738, 65512, 292489, 490784, 676785, 309457, 331414, 134123, 208276, 554960, 703220, 302924, 351870, 612717, 479593, 195483, 323597, 250088, 608096, 130303, 292326, 480286, 123142, 693189, 417562, 616536, 688146, 381091, 121458, 11378, 191513, 671096, 327664, 548001, 301079, 313454, 378564, 548213, 648058, 584395, 668607, 634308, 218710, 517945, 274515, 473981, 232159, 345883, 416367, 436034, 362360, 304044, 45118, 46634, 465063, 659739, 176973, 619633, 630569, 239421, 241341, 75400, 272845, 500356, 592289, 342231, 547299, 41565, 471099, 697147,
532099, 314321, 417147, 223635, 89597, 626644, 708396, 336900, 262518, 410391, 347313, 77160, 434892, 599545, 617238, 542915, 101352, 491371, 604421, 720630, 633984, 262836, 175568, 2326, 390758, 81875, 656137, 2358, 93279, 299954, 519709, 199968, 507880, 241745, 54008, 641416, 258706, 717432, 426852, 661675, 547460, 119276, 149350, 610393, 323460, 109944, 15065, 515781, 543116, 57895, 643279, 349670, 90026, 10572, 557807, 604646, 134030, 100408, 451839, 476822, 461301, 172275, 717733, 351831, 596903, 526908, 295937, 140330, 64386, 136917, 278842, 222541, 487679, 21453, 94031, 382030, 487186, 348401, 575021, 73399, 327647, 291642, 41728, 125629, 30702, 610723, 390665, 198858, 393568, 255751, 391552, 355635, 83285, 416445, 179738, 471531, 40568, 637924, 580103, 423907, 359847, 711606,
240310, 131567, 639936, 679562, 358863, 381226, 126263, 615670, 157464, 507063, 580092, 48163, 384249, 372750, 522599, 527351, 558265, 166156, 423163, 643254,
421781, 522709, 45939, 704283, 594753, 625546, 120843, 521947, 123385, 209121, 46763, 550784, 179175, 478975)
alist=[1,0,1,0,1,0,1,1]+[1,0,1,0,1,0,1,0]+[1,1,1,0,1,0,1,0]+[1,2,1,0,1,0,1,0]+[0,0,0,0,0,0,0,0]+[0,0,0,0,0,0,0,0]+[0,0,0,0,0,0,0,0]+[0,0,0,0,0,0,0,0]
b=bytearray(alist)


p = Player(False, array)

p.currentRound=2
pre(b)
p.make_move_decision(b, "my_position", 5)
print(p.answer)
print("----")

