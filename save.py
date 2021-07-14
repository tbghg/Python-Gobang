import pygame
import os
from pygame.locals import *
from consts import *
from sys import exit

SAVE_PATH = 'savedata/'
IMAGE_PATH = 'UI/'

class SaveData(object):
    def __init__(self):
        pygame.init()
        self.Data_Have = [False,False,False,False,False,False]
        self.__screen = pygame.display.set_mode((1130, 652), 0, 32)
        pygame.display.set_caption('五子棋')
        self.__ui_black = pygame.image.load(IMAGE_PATH + 'black.jpg')

    def Load_Game__Show(self):  # 将文档中的图片全部显示出来
        for i in range(6):
            try:    # 检查相应位置是否存在存档，如果不存在，则贴上空的背景图片，即 0.jpg ,总计六个存档
                self.Save_Pic = pygame.image.load(SAVE_PATH + str(i+1) + '.jpg').convert()
                self.Data_Have[i] = True
            except:
                self.Save_Pic = pygame.image.load(SAVE_PATH + '0.jpg').convert()

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

    def Load_Game__Mouse(self, chess_map, chess_state, enable_ai, isAI):
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
            clock.tick(60)
            buttons = pygame.mouse.get_pressed() # 检测鼠标按的状态
            x1, y1 = pygame.mouse.get_pos()      # 获取鼠标位置

            # 存档一，如果鼠标在这个范围，则打印出红色边框，下面六个都是如此
            if 100 <= x1 <= 100 + 282 and 60 <= y1 <= 60 + 163 :    # 检测鼠标位置
                pygame.draw.rect(self.__screen, [255, 0, 0], [100, 60, 282, 163], 5)    # 绘制方框
                pygame.display.update()

                if buttons[0]:      # 如果是左键按下
                    loop = False    # 退出循环
                    self.Save_Data(1, chess_map, chess_state, enable_ai, isAI)          # 存档
                    self.Data_Have[0] = True
                    self.Save_Data_Have()
                    os.rename('savedata/temp.jpg', 'savedata/1.jpg')

            # 存档二，与第一个相同
            elif 100 + (40 + 282)*1 <= x1 <= 100 + (40 + 282)*1 + 282 and 60 <= y1 <= 60 + 163 :
                pygame.draw.rect(self.__screen, [255, 0, 0], [100 + (40 + 282)*1, 60, 282, 163], 5)
                pygame.display.update()

                if buttons[0]:
                    loop = False
                    self.Save_Data(2,chess_map, chess_state, enable_ai, isAI)
                    self.Data_Have[1] = True
                    self.Save_Data_Have()
                    os.rename('savedata/temp.jpg', 'savedata/2.jpg')  # 这里似乎需要写为绝对路径，上一行写的那个找不到

            # 存档三
            elif 100 + (40 + 282)*2 <= x1 <= 100 + (40 + 282)*2 + 282 and 60 <= y1 <= 60 + 163 :
                pygame.draw.rect(self.__screen, [255, 0, 0], [100 + (40 + 282)*2, 60, 282, 163], 5)
                pygame.display.update()

                if buttons[0]:
                    loop = False
                    self.Save_Data(3,chess_map, chess_state, enable_ai, isAI)
                    self.Data_Have[2] = True
                    self.Save_Data_Have()
                    os.rename('savedata/temp.jpg', 'savedata/3.jpg')  # 这里似乎需要写为绝对路径，上一行写的那个找不到

            # 存档四
            elif 100 <= x1 <= 100 + 282 and 60 + 120 + 163 <= y1 <= 60 + 120 + 163 + 163 :
                pygame.draw.rect(self.__screen, [255, 0, 0], [100, 60 + 120 + 163, 282, 163], 5)
                pygame.display.update()

                if buttons[0]:
                    loop = False
                    self.Save_Data(4,chess_map, chess_state, enable_ai, isAI)
                    self.Data_Have[3] = True
                    self.Save_Data_Have()
                    os.rename('savedata/temp.jpg', 'savedata/4.jpg')  # 这里似乎需要写为绝对路径，上一行写的那个找不到

            # 存档五
            elif 100 + (40 + 282)*1 <= x1 <= 100 + (40 + 282)*1 + 282 and 60 + 120 + 163 <= y1 <= 60 + 120 + 163 + 163 :
                pygame.draw.rect(self.__screen, [255, 0, 0], [100 + (40 + 282)*1, 60 + 120 + 163, 282, 163], 5)
                pygame.display.update()

                if buttons[0]:
                    loop = False
                    self.Save_Data(5,chess_map, chess_state, enable_ai, isAI)
                    self.Data_Have[4] = True
                    self.Save_Data_Have()
                    os.rename('savedata/temp.jpg', 'savedata/5.jpg')  # 这里似乎需要写为绝对路径，上一行写的那个找不到

            # 存档六
            elif 100 + (40 + 282)*2 <= x1 <= 100 + (40 + 282)*2 + 282 and 60 + 120 + 163 <= y1 <= 60 + 120 + 163 + 163 :
                pygame.draw.rect(self.__screen, [255, 0, 0], [100 + (40 + 282)*2, 60 + 120 + 163, 282, 163], 5)
                pygame.display.update()

                if buttons[0]:
                    loop = False
                    self.Save_Data(6,chess_map, chess_state, enable_ai, isAI)
                    self.Data_Have[5] = True
                    self.Save_Data_Have()
                    os.rename('savedata/temp.jpg','savedata/6.jpg')  # 这里似乎需要写为绝对路径，上一行写的那个找不到

            else:
                self.Load_Game__Show()
        try :
            os.remove(SAVE_PATH + 'temp.jpg')
        except:
            pass

    def Save_Data_Have(self):
        # 记录存档是否存在，也即Save_Data列表
        fl = open(SAVE_PATH+ "data.txt", "w+")
        for k in self.Data_Have:
            fl.write(str(k) + '\n')
        fl.close()

    def Save_Data(self, num, map, chess_state, enable_ai, isAI):
        if self.Data_Have[num-1]:
            os.remove(SAVE_PATH + str(num) + '.jpg')
        fl = open(SAVE_PATH+ str(num)+ ".txt", "w+")

        for i in map:
            for j in i:
                fl.write(str(j))
                fl.write(' ')
            fl.write('\n')

        if chess_state == ChessboardState.WHITE :
            state = 2
        else :
            state = 1
        fl.write(str(state) + '\n')     # 下一步为黑棋还是白棋
        if enable_ai :
            fl.write(str(1) + '\n')     # 本局是否为人机对战
        else:
            fl.write(str(0) + '\n')
        if isAI :
            fl.write(str(1) + '\n')     # 若为人机对战下一步是否为人
        else:
            fl.write(str(0) + '\n')
        fl.close()

    def save_ready(self,screen):
        self.__screen.blit(self.__ui_black, (0, 0))
        self.Load_Game__Show()