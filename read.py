from save import *
from sys import exit

SAVE_PATH = 'savedata/'
IMAGE_PATH = 'UI/'

class Read():
    def __init__(self):
        pygame.init()
        self.Data_Have = [False, False, False, False, False, False]
        self.__screen = pygame.display.set_mode((1130, 652), 0, 32)
        self.n_back_menu = False
        self.isAI = False
        self.enable_ai = False  # 是否采用 AI 对战
        self.chess_state = ChessboardState.EMPTY
        self.board = [[ChessboardState.EMPTY for x in range(N)] for y in range(N)]

    def Load_Game__Show(self):  # 将文档中的图片全部显示出来
        for i in range(6):
            try:    # 检查相应位置是否存在存档，如果不存在，则贴上空的背景图片，即 0.jpg ,总计六个存档
                self.Save_Pic = pygame.image.load(SAVE_PATH + str(i+1) + '.jpg').convert()
                self.Data_Have[i] = True
            except:
                self.Save_Pic = pygame.image.load(SAVE_PATH + '0.jpg').convert()
                self.Data_Have[i] = False

            self.Save_Pic_rect = self.Save_Pic.get_rect()
            self.Save_Pic_Size = (int(self.Save_Pic_rect[2] / 4), int(self.Save_Pic_rect[3] / 4))   # 将图片缩小至原来的4*4倍
            self.Save_Pic = pygame.transform.scale(self.Save_Pic, self.Save_Pic_Size)   # 将图片呈现上去

            if i == 0 :
                self.__screen.blit(self.Save_Pic, (100 + (40 + 282)*0, 60))
            if i == 1 :
                self.__screen.blit(self.Save_Pic, (100 + (40 + 282)*1, 60))
            if i == 2 :
                self.__screen.blit(self.Save_Pic, (100 + (40 + 282)*2, 60))
            if i == 3 :
                self.__screen.blit(self.Save_Pic, (100 + (40 + 282)*0, 60 + 120 + 163))
            if i == 4 :
                self.__screen.blit(self.Save_Pic, (100 + (40 + 282)*1, 60 + 120 + 163))
            if i == 5 :
                self.__screen.blit(self.Save_Pic, (100 + (40 + 282)*2, 60 + 120 + 163))

            pygame.display.update()

    def Load_Game__Mouse(self):
        loop = True
        clock = pygame.time.Clock()    # 绘制初始的红色方框
        pygame.draw.rect(self.__screen, [255, 0, 0], [100, 60, 282, 163], 5)
        pygame.draw.rect(self.__screen, [255, 0, 0], [100 + (40 + 282) * 1, 60, 282, 163], 5)
        pygame.draw.rect(self.__screen, [255, 0, 0], [100 + (40 + 282) * 2, 60, 282, 163], 5)
        pygame.draw.rect(self.__screen, [255, 0, 0], [100, 60 + 120 + 163, 282, 163], 5)
        pygame.draw.rect(self.__screen, [255, 0, 0], [100 + (40 + 282) * 1, 60 + 120 + 163, 282, 163], 5)
        pygame.draw.rect(self.__screen, [255, 0, 0], [100 + (40 + 282) * 2, 60 + 120 + 163, 282, 163], 5)
        self.Load_Game__Show()      # 将图片重新呈现一遍
        pygame.display.update()

        while loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        loop=False
                        self.n_back_menu = True
            clock.tick(60)
            buttons = pygame.mouse.get_pressed() # 检测鼠标按的状态
            x1, y1 = pygame.mouse.get_pos()      # 获取鼠标位置

            # 存档一，如果鼠标在这个范围，就打印出红色边框，下面六个都是这样
            if 100 <= x1 <= 100 + 282 and 60 <= y1 <= 60 + 163 and self.Data_Have[0]:   # 检测鼠标位置
                pygame.draw.rect(self.__screen, [255, 0, 0], [100, 60, 282, 163], 5)    # 绘制方框
                pygame.display.update()

                if buttons[0]:          # 如果左键按下
                    loop = False        # 退出循环
                    self.Read_Data(1)   # 读取存档

            # 存档二
            elif 100 + (40 + 282)*1 <= x1 <= 100 + (40 + 282)*1 + 282 and 60 <= y1 <= 60 + 163 and self.Data_Have[1]:
                pygame.draw.rect(self.__screen, [255, 0, 0], [100 + (40 + 282)*1, 60, 282, 163], 5)
                pygame.display.update()

                if buttons[0]:          # 如果左键按下
                    loop = False        # 退出循环
                    self.Read_Data(2)   # 读取存档

            # 存档三
            elif 100 + (40 + 282)*2 <= x1 <= 100 + (40 + 282)*2 + 282 and 60 <= y1 <= 60 + 163 and self.Data_Have[2]:
                pygame.draw.rect(self.__screen, [255, 0, 0], [100 + (40 + 282)*2, 60, 282, 163], 5)
                pygame.display.update()

                if buttons[0]:          # 如果左键按下
                    loop = False        # 退出循环
                    self.Read_Data(3)   # 读取存档

            # 存档四
            elif 100 <= x1 <= 100 + 282 and 60 + 120 + 163 <= y1 <= 60 + 120 + 163 + 163 and self.Data_Have[3]:
                pygame.draw.rect(self.__screen, [255, 0, 0], [100, 60 + 120 + 163, 282, 163], 5)
                pygame.display.update()

                if buttons[0]:          # 如果左键按下
                    loop = False        # 退出循环
                    self.Read_Data(4)   # 读取存档

            # 存档五
            elif 100 + (40 + 282)*1 <= x1 <= 100 + (40 + 282)*1 + 282 and 60 + 120 + 163 <= y1 <= 60 + 120 + 163 + 163 and self.Data_Have[4]:
                pygame.draw.rect(self.__screen, [255, 0, 0], [100 + (40 + 282)*1, 60 + 120 + 163, 282, 163], 5)
                pygame.display.update()

                if buttons[0]:          # 如果左键按下
                    loop = False        # 退出循环
                    self.Read_Data(5)   # 读取存档

            # 存档六
            elif 100 + (40 + 282)*2 <= x1 <= 100 + (40 + 282)*2 + 282 and 60 + 120 + 163 <= y1 <= 60 + 120 + 163 + 163 and self.Data_Have[5]:
                pygame.draw.rect(self.__screen, [255, 0, 0], [100 + (40 + 282)*2, 60 + 120 + 163, 282, 163], 5)
                pygame.display.update()

                if buttons[0]:              # 如果左键按下
                    loop = False            # 退出循环
                    self.Read_Data(6)       # 读盘
            else:
                self.Load_Game__Show()

    def Read_Data(self, num):
        fl = open(SAVE_PATH + str(num) + ".txt", "r")
        i=0
        map = []
        lines = fl.readlines()
        for msg in lines:
            i+=1
            if i <= 15 :
                msg = msg.strip('\n')
                adm = msg.split(' ')
                map.append(adm)
            if i == 16 :
                chess_state = int(msg)
            if i == 17 :
                msg = int(msg)
                self.enable_ai = bool(msg)
            if i == 18:
                msg = int(msg)
                self.isAI = bool(msg)
        for j in range(15):
            for i in range (15):
                if int(map[j][i]) == 0:
                    self.board[j][i] = ChessboardState.EMPTY
                if int(map[j][i]) == 1:
                    self.board[j][i] = ChessboardState.BLACK
                if int(map[j][i]) == 2:
                    self.board[j][i] = ChessboardState.WHITE

        fl.close()
        if chess_state == 1:
            self.chess_state = ChessboardState.BLACK
        elif chess_state == 2 :
            self.chess_state = ChessboardState.WHITE

    def reset(self):
        self.isAI = False
        self.enable_ai = False  # 是否采用 AI 对战
        self.chess_state = ChessboardState.EMPTY

    def Read_Ready(self):
        self.__ui_black = pygame.image.load(IMAGE_PATH + 'black.jpg')
        self.__screen.blit(self.__ui_black, (0, 0))
        self.Load_Game__Show()