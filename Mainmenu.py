import pygame
from sys import exit

pygame.init()

IMAGE_PATH = 'UI/'

WIDTH = 1130    # 设置整个框架的宽度为 1130
HEIGHT = 652    # 设置整个框架的高度为 652
class Mainmenu_UI(object):
    def __init__(self):
        self.Main_screen=pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
        pygame.display.set_caption('五子棋')
        self.i0=pygame.image.load(IMAGE_PATH +'title.jpg').convert()
        self.i1=pygame.image.load(IMAGE_PATH +'begin_game.jpg').convert()
        self.i1_click=pygame.image.load(IMAGE_PATH +'begin_game_click.jpg').convert()
        self.i2=pygame.image.load(IMAGE_PATH +'load_game.jpg').convert()
        self.i2_click=pygame.image.load(IMAGE_PATH +'load_game_click.jpg').convert()
        self.i3=pygame.image.load(IMAGE_PATH +'Quit_game.jpg').convert()
        self.i3_click=pygame.image.load(IMAGE_PATH +'Quit_game_click.jpg').convert()
        self.i4=pygame.image.load(IMAGE_PATH +'human_human.jpg').convert()
        self.i4_click=pygame.image.load(IMAGE_PATH +'human_human_click.jpg').convert()
        self.i5=pygame.image.load(IMAGE_PATH +'human_AI.jpg').convert()
        self.i5_click=pygame.image.load(IMAGE_PATH +'human_AI_click.jpg').convert()
        self.i6=pygame.image.load(IMAGE_PATH +'return_menu.jpg').convert()
        self.i6_click=pygame.image.load(IMAGE_PATH +'return_menu_click.jpg').convert()
        self.i7=pygame.image.load(IMAGE_PATH +'player_first.jpg').convert()
        self.i7_click=pygame.image.load(IMAGE_PATH +'player_first_click.jpg').convert()
        self.i8=pygame.image.load(IMAGE_PATH +'AI_first.jpg').convert()
        self.i8_click=pygame.image.load(IMAGE_PATH +'AI_first_click.jpg').convert()
        self.bg_image=pygame.image.load(IMAGE_PATH +'background.jpg').convert()
        self.Mainmenu_sound = pygame.mixer.Sound(IMAGE_PATH +"Mainmenu_begin.wav")
        self.volume=2
        self.still=False    # 防止跳转页面时鼠标点击重复生效
        self.n_return=False     # 判断是否由第二个界面返回主菜单
        self.enable_ai = False  # 是否采用 AI 对战
        self.AIFirst = False    # AI 是否先手
        self.GameStart = False  # 游戏是否开始
        self.isAI = False       # 下一步是否为 AI 下棋
        self.n_loadgame = False # 是否进入读档
    def Mainmenu_transform (self):
        # 将图片缩放至合适大小
        i0_rect=self.i0.get_rect()
        title_size=(int(i0_rect[2]*3/4),int(i0_rect[3]*3/4))
        self.i0=pygame.transform.scale(self.i0,title_size)
        i_rect=self.i1.get_rect()                     
        size=(int(i_rect[2]*2/3),int(i_rect[3]*2/3)) 
        self.i1=pygame.transform.scale(self.i1,size)
        self.i1_click=pygame.transform.scale(self.i1_click,size)
        self.i2=pygame.transform.scale(self.i2,size)
        self.i2_click=pygame.transform.scale(self.i2_click,size)
        self.i3=pygame.transform.scale(self.i3,size)
        self.i3_click=pygame.transform.scale(self.i3_click,size)
        self.i4=pygame.transform.scale(self.i4,size)
        self.i4_click=pygame.transform.scale(self.i4_click,size)
        self.i5=pygame.transform.scale(self.i5,size)
        self.i5_click=pygame.transform.scale(self.i5_click,size)
        self.i6=pygame.transform.scale(self.i6,size)
        self.i6_click=pygame.transform.scale(self.i6_click,size)
        self.i7=pygame.transform.scale(self.i7,size)
        self.i7_click=pygame.transform.scale(self.i7_click,size)
        self.i8=pygame.transform.scale(self.i8,size)
        self.i8_click=pygame.transform.scale(self.i8_click,size)

        self.Main_screen.fill((255,255,255))

    def Mainmenu_select (self):
        # 进入主菜单进行选择
        self.Mainmenu_sound.set_volume(self.volume)
        self.Mainmenu_sound.play(0) # 播放背景音乐
        clock = pygame.time.Clock() 
        n1=True
        n2=True
        n3=True
        # 主菜单，第一次循环，判断开始游戏、载入游戏及退出游戏
        while n1:
            for event in pygame.event.get(): 
            # 判断事件类型是否是退出事件
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:   # 1代表的是鼠标左键
                        still=True

            clock.tick(30)
            self.Main_screen.blit(self.bg_image,(0,0))
            self.Main_screen.blit(self.i0,(0,0))
            self.Main_screen.blit(self.i1,(70,150))
            self.Main_screen.blit(self.i2,(70,300))
            self.Main_screen.blit(self.i3,(70,450))
            buttons = pygame.mouse.get_pressed()
            x1, y1 = pygame.mouse.get_pos()
            if x1>85 and x1<390 and y1<235 and y1>150:
                self.Main_screen.blit(self.i1_click,(70,150))
                if buttons[0] and still==True:
                    n1=False
            elif x1>85 and x1<390 and y1<385 and y1>290:
                self.Main_screen.blit(self.i2_click,(70,300))
                if buttons[0] and still==True:
                    n1=False
                    n2=False
                    self.GameStart = True
                    self.n_loadgame=True
            elif x1>85 and x1<390 and y1<535 and y1>465:
                self.Main_screen.blit(self.i3_click,(70,450))
                if buttons[0] and still==True:
                    pygame.quit()
                    exit()
            else:
                self.Main_screen.blit(self.i1,(70,150))
                self.Main_screen.blit(self.i2,(70,300))
                self.Main_screen.blit(self.i3,(70,450))
            pygame.display.update()
        still=False

        # 进入第二次循环（选择开始游戏进入），判断人人对战、人机对战或返回菜单
        while n2:
            for event in pygame.event.get(): 
            # 判断事件类型是否是退出事件
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    if event.button==1:    # 1代表的是鼠标左键
                        still=True
            clock.tick(30)
            self.Main_screen.blit(self.bg_image,(0,0))
            self.Main_screen.blit(self.i0,(0,0))
            self.Main_screen.blit(self.i4,(70,150))
            self.Main_screen.blit(self.i5,(70,300))
            self.Main_screen.blit(self.i6,(70,450))
            buttons2 = pygame.mouse.get_pressed()
            x1, y1 = pygame.mouse.get_pos()
            if x1>85 and x1<390 and y1<235 and y1>150:
                self.Main_screen.blit(self.i4_click,(70,150))
                if buttons2[0] and still==True:
                    n2=False
                    self.GameStart = True

            elif x1>85 and x1<390 and y1<385 and y1>290:
                self.Main_screen.blit(self.i5_click,(70,300))
                if buttons2[0] and still==True:
                    n2=False
                    self.enable_ai=True
                    self.GameStart = True

            elif x1>85 and x1<390 and y1<535 and y1>465:
                self.Main_screen.blit(self.i6_click,(70,450))
                if buttons2[0] and still==True:
                    n2=False
                    self.n_return=True
            else:
                self.Main_screen.blit(self.i4,(70,150))
                self.Main_screen.blit(self.i5,(70,300))
                self.Main_screen.blit(self.i6,(70,450))
            pygame.display.update()
        still=False
        if self.enable_ai:
            # 第三次循环（选择人机对战进入），判断玩家执黑或电脑执黑
            while n3:
                for event in pygame.event.get(): 
                    # 判断事件类型是否是退出事件
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    elif event.type==pygame.MOUSEBUTTONDOWN:
                        if event.button==1:     # 1代表的是鼠标左键
                            still=True
                clock.tick(30)
                self.Main_screen.blit(self.bg_image,(0,0))
                self.Main_screen.blit(self.i0,(0,0))
                self.Main_screen.blit(self.i7,(70,150))
                self.Main_screen.blit(self.i8,(70,300))
                buttons3 = pygame.mouse.get_pressed()
                x1, y1 = pygame.mouse.get_pos()
                if x1>85 and x1<390 and y1<235 and y1>150:
                    self.Main_screen.blit(self.i7_click,(70,150))
                    if buttons3[0] and still==True:
                        n3=False
                elif x1>85 and x1<390 and y1<385 and y1>290:
                    self.Main_screen.blit(self.i8_click,(70,300))
                    if buttons3[0] and still==True:
                        n3=False
                        self.AIFirst = True
                else:
                    self.Main_screen.blit(self.i7,(70,150))
                    self.Main_screen.blit(self.i8,(70,300))
                pygame.display.update()