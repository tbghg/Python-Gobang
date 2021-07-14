from Mainmenu import *
from escmenu import *
from ChessAI import *
from read import *
from gobang import GoBang
from render import GameRender

SAVE_PATH = 'savedata/'

n0=True
n_esc=False
Mainmenu_flag=True

while n0:
    if Mainmenu_flag==True:
        Select = Mainmenu_UI()
        Select.Mainmenu_transform()
        Select.Mainmenu_select()
        if Select.n_return==True:
            continue

    if __name__ == '__main__':
        gobang = GoBang()
        render = GameRender(gobang)
        result = ChessboardState.EMPTY
        AI = ChessAI(N)
        save = SaveData()
        read = Read()
        esc_select=escmenu_UI()

        AIplayer = MAP_ENTRY_TYPE.MAP_PLAYER_TWO    # 如果是电脑先手则更改为one，电脑后手就更改为two
        board = [[0 for x in range(N)] for y in range(N)]

    if Select.n_loadgame ==True:
    # 读取存档
        read.reset()
        read.Read_Ready()
        read.Load_Game__Mouse()
        if read.n_back_menu == True:
            Select.Mainmenu_sound.stop()
            continue
        Select.isAI = read.isAI
        Select.enable_ai = read.enable_ai
        if render.chess_state() == read.chess_state :
            pass
        else :
            pass
            if not Select.enable_ai :
                render.change_state()
        for i in range(15):
            for j in range(15):
                gobang.set_chessboard_state(i,j,read.board[i][j])
    # 准备进入游戏
    Select.Mainmenu_sound.stop()
    n_first_step=True
    render.play_chess_sound.play(0)
    # 游戏内进行循环
    n1=True
    while n1:
        # 捕捉pygame事件
        for event in pygame.event.get():
            # 退出程序
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    n_esc=True

            if Select.AIFirst and Select.GameStart :  # 电脑设置为先手并进行游戏
                AIplayer = MAP_ENTRY_TYPE.MAP_PLAYER_ONE
                gobang.set_chessboard_state(7, 7, render.chess_state())
                render.set_option(7, 7)    
                render.change_state()
                render.draw_chess()
                render.draw_mouse()
                pygame.display.update()
                Select.AIFirst = False

            elif event.type == MOUSEBUTTONDOWN and Select.GameStart:
                # 成功着棋
                if render.one_step() :
                    n_first_step=False
                    result = gobang.get_chess_result()
                    render.change_state()
                    if Select.enable_ai:
                        Select.isAI = True
                elif render.press_button():
                    pass
                else:
                    continue
                if result != ChessboardState.EMPTY:
                    break
                if Select.enable_ai:  # 若电脑先手默认为正中心，下面为除去电脑先手第一步后的下棋模式
                    if Select.isAI:
                        for i in range(N):
                            for j in range(N):
                                if gobang.get_chessMap()[j][i] == ChessboardState.EMPTY:
                                    board[j][i] = 0
                                if gobang.get_chessMap()[j][i] == ChessboardState.BLACK:
                                    board[j][i] = 1
                                if gobang.get_chessMap()[j][i] == ChessboardState.WHITE:
                                    board[j][i] = 2
                        x, y = AI.findBestChess(board, AIplayer)
                        Select.isAI = not Select.isAI
                        gobang.set_chessboard_state(y, x, render.chess_state())
                        render.set_option(y, x)   
                        render.change_state()
                        result = gobang.get_chess_result()

        # 绘制大部分图形
        render.draw_chess()
        render.draw_last()
        render.draw_mouse()
        render.draw_button()
        if render.n_esc ==True:
            n_esc=True
            render.n_esc=False
        if n_first_step ==False:
            pass

        if n_esc:
            pygame.mouse.set_visible(False)
            render.draw_chess()
            pygame.display.update()
            try :
                os.remove(SAVE_PATH + 'temp.jpg')
            except:
                pass
            try:
                pygame.image.save(render._GameRender__screen, SAVE_PATH + "temp.jpg")   # 提前保存游戏截图
            except:
                pass
            pygame.mouse.set_visible(True)
            esc_select=escmenu_UI()
            esc_select.escmenu_transform()
            esc_select.escmenu_select()
            if esc_select.esc_save == True:
                # 存档
                save.save_ready(render.screen())
                for i in range(N):
                    for j in range(N):
                        if gobang.get_chessMap()[j][i] == ChessboardState.EMPTY:
                            board[j][i] = 0
                        if gobang.get_chessMap()[j][i] == ChessboardState.BLACK:
                            board[j][i] = 1
                        if gobang.get_chessMap()[j][i] == ChessboardState.WHITE:
                            board[j][i] = 2
                save.Load_Game__Mouse(board, render.chess_state(), Select.enable_ai, Select.isAI)              
            n_esc=False
        if esc_select.n_quitgame ==True:
            render.play_chess_sound.stop()
            break

        if result != ChessboardState.EMPTY:
            render.draw_chess()
            render.draw_button()
            render.draw_result(result)
            pygame.display.update()

            n1=False
            n2=True
            still=False
            while n2:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        exit()
                    elif event.type==pygame.MOUSEBUTTONDOWN:
                        if event.button==1:    
                            still=True
                mouse_button = pygame.mouse.get_pressed()
                if mouse_button[0] and still ==True:
                    n2=False
                    render.play_chess_sound.stop()

        pygame.display.update() # 刷新游戏