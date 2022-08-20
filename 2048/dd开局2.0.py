

def able(self,index,my_chessboard):
    '''
己方可合并的移动方向，上下左右——>[0,1,2,3]
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
己方可在对面边界放置棋子的位置
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
    for i in range(4):#在当前局面下可合并
        if direction>=0:
            break
        if self.isFirst:
            for j in range(4):
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
        else:
            for j in range(4,8):
                index=2*i+8*j
                if my_chessboard[index]==0:
                    break
                if my_chessboard[index]==1 and my_chessboard[index+1]!=0:
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
    else:#以上两种情况皆不满足，自保种田
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