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




class Player():
    def __init__(self, isFirst, array):
        self.isFirst=isFirst
        self.array=array
        self.currentRound=0
        self.round_mode=self.set_round_mode()
        self.answer=None
        self.end_depth=5
        self.ROWS = 4
        self.COLLUMS = 8
        self.array=array
        self._where=isFirst   # ??????????????????1?????????????????????0??????????????????,????????????????????????1

    def Evl(self,my_chessboard, L_atk=0, R_atk=0, v1=1.0, v2=1.0, v3=1.0):
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
                    if(my_chessboard[2*j] == 49):
                        tevl_1 += (float(int(chr(my_chessboard[2*j+1]), base=16)) *
                                ((Evl_Mat_1[i][j] + Evl_Mat_1_Trans[i][j]) * v1 +
                                    (Evl_Mat_2[i][j] + Evl_Mat_2_Trans[i][j]) * v2 +
                                    (Evl_Mat_3[1-L_atk][j] + Evl_Mat_3_Trans[1-L_atk][j]) * v3))
                    elif(my_chessboard[2*j] == 48):
                        tevl_1 -= (float(int(chr(my_chessboard[2*j+1]), base=16)) *
                                ((Evl_Mat_1[i][j] + Evl_Mat_1_Trans[i][j]) * v1 +
                                    (Evl_Mat_2[i][j] + Evl_Mat_2_Trans[i][j]) * v2 +
                                    (Evl_Mat_3[1-L_atk][j] + Evl_Mat_3_Trans[1-L_atk][j]) * v3))
                    else:
                        raise ValueError
                evl_1 = tevl_1 if (i == 0 or tevl_1 > evl_1) else evl_1  # ?????????????????????
            for i in range(4):
                tevl_2 = 0.0  # temp2
                for j in range(16):  # ??????????????????
                    if(my_chessboard[2*j] == 48):
                        tevl_2 += (float(int(chr(my_chessboard[2*j+33]), base=16)) *
                                ((Evl_Mat_1[i][j] + Evl_Mat_1_Trans[i][j]) * v1 +
                                    (Evl_Mat_2[i][j] + Evl_Mat_2_Trans[i][j]) * v2 +
                                    (Evl_Mat_3[R_atk][j] + Evl_Mat_3_Trans[R_atk][j]) * v3))
                    elif(my_chessboard[2*j] == 49):
                        tevl_2 -= (float(int(chr(my_chessboard[2*j+33]), base=16)) *
                                ((Evl_Mat_1[i][j] + Evl_Mat_1_Trans[i][j]) * v1 +
                                    (Evl_Mat_2[i][j] + Evl_Mat_2_Trans[i][j]) * v2 +
                                    (Evl_Mat_3[R_atk][j] + Evl_Mat_3_Trans[R_atk][j]) * v3))
                    else:
                        raise ValueError
                evl_2 = tevl_2 if (i == 0 or tevl_2 > evl_2) else evl_2  # ?????????????????????
            evl = evl_1 - evl_2
            return evl


    def Smooth_Evl(self,my_chessboard):
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
                    smt -= abs(int(chr(my_chessboard[8*i+2*j+1]), base=16) -
                            int(chr(my_chessboard[8*i+2*j+3]), base=16))
                    smt -= abs(int(chr(my_chessboard[8*j+2*i+1]), base=16) -
                            int(chr(my_chessboard[8*j+2*i+9]), base=16))
                    smt += abs(int(chr(my_chessboard[8*i+2*j+33]), base=16) -
                            int(chr(my_chessboard[8*i+2*j+35]), base=16))
                    smt += abs(int(chr(my_chessboard[8*j+2*i+33]), base=16) -
                            int(chr(my_chessboard[8*j+2*i+41]), base=16))
            return smt


    def Free_Evl(self,my_chessboard):
        """
        ??????????????????????????????????????????
        ???????????????????????????????????????????????????
        """
        if (len(my_chessboard) != 64):
            raise ValueError
        else:
            free = 0.0
            for i in range(32):
                if (my_chessboard[2*i+1] == 48):
                    if (my_chessboard[2*i] == 49 and i < 16):
                        free += 1.0
                    elif (my_chessboard[2*i] == 48 and i >= 16):
                        free -= 1.0
                    else:
                        raise ValueError
            return free


    def Threat_Evl(self,my_chessboard, state, side=1, v1=1.0, v2=1.0, v3=1.0):
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
                if (my_chessboard[2*i] == 49 and my_chessboard[2*i+8] == 49):
                    threat += v1 * (float(int(chr(my_chessboard[2*i+1]), base=16)) +
                                    float(int(chr(my_chessboard[2*i+9]), base=16)))
                elif (my_chessboard[2*i] == 48 and my_chessboard[2*i+8] == 48):
                    threat -= v1 * (float(int(chr(my_chessboard[2*i+1]), base=16)) +
                                    float(int(chr(my_chessboard[2*i+9]), base=16)))
                elif (my_chessboard[2*i+1] == my_chessboard[2*i+9]):
                    # ?????????????????? float(my_chessboard[2*i] - my_chessboard[2*i+8])
                    threat += (v2 * float(2*int(chr(my_chessboard[2*i+1]), base=16)) if (not state)
                            else (-1) * v2 * side * float(2*int(chr(my_chessboard[2*i+1]), base=16)))
                else:
                    threat += v3 * (float(2*(my_chessboard[2*i]-48.5) * int(chr(my_chessboard[2*i+1]), base=16)) +
                                    float(2*(my_chessboard[2*i+8]-48.5) * int(chr(my_chessboard[2*i+9]), base=16)))
            return threat


    def Get_Evl(self,my_chessboard, state, side=1, L_atk=0, R_atk=0, v1=1.0, v2=1.0, v3=1.0, v4=1.0):
        '''
        ??????????????????????????????????????????????????????;
        state???0???1???0?????????????????????1?????????????????????side?????????1??????????????????????????????-1????????????????????????
        L_atk??????????????????????????????????????????R_atk?????????????????????????????????????????????????????????0???
        ?????? v1 v2 v3 v4 ???????????? Evl Smooth_Evl Free_Evl Threat_Evl ????????????float??????
        '''
        return float(side *
                    (v1 * self.Evl(my_chessboard, L_atk, R_atk) +
                    v2 * self.Smooth_Evl(my_chessboard) +
                    v3 * self.Free_Evl(my_chessboard) +
                    v4 * self.Threat_Evl(my_chessboard, state, side)))


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
            return tuple([row,column])
        elif mode=='direction':
            return tuple(direction)

    def set_round_mode(self):
        if self.isFirst is True:
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
        if (player_move_mode == 'my_position' and self.isFirst) or (player_move_mode == 'your_position' and not self.isFirst):
            #?????????
            for i in range(4):
                for j in range(4):
                    index=2*i+8*j+1 #??????????????????????????????????????????
                    if my_chessboard[index] == 0:
                        null_list.append(int((index-1)/2)) #????????????null_list??????????????????????????????????????????
            if null_list is not None:
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
                    index=2*i+8*j+1 #??????????????????????????????????????????
                    if my_chessboard[index] == 0:
                        null_list.append(int((index-1)/2)) #????????????null_list??????????????????????????????????????????
            if null_list is not None:
                if self.isFirst is True: #????????????????????????
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

        if depth == self.end_depth:
            #????????????????????????
            if player_move_mode in ('my_position', 'your_position'):
                return self.Get_Evl(my_chessboard,0)
            else:
                return self.Get_Evl(my_chessboard,1)

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
                self.currentRound+=1
                new_value=self.move_search(next_chessboard,self.get_next_mode(player_move_mode),depth+1,max_min) #recurse
                self.currentRound-=1 #backtrack
                if not depth:  
                    max_min=max(max_min,new_value)
                elif (new_value>max_min): #????????????
                    max_min=new_value
                    col=place//4
                    row=place%4
                    self.answer=(row,col)
                if max_min>last_max_min:
                    return max_min
            if max_min == float('-inf'):
                return self.Get_Evl(my_chessboard,0)


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
                self.currentRound+=1
                new_value=self.move_search(next_chessboard,self.get_next_mode(player_move_mode),depth+1,max_min) #recurse
                self.currentRound-=1 #backtrack
                max_min=min(max_min,new_value)
                if max_min<=last_max_min:
                    return max_min
            if max_min==float('inf'):
                return self.Get_Evl(my_chessboard,0)

        if player_move_mode == 'my_direction':
            max_min=float('-inf')
            for direction in range(4): #0~3??????????????????
                next_chessboard=my_chessboard.copy()
                next_chessboard=self.switch(next_chessboard,direction,self.isFirst)#??????????????????
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

        if player_move_mode == 'your_direction':
            max_min=float('inf')
            for direction in range(4): #0~3??????????????????
                next_chessboard=my_chessboard.copy()
                next_chessboard=self.switch(next_chessboard,direction,not self.isFirst) #??????????????????
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

    def output(self, currentRound, board, mode):
        '''
        self: Player, currentRound: int, board: Chessboard, mode: str) -> Union[Tuple[int, int], int]
        ????????????
        '''
        myboard = self.chessboard2mine(currentRound,board)
        print(myboard)
        self.currentRound = currentRound
        if self.currentRound <= 8:
            #decision=self.Beginning(myboard,board, currentRound, mode)
            #return decision
            if mode=="_position" or mode=="_direction":
                return None
            elif mode=="position":
                my_mode="my_position"
            else:
                my_mode="my_direction"
                self.make_move_decision(myboard,my_mode,board.getTime()) # ?????????5??????????????????,??????????????????
                print(self.answer)
            return self.answer
        #elif timeup(board.getTime()):
        #    decision= self.move_search(myboard, currentRound, board.getTime(), mode)
        else:
            if mode=="_position" or mode=="_direction":
                return None
            elif mode=="position":
                my_mode="my_position"
            else:
                my_mode="my_direction"
                self.make_move_decision(myboard,my_mode,board.getTime()) # ?????????5??????????????????,??????????????????
                print(self.answer)
            return self.answer
        
        #????????????????????????????????????
 
    def chessboard2mine(self,currentRound,board):
        my_board=bytearray([0 for _ in range(64)])
        for x in range(4):
            for y in range(4):
                #??????4*4
                my_board[2*x+8*y]=board.getBelong((x,y))
                my_board[2*x+8*y+1]=board.getVal((x,y))
                #??????4*4
                my_board[2*x+8*y+32]=board.getBelong((x+4,y))
                my_board[2*x+8*y+33]=board.getVal((x+4,y))
        return my_board

    def switch(self,my_board:bytearray(),direction: int,chessman : bool) ->bytearray():
        def changeformat(mybls:bytearray(), lenth) -> bytearray():
        # ????????????????????????
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
        # ?????????????????????????????????????????????
        
        
        #  ??????
        #self.where = 1 if self.isFirst == (my_board[0]<0x80) else 0
        #print('self.isFirst:',self.isFirst,'; self.where:',['???','???'][self.where],
        #      '; chessman:',chessman,'; move_direction',['???','???','???','???'][direction],'\n')
        #  0???8???????????????
        #  ????????????
        #self._where = self.where if chessman == self.isFirst else 1-self.where
        movedict = {
            0:self.move_up,
            1:self.move_down,
            2:self.move_left,
            3:self.move_right
            }
        if direction in [0,1]:   # 0,1,2,3  ->  ????????????
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
    # ??????????????????????????????
         
 
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
                    if mybyte[i-1]/0x80 == isFriend:  #  ??????????????????
                        #print(i,1)
                        mybyte[i-1],mybyte[i]=mybyte[i],mybyte[i-1]
                        if (side == 'left' and i >= self.COLLUMS//2) or\
                           (side == 'right' and i < self.COLLUMS//2):
                            mybyte[i] = (1-isFriend) * 0x80
                        i-=1
                    elif mybyte[i-1]%0x80 == mybyte[i]%0x80 and i-1 not in protectnum:#  ?????????????????????????????????
                        #print(i,2)
                        mybyte[i-1],mybyte[i]=mybyte[i]+1,isFriend * 0x80
                        if side == 'change'or (side == 'left' and i >= self.COLLUMS//2) or \
                           (side == 'right' and i < self.COLLUMS//2):
                                #???????????????????????????
                            mybyte[i] = (1-isFriend) * 0x80
                        protectnum.append(i-1)
                        return
                    elif mybyte[i-1]%0x80 != mybyte[i]%0x80 or mybyte[i-1]//0x80 != isFriend\
                       or i-1 in protectnum:#  ????????????????????????
                        return
            for i in range(1,len(mybyte)):
                move_one(i,mybyte,side)
            return mybyte
             
 
    def move_up(self,lst:[bytearray(),...],chessman : bool) -> [bytearray(),...]:
        for i in range(len(lst)):
            if self._where == 1 and i < self.COLLUMS//2 or\
                self._where == 0 and i >= self.COLLUMS//2:  #  1??????????????????
                lst[i] = self.move_row(lst[i],'',chessman)
            else:
                lst[i] = self.move_row(lst[i],'change',chessman)
        return lst
 
    def move_down(self,lst:[bytearray(),...],chessman : bool) -> [bytearray(),...]:
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
 
    def move_left(self,lst:[bytearray(),...],chessman : bool) -> [bytearray(),...]:
        if self._where == 1:   # ???????????????
            for i in range(len(lst)):
                lst[i] = self.move_row(lst[i],'left',chessman)
        else:
            for i in range(len(lst)):
                lst[i] = self.move_row(lst[i],'right',chessman)
        return lst
 
    def move_right(self,lst:[bytearray(),...],chessman : bool) -> [bytearray(),...]:
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
'''
05.23
????????????162???180??????????????????
?????????make_move_decision?????????
????????????201???
'''

p=Player(True,[1,2,3,4,5,6,7,8,9,10])
alist=[1,1,1,2,1,3,1,4,0,1,0,2,0,3,0,4]+[1,1,1,2,1,3,1,4,1,1,1,1,1,2,0,2]+[1,1,1,2,1,3,1,4,0,1,0,2,0,3,0,4]+[1,1,1,2,1,3,1,4,0,1,0,2,0,3,0,4]
#alist=[0,1,0,1]+[0 for _ in range(62)]
b=bytearray(alist)
p.make_move_decision(b,"my_direction",5)
print(p.answer)
