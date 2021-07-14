import pygame
from consts import *

IMAGE_PATH = 'UI/'
SAVE_PATH = 'savedata/'

WIDTH = 1128        # 设置整个框架的宽度
HEIGHT = 652        # 设置整个框架的高度
side = 10           # 设置棋盘图片与整个背景图片间的留白距离（10*10）
MARGIN = 27 + side  # 棋盘的边界为27
GRID = 40           # 网格之间的距离
PIECE = 40          # 棋子为40*40像素

class GameRender(object):
    def __init__(self, gobang):
        self.__option = [[-1, -1], [-1, -1], [-1, -1], [-1, -1]]  # 把黑白的步骤记录下来，用于显示上一步落子与悔棋
        # 绑定逻辑类
        self.__gobang = gobang
        # 黑棋开局
        self.__currentPieceState = ChessboardState.BLACK
        self.__gobang.set_chessboard_state
        # 初始化 pygame
        pygame.init()
        pygame.mixer.init()  # 音乐初始化
        self.__screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
        pygame.display.set_caption('五子棋')

        self.__ui_background = pygame.image.load(IMAGE_PATH + 'background.jpg').convert()
        self.__ui_last = pygame.image.load(IMAGE_PATH + 'dot.png').convert()

        self.n_esc =False
        self.__ui_button_retract = pygame.image.load(IMAGE_PATH + 'button_retract.jpg').convert()
        self.__ui_button_music = pygame.image.load(IMAGE_PATH + 'button_music.jpg').convert()
        self.__ui_button_silence = pygame.image.load(IMAGE_PATH + 'button_silence.jpg').convert()
        self.__ui_button_menu = pygame.image.load(IMAGE_PATH + 'button_menu.jpg').convert()
        i_button_rect=self.__ui_button_retract.get_rect()
        button_size=(int(i_button_rect[2]*2/5),int(i_button_rect[3]*2/5))
        self.__ui_button_retract = pygame.transform.scale(self.__ui_button_retract,button_size)
        self.__ui_button_music = pygame.transform.scale(self.__ui_button_music,button_size)
        self.__ui_button_silence = pygame.transform.scale(self.__ui_button_silence,button_size)
        self.__ui_button_menu = pygame.transform.scale(self.__ui_button_menu,button_size)
        self.__ui_chessboard = pygame.image.load(IMAGE_PATH + 'chessboard.png').convert_alpha()
        self.__ui_piece_black = pygame.image.load(IMAGE_PATH + 'piece_black0.png').convert_alpha()
        self.__ui_piece_white = pygame.image.load(IMAGE_PATH + 'piece_white0.png').convert_alpha()
        # 设置音乐
        self.n_music =True
        self.volume = 2
        self.play_chess_sound = pygame.mixer.Sound("UI/play_chess.wav")
        self.play_chess_sound.set_volume(self.volume)

    def coordinate_transform_map2pixel(self, i, j):
        # 从 chessMap 里的逻辑坐标到 UI 上的绘制坐标的转换
        return MARGIN + j * GRID, MARGIN + i * GRID

    def coordinate_transform_pixel2map(self, x, y):
        # 从 UI 上的绘制坐标到 chessMap 里的逻辑坐标的转换
        i, j = int(round((y - MARGIN) / GRID)), int(round((x - MARGIN) / GRID))  # 修改了
        # 有MAGIN, 排除边缘位置导致 i,j 越界
        if i < 0 or i >= N or j < 0 or j >= N:
            return None, None
        else:
            return i, j

    def draw_chess(self):
        # 绘制棋盘
        self.__screen.blit(self.__ui_background, (0, 0))
        self.__screen.blit(self.__ui_chessboard, (10, 10))
        # 绘制棋子
        for i in range(0, N):
            for j in range(0, N):
                x, y = self.coordinate_transform_map2pixel(i, j)
                state = self.__gobang.get_chessboard_state(i, j)
                if state == ChessboardState.BLACK:
                    self.__screen.blit(self.__ui_piece_black, (x - PIECE / 2, y - PIECE / 2))
                elif state == ChessboardState.WHITE:
                    self.__screen.blit(self.__ui_piece_white, (x - PIECE / 2, y - PIECE / 2))
                else:
                    pass

    def draw_mouse(self):
        # 获取鼠标坐标
        x, y = pygame.mouse.get_pos()
        # 棋子跟随鼠标移动
        if side + 615 >= x >= side and side + 615 >= y >= side:
            if self.__currentPieceState == ChessboardState.BLACK:
                self.__screen.blit(self.__ui_piece_black, (x - PIECE / 2, y - PIECE / 2))
            else:
                self.__screen.blit(self.__ui_piece_white, (x - PIECE / 2, y - PIECE / 2))

    def draw_result(self, result):
        font = pygame.font.Font(u"C:\Windows\Fonts\FZSTK.TTF", 50)      # 调整字体
        tips = u"本局结束:"
        if result == ChessboardState.BLACK:
            tips = tips + u"黑棋胜利"
        elif result == ChessboardState.WHITE:
            tips = tips + u"白棋胜利"
        else:
            tips = tips + u"平局"
        text = font.render(tips, True, (255, 0, 0))
        pygame.image.save(self.__screen, "screenshot.jpg")
        self.__screen.blit(text, (WIDTH / 2 - 200, HEIGHT / 2 - 50))

    def one_step(self):
        i, j = None, None
        # 检测鼠标点击
        mouse_button = pygame.mouse.get_pressed()
        # 如果左键按下
        if mouse_button[0]:
            x, y = pygame.mouse.get_pos()
            i, j = self.coordinate_transform_pixel2map(x, y)
        if not i is None and not j is None:
            # 格子上已经有棋子
            if self.__gobang.get_chessboard_state(i, j) != ChessboardState.EMPTY:
                return False
            else:
                self.__gobang.set_chessboard_state(i, j, self.__currentPieceState)
                self.set_option(i, j)
                return True
        return False

    def change_state(self):     # 更换下棋方
        if self.__currentPieceState == ChessboardState.BLACK:
            self.__currentPieceState = ChessboardState.WHITE
        else:
            self.__currentPieceState = ChessboardState.BLACK

    def chess_state(self):
        return self.__currentPieceState

    def screen(self):
        return self.__screen

    def change_music(self):
        if self.n_music ==True:
            try:
                self.play_chess_sound.stop()
                self.n_music=False
            except:
                pass
        else:
            self.play_chess_sound.play(0)
            self.n_music=True

    def draw_button(self):
            # 绘制按钮
            self.__screen.blit(self.__ui_button_retract, (625, 10))
            if self.n_music == True:
                self.__screen.blit(self.__ui_button_music, (625, 130))
            else:
                self.__screen.blit(self.__ui_button_silence, (625, 130))
            self.__screen.blit(self.__ui_button_menu, (625, 250))

    def press_button(self):     # 检测是否按下按钮
        mouse_button = pygame.mouse.get_pressed()
        if mouse_button[0]:
            x, y = pygame.mouse.get_pos()
        if x>625 and x<675 and y<105 and y>10:
            if self.__option[2] != [-1, -1] and self.__option[3] != [-1, -1]:
                self.retract()
        elif x>625 and x<675 and y<225 and y>130:
            self.change_music()
        elif x>625 and x<675 and y<345 and y>250:
            self.n_esc =True

    def set_option(self,i,j):   # 记录前四步落子

        self.__option[3] = self.__option[2]
        self.__option[2] = self.__option[1]
        self.__option[1] = self.__option[0]
        self.__option[0] = [i, j]

    def draw_last(self):        # 显示上一步落子
        if self.__option[0] != [-1, -1]:
            [i, j] = self.__option[0]
            x, y = self.coordinate_transform_map2pixel(i, j)
            self.__screen.blit(self.__ui_last, (x-3, y-3 ))


        if self.__option[1] != [-1, -1]:
            [i, j] = self.__option[1]
            x, y = self.coordinate_transform_map2pixel(i, j)
            self.__screen.blit(self.__ui_last, (x-3, y-3))

    def retract(self):          # 悔棋
        i, j = self.__option[0]
        self.__gobang.set_chessboard_state(i, j, ChessboardState.EMPTY)
        self.__option[0] = self.__option[2]
        i, j = self.__option[1]
        self.__gobang.set_chessboard_state(i, j, ChessboardState.EMPTY)
        self.__option[1] = self.__option[3]
        self.__option[2] = [-1, -1]
        self.__option[3] = [-1, -1]