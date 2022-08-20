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
