import pygame
import time

WINDOW_HIGH = 600
WINDOW_WIDTH = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PINK = (247, 42, 178)
GREEN = (60, 255, 0)

LEFT = 1
SCROLL = 2
RIGHT = 3

REFRESH_RATE = 3
winner = -1


def checkWin(board):
    # check lines
    global winner
    if board[0][0] == board[0][1] == board[0][2] != 0:
        print("player", board[0][2])
        winner = board[0][2]
        return True
    elif board[1][0] == board[1][1] == board[1][2] != 0:
        print("player", board[1][2])
        winner = board[1][2]
        return True
    elif board[2][0] == board[2][1] == board[2][2] != 0:
        print("player", board[2][2])
        winner = board[2][2]
        return True
    # check rows
    elif board[0][0] == board[1][0] == board[2][0] != 0:
        print("player", board[2][0])
        winner = board[2][0]
        return True
    elif board[0][1] == board[1][1] == board[2][1] != 0:
        print("player", board[2][1])
        winner = board[2][1]
        return True
    elif board[0][2] == board[1][2] == board[2][2] != 0:
        print("player", board[2][2])
        winner = board[2][2]
        return True
    # check diagonally
    elif board[0][0] == board[1][1] == board[2][2] != 0:
        print("player", board[2][2])
        winner = board[2][2]
        return True
    elif board[0][2] == board[1][1] == board[2][0] != 0:
        print("player", board[2][0])
        winner = board[2][0]
        return True
    return False


def checkTie(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return False
    global winner
    winner = 0
    return True


def updateBoard(board, pos, player):
    for i in range(0, 3):
        for j in range(0, 3):
            if j * (WINDOW_WIDTH / 3) <= pos[0] <= (j + 1) * (WINDOW_WIDTH / 3) and \
                    i * (WINDOW_HIGH / 3) <= pos[1] <= (i + 1) * (WINDOW_HIGH / 3):
                if board[i][j] == 0:
                    board[i][j] = player


def printBoard(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], end="")
        print("")


def showMarks(screen, board):
    img1 = pygame.image.load('o.png').convert()
    img1.set_colorkey(PINK)
    img1 = pygame.transform.scale(img1, (200, 200))

    img2 = pygame.image.load('x_G.png').convert()
    img2.set_colorkey(PINK)
    img2 = pygame.transform.scale(img2, (200, 200))
    for i in range(3):
        for j in range(3):
            if board[i][j] == 1:
                screen.blit(img1, (j * (WINDOW_WIDTH / 3), i * (WINDOW_HIGH / 3)))
            elif board[i][j] == 2:
                screen.blit(img2, (j * (WINDOW_WIDTH / 3), i * (WINDOW_HIGH / 3)))
    pygame.display.flip()



def main():
    player = 1
    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    pygame.init()
    size = (WINDOW_WIDTH, WINDOW_HIGH)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Game")
    screen.fill(WHITE)
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, [i * (WINDOW_WIDTH / 3), 0], [i * (WINDOW_WIDTH / 3), WINDOW_HIGH], 5)
        pygame.display.flip()
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, [0, i * (WINDOW_HIGH / 3)], [WINDOW_WIDTH, i * (WINDOW_HIGH / 3)], 5)
        pygame.display.flip()
    clock = pygame.time.Clock()
    pygame.display.flip()
    showMarks(screen, board)
    pygame.mouse.set_visible(False)

    img1 = pygame.image.load('o.png').convert()
    img1.set_colorkey(PINK)
    img1 = pygame.transform.scale(img1, (50, 50))

    img2 = pygame.image.load('x_G.png').convert()
    img2.set_colorkey(PINK)
    img2 = pygame.transform.scale(img2, (50, 50))

    img3 = pygame.image.load('x_win.png').convert()
    img3 = pygame.transform.scale(img3, (WINDOW_WIDTH, WINDOW_HIGH))

    img4 = pygame.image.load('o_win.png').convert()
    img4 = pygame.transform.scale(img4, (WINDOW_WIDTH, WINDOW_HIGH))

    img5 = pygame.image.load('tie.png').convert()
    img5 = pygame.transform.scale(img5, (WINDOW_WIDTH, WINDOW_HIGH))

    finish = False
    while not finish:
        finish = checkWin(board)
        if not finish:
            finish = checkTie(board)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                pos = pygame.mouse.get_pos()
                if player % 2 == 0:
                    updateBoard(board, pos, 2)
                else:
                    updateBoard(board, pos, 1)
                player += 1

        screen.fill(WHITE)
        for i in range(1, 3):
            pygame.draw.line(screen, BLACK, [i * (WINDOW_WIDTH / 3), 0], [i * (WINDOW_WIDTH / 3), WINDOW_HIGH], 5)
            pygame.display.flip()
        for i in range(1, 3):
            pygame.draw.line(screen, BLACK, [0, i * (WINDOW_HIGH / 3)], [WINDOW_WIDTH, i * (WINDOW_HIGH / 3)], 5)
            pygame.display.flip()
        showMarks(screen, board)
        mPos = pygame.mouse.get_pos()
        if player % 2 != 0:
            screen.blit(img1, mPos)
        else:
            screen.blit(img2, mPos)
        pygame.display.flip()
        printBoard(board)
        clock.tick(REFRESH_RATE)
    if winner == 1:
        screen.blit(img4, (0, 0))
    elif winner == 2:
        screen.blit(img3,(0,0))
    else:
        screen.blit(img5,(0,0))
    pygame.display.flip()
    time.sleep(10.0)
    pygame.quit()
    print(winner)





main()
