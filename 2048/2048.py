import pygame
import random

pygame.init()
pygame.font.init()

w = 400
h = 500

surface = pygame.display.set_mode((w,h))
pygame.display.set_caption("2048")
timer = pygame.time.Clock()
score = 0
file = open("highscore.txt","r")
high = int(file.readline())
file.close()
highScore = high
fps = 60
b_speed=0.5
spawnNew = True
full = False
iniCount = 0
direction = ""
colors = {0: (204, 192, 179),
        2: (238, 228, 218),
        4: (237, 224, 200),
        8: (242, 177, 121),
        16: (245, 149, 99),
        32: (246, 124, 95),
        64: (246, 94, 59),
        128: (237, 207, 114),
        256: (237, 204, 97),
        512: (237, 200, 80),
        1024: (237, 197, 63),
        2048: (237, 194, 46),
        'light text': (249, 246, 242),
        'dark text': (119, 110, 101),
        'other': (0, 0, 0),
        'bg': (187, 173, 160)}
font = pygame.font.Font("freesansbold.ttf",24)
boardValues= [[0 for i in range (4)]for j in range(4)]

def drawBoard():
    pygame.draw.rect(surface,colors['bg'],(0,0,400,400))
    scoreText = font.render("Score: " + str(score),True,"black")
    highScoreText = font.render("High Score: " + str(highScore),True,"black")
    surface.blit(scoreText,(20,410))
    surface.blit(highScoreText,(20,450))

def drawPieces(board):
    for r in range(4):
        for c in range(4):
            value = board[r][c]
            if value > 8: 
                valueColor = colors['light text']
            else: 
                valueColor = colors['dark text']
            pygame.draw.rect(surface,colors[value],(95 * c + 20,r * 95 + 20,75,75))
            if value > 0:
                valueLen = len(str(value)) 
                font = pygame.font.Font("freesansbold.ttf", 48 - valueLen * 5)
                number = font.render(str(value),True,valueColor)
                textRect = number.get_rect(center = (95 * c + 57, r * 95 + 57))
                surface.blit(number,textRect)

def newPieces(board):
    fulll = False
    count = 0
    while any(0 in row for row in board) and count < 1: 
        row = random.randint(0,3)
        col = random.randint(0,3)
        if board[row][col] == 0: 
            count += 1
            if random.randint(7,10) == 10: 
                board[row][col] = 4
            else: 
                board[row][col] = 2
    if count < 1: 
        fulll = True
    return board,fulll

def takeTurn(dir,board):    
    global score
    change = False
    merged = [[False for i in range (4)]for j in range(4)]
    if dir == "up":
        for r in range(len(board)):
            for c in range(len(board[0])): 
                shift = 0
                if r > 0: 
                    for i in range(r):
                        if board[i][c] == 0: 
                            shift += 1
                    if shift > 0:
                        
                        board[r - shift][c] = board[r][c]
                        board[r][c] = 0
                    if board[r - shift][c] == board[r - shift - 1][c] and not merged[r-shift-1][c] and not merged[r-shift][c]:
                        board[r - shift - 1][c] *= 2
                        board[r - shift][c] = 0
                        merged[r - shift - 1][c] = True
                        change = True
                        score += board[r - shift - 1][c]
                    
    
    elif dir == "down":
        for r in range(len(board)-1):
            for c in range(len(board[0])):
                shift = 0
                for i in range(r + 1):
                    if board[3-i][c] == 0:
                        shift += 1
                if shift > 0: 
                    board[2-r+shift][c] = board[2-r][c]
                    board[2 - r][c] = 0
                if 3-r+shift <= 3:
                    if board[3-r+shift][c] == board[2-r + shift][c] and not merged[3-r+shift][c] and not merged[2-r+shift][0]:
                        board[3-r + shift][c] *= 2
                        board[2-r + shift][c] = 0
                        merged[3-r + shift][c] = True
                        change = True
                        score += board[3-r + shift][c]
    
    elif dir == "left":
        for r in range(len(board)):
            for c in range(len(board[0])):
                shift = 0
                for i in range(c):
                    if board[r][i] == 0: 
                        shift += 1
                if shift > 0: 
                    board[r][c - shift] = board[r][c]
                    board[r][c] = 0
                if board[r][c - shift] == board[r][c - shift - 1] and not merged[r][c - shift - 1] and not merged[r][c - shift]:
                    board[r][c - shift - 1] *= 2
                    board[r][c - shift] = 0
                    merged[r][c - shift - 1] = True
                    change = True
                    score += board[r][c - shift - 1]
    
    elif dir == "right":
        for r in range(len(board)):
            for c in range(len(board[0])):
                shift = 0
                for i in range(c):
                    if board[r][3-i] == 0:
                        shift += 1
                if shift > 0: 
                    board[r][3-c+shift] = board[r][3-c]
                    board[r][3-c] = 0
                if 4-c+shift <= 3:
                    if board[r][3-c+shift] == board[r][4-c + shift] and not merged[r][3-c+shift] and not merged[r][4-c+shift]:
                            board[r][4-c + shift] *= 2
                            board[r][3-c + shift] = 0
                            merged[r][4-c + shift] = True
                            change = True
                            score += board[r][4-c + shift]
                
                
    return board,change

def drawOver():
    pygame.draw.rect(surface,"black",(50,50,300,100))
    font = pygame.font.SysFont("Freesansbold",30)
    gameOverText1 = font.render("GAME OVER",True,"white")
    gameOverText2 = font.render("PRESS ENTER TO RESTART",True,"white")
    surface.blit(gameOverText1,(130,65))
    surface.blit(gameOverText2,(70,105))

gameOver = False
change = True
while not gameOver: 
    timer.tick(fps)
    surface.fill("White")
    drawBoard()
    drawPieces(boardValues)
    if highScore < score: 
        highScore = score
    
    if spawnNew or iniCount < 2: 
        boardValues,full = newPieces(boardValues)
        spawnNew = False
        iniCount += 1
    
    if direction != "":
            boardValues,change = takeTurn(direction,boardValues)
            direction = ""
            spawnNew = True
    
    if not change and full:
        drawOver()
        if highScore > high: 
            file = open("highscore.txt","w")
            file.write(str(highScore))
            file.close()
            high = highScore
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                gameOver = True
        if event.type == pygame.KEYUP: 
            if full and not change: 
                if event.key == pygame.K_RETURN:
                    boardValues= [[0 for i in range (4)]for j in range(4)]
                    spawnNew = True
                    iniCount = 0
                    score = 0 
                    direction = ""
                    full = False
            elif event.key == pygame.K_UP:
                direction = "up"
            elif event.key == pygame.K_DOWN:
                direction = "down"
            elif event.key == pygame.K_LEFT:
                direction = "left"
            elif event.key == pygame.K_RIGHT:
                direction = "right"
    pygame.display.flip()
pygame.quit()