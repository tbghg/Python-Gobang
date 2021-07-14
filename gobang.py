from consts import *

class GoBang(object): 
    def __init__(self):
        self.__chessMap = [[ChessboardState.EMPTY for j in range(N)] for i in range(N)] # 将棋盘的落子状态全部记录下来
        self.__currentI = -1
        self.__currentJ = -1
        self.__currentState = ChessboardState.EMPTY
        self.__option=[[0, 0],[0,0]]    # 将最近两来回的黑白棋步骤记录下来，用于显示下一步落子，以及悔棋

    def get_chessMap(self): # 返回棋盘落子状况
        return self.__chessMap

    def set_option(self,i,j,state) :    # 黑棋记为1，白棋记为2，黑棋为第一个，白棋为第二个，以便实现显示上一步落子
        if state == ChessboardState.BLACK :
            self.__option[0]=[i,j]
        else:
            self.__option[1] = [i, j]

    def get_option(self):   # 获取前两步下棋状况
        return self.__option

    def get_chessboard_state(self, i, j):   # 得到i,j坐标位置的状态，检测是否可以落子，以及是否游戏结束
        return self.__chessMap[i][j]

    def set_chessboard_state(self, i, j, state):    # 设置i,j位置的状态
        self.__chessMap[i][j] = state
        self.__currentI = i
        self.__currentJ = j
        self.__currentState = state

    def get_chess_result(self): # 检测游戏是否结束
        if self.have_five(self.__currentI, self.__currentJ, self.__currentState):
            return self.__currentState
        else:
            return ChessboardState.EMPTY

    def count_on_direction(self, i, j, xdirection, ydirection, color):  # 判断是否游戏结束的核心算法（检查是否存在五子的状况）结合下面的函数一同观看
        count = 0
        for step in range(1, 5):    # 除当前位置外,朝对应方向再看4步
            if xdirection != 0 and (j + xdirection * step < 0 or j + xdirection * step >= N):
                break
            if ydirection != 0 and (i + ydirection * step < 0 or i + ydirection * step >= N):
                break
            if self.__chessMap[i + ydirection * step][j + xdirection * step] == color:
                count += 1
            else:
                break
        return count
    

    def have_five(self, i, j, color):   # 判断是否游戏结束的核心算法（检查是否存在五子的状况）结合上面的函数一同观看
        # 对四个方向进行计数 横 竖 左斜 右斜
        directions = [[(-1, 0), (1, 0)], \
                      [(0, -1), (0, 1)], \
                      [(-1, 1), (1, -1)], \
                      [(-1, -1), (1, 1)]]

        for axis in directions:
            axis_count = 1
            for (xdirection, ydirection) in axis:
                axis_count += self.count_on_direction(i, j, xdirection, ydirection, color)
                if axis_count >= 5:
                    return True

        return False