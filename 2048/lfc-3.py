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

                if self.isFirst and depth!=0:
                    self.currentRound+=1
                depth+=1
                new_value=self.move_search(next_chessboard,self.get_next_mode(player_move_mode),depth,max_min) #recurse
                depth-=1
                if self.isFirst and depth!=0:
                    self.currentRound+=1

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
                if not self.isFirst:
                    self.currentRound+=1
                depth+=1
                new_value=self.move_search(next_chessboard,self.get_next_mode(player_move_mode),depth,max_min) #recurse
                depth-=1
                if not self.isFirst:
                    self.currentRound+=1
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
                depth+=1
                new_value=self.move_search(next_chessboard,self.get_next_mode(player_move_mode),depth,max_min) #recurse
                depth-=1
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
                depth+=1
                new_value=self.move_search(next_chessboard,self.get_next_mode(player_move_mode),depth,max_min) #recurse
                depth-=1
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
array=(356913, 393298, 305532, 290647, 632321, 511546, 715560, 323624, 381473, 418814, 257790, 28108, 311350, 596425, 487167, 551874, 621668, 210321, 266902, 261196, 133626, 110839, 522001, 560891, 100539, 703270, 652235, 275467, 659441, 92853, 255718, 208623, 18758, 67175, 138835, 384332, 610820, 252667, 184428, 22097, 239828, 273096, 23483, 430944, 544372, 452378, 23796, 280724, 289194, 303992, 497963, 447997, 717805, 406355, 309754, 502548, 219880, 697909, 603709, 121261, 327954, 694449, 372804, 252036, 567965, 245593, 516793, 160319, 229758, 515314, 705640, 122307, 108123, 413970, 710556, 7814, 524971, 442532, 617967, 628279, 302308, 712948, 402941, 452896, 390975, 366519, 398486, 472174, 277657, 243745, 8041, 350339, 21664, 496786, 466532, 41865, 466037, 464951, 111561, 258011, 35646,
622087, 381695, 514637, 688103, 413391, 86996, 642190, 391921, 446706, 649505, 718600, 99287, 68288, 584006, 108536, 8119, 210363, 607305, 683995, 528301, 419131, 263360, 682913, 373419, 648670, 213275, 5521, 687982, 711573, 28539, 290307, 76393, 672743, 205638, 4097, 608271, 669497, 152348, 344668, 524817, 700860, 654940, 160537, 564302, 587643, 450335, 532693, 536930, 88684, 165751, 17036, 134684, 434002, 507803, 119783, 249108, 238139, 281813, 340323, 622237, 524519, 14990, 399137, 100157, 344702, 524424, 628118, 434645, 401043, 313224, 498737, 309603, 501815, 500354, 304278, 61465, 181398, 535267, 14371, 500027, 43779, 212200, 191672, 529206, 26230, 373664, 467540, 174271, 213382, 410905, 332253, 209037, 209360, 248529, 13342, 712933, 291808, 28816, 699105, 344237, 2661, 631163, 42740, 315422, 317548, 226594, 187178, 170671, 348291, 547036, 507105, 686683, 473945, 215549, 624107, 196701, 463810, 668495, 646977, 320474, 229071, 194260, 699295, 519908, 482999, 92270, 77516, 495682, 128535, 585279, 294258, 76585, 272659, 268361, 96180, 510254, 107225, 197449, 353945, 581967, 541925, 184112, 76809, 293414, 678519, 256946, 656470, 373620, 419302, 698488, 456610, 152144, 594757, 566798, 40853, 296120, 264975, 630210, 228969, 356464, 701572, 432253, 422572, 111922, 557023, 319073, 567179, 568833, 335119, 240774, 248490, 496858, 8086, 350490, 518092, 465005, 2287, 557069, 129145, 402088, 710976, 337794, 566852,
195961, 100620, 133243, 188241, 550162, 136915, 329828, 220909, 283350, 50799, 215370, 591242, 658952, 329352, 550972, 115859, 311236, 325434, 411441, 38821, 707097, 606419, 323981, 527046, 158952, 131648, 105914, 487761, 525645, 291489, 394794, 373868, 596841, 148128, 444611, 223690, 223593, 479331, 708914, 684695,
390119, 39676, 535781, 428972, 535571, 528105, 219041, 583775, 455742, 502902, 303637, 570278, 51695, 37970, 486165, 256323, 228330, 433743, 636695, 56071, 171421, 650220, 198055, 212819, 220897, 303294, 22352, 605642, 644118, 163083, 224799, 278351, 130580, 712870, 291452, 322746, 391882, 156861, 505363, 690905, 474461, 8920, 177832, 540049, 650457, 349126, 137729, 130425, 451290, 623520, 226624, 226978, 396134, 675007, 83104, 70030, 168667, 581075, 112961, 588847, 504568, 130462, 601726, 514849, 433590, 705142, 94036, 546210, 263714, 452334, 530871, 20044, 288518, 509532, 421296, 49566, 425787, 447835, 46426, 37957, 542765, 673248, 628032, 392482, 280375, 301686, 280638, 101394, 123426, 255085, 461129, 386477, 172184, 18012, 589473, 179721, 449004, 306261, 437107, 160373, 493610, 338408, 225980, 138057, 327742, 362836, 209409, 271738, 221313, 251514, 541290, 694857, 655871, 92438, 281813, 460831, 41255, 113205, 668554, 674930, 396410, 150721, 317598, 461959, 484499, 516146, 216476, 203085, 345711, 369885, 597148, 226394, 468103, 543381, 489048, 125149, 285245, 164886, 655996, 1090, 77541, 650573, 12400, 172901, 254059, 653226, 14185, 223057, 82921, 673520, 375647, 541465, 439452, 213388, 115551, 552354, 314337, 445428, 657495, 99490, 418848, 203235,
70764, 81095, 185066, 639564, 406946, 682593, 115120, 449573, 621784, 30946, 175298, 428710, 500899, 512049)
alist=[1,0,1,0,1,0,1,0]+[1,0,1,0,1,0,1,0]+[1,0,1,0,1,0,1,0]+[1,0,1,0,1,0,1,0]+[0,0,0,0,0,0,0,0]+[0,0,0,1,0,0,0,0]+[0,0,0,0,0,0,0,0]+[0,0,0,0,0,0,0,0]
b=bytearray(alist)


p = Player(False, array)
print(p.answer)

pre(b)
p.make_move_decision(b, "my_position", 5)
print(p.answer)
print("----")

