import numpy as np
import pygame
import sys
import tkinter as tk

from tkinter import messagebox

rowSize= 6
colSize = 7
gameOver = False
player = 1

def creatBoard():
    board = np.zeros((rowSize,colSize))
    return board

def validLoc(board,col):
    if board[0,col] == 0: 
        return True
    
    else:
        print("TRY ANOTHER COL!")
        return False
    
def getRow(board,col):
    for i in range(rowSize-1,-1,-1):
        if board[i,col] == 0: 
            return i
        
def dropChip(board,col,row,chip):
    board[row,col] = chip
    
def winCheck(board,chip):
    for c in range(colSize-3):
        for r in range(rowSize):
            if board[r,c] == chip and board[r,c+1] == chip and board[r,c+2] == chip and board[r,c+3] == chip:
                return True
            
    for c in range(colSize):
        for r in range(rowSize-3):
            if board[r,c] == chip and board[r+1,c] == chip and board[r+2,c] == chip and board[r+3,c] == chip:
                return True
            
    for c in range(colSize-3):
        for r in range(rowSize-3):
            if board[r,c] == chip and board[r+1,c+1] == chip and board[r+2,c+2] == chip and board[r+3,c+3] == chip:
                return True
            
    for c in range(colSize-3):
        for r in range(3,rowSize):
            if board[r,c] == chip and board[r-1,c+1] == chip and board[r-2,c+2] == chip and board[r-3,c+3] == chip:
                return True
                
    

def drawBoard(board): 
    for c in range(colSize):
        for r in range(rowSize):
            pygame.draw.rect(surface,"blue",(c*squareSize,r*squareSize+squareSize,squareSize,squareSize))
            pygame.draw.circle(surface,"black",(int(c*squareSize + squareSize // 2),int(r*squareSize + squareSize + squareSize // 2)),radius)
    for c in range(colSize):
        for r in range(rowSize):
            if board[r,c] == 1: 
                pygame.draw.circle(surface,"red",(int(c*squareSize + squareSize // 2),int(r*squareSize + squareSize + squareSize // 2)),radius)
            elif board[r,c] == 2: 
                pygame.draw.circle(surface,"yellow",(int(c*squareSize + squareSize // 2),int(r*squareSize + squareSize + squareSize // 2)),radius)
    pygame.display.update()
    
def tieCheck(board):
    count = 0
    for c in range(colSize):
        for r in range(rowSize):
            if board[r,c] == 0: 
                count += 1
    return count
                    

def message_box(subject, content):
    root = tk.Tk() # new tkinter window    
    root.attributes("-topmost", True)
    
    # on top of all oter windows    
    root.withdraw()
    messagebox.showinfo(subject, content)
    
    # shows depending on whatever subject, content we give    
    try:
        root.destroy()
    except:
        pass   

board = creatBoard()
print(board)

pygame.init()
squareSize = 100
radius = int(squareSize //2 - 5)
w = colSize * squareSize
l = (rowSize +1) * squareSize
surface = pygame.display.set_mode((w,l))
drawBoard(board)
pygame.display.update()

while not gameOver:
    # if player == 1: 
    #     col = int(input("Player 1 drop your token (0 to 6): "))
    #     if validLoc(board,col):
    #         row = getRow(board,col)
    #         dropChip(board,col,row,chip=1)
    #         if winCheck(board,chip=1):
    #             print("Player 1 wins!")
    #             gameOver=True
    #     player += 1
    # else:
    #     col = int(input("Player 2 drop your token (0 to 6): "))
    #     if validLoc(board,col):
    #         row = getRow(board,col)
    #         dropChip(board,col,row,chip=2)
    #         if winCheck(board,chip=2):
    #             print("Player 2 wins!")
    #             gameOver=True
    #     player -= 1
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEMOTION: 
            posx = event.pos[0]
            pygame.draw.rect(surface,"black",(0,0,w,squareSize))
            if player == 1: 
                pygame.draw.circle(surface,"red",(posx,squareSize //2),radius)
            else:
                pygame.draw.circle(surface,"yellow",(posx,squareSize //2),radius)
        pygame.display.update()
        
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if event.button == 1:
                print(event.pos)

                count = tieCheck(board)
                
                if count == 0: 
                    message_box("What?","It tied >:(")
                    gameOver = True
                
                if player == 1:
                    posx = event.pos[0]
                    col = posx // 100
                    if validLoc(board,col):
                        row = getRow(board,col)
                        dropChip(board,col,row,chip=1)
                        
                        drawBoard(board)
                        if winCheck(board,chip=1):
                            print("Player 1 wins!")
                            gameOver=True
                            message_box("Player 1 won!","Player 2 lost >:)")
                    player +=1
                    
                else:
                    posx = event.pos[0]
                    col = posx // 100
                    if validLoc(board,col):
                        row = getRow(board,col)
                        dropChip(board,col,row,chip=2)
                        
                        drawBoard(board)
                        if winCheck(board,chip=2):
                            print("Player 2 wins!")
                            gameOver=True
                            message_box("Player 2 won!","Player 1 lost >:)")
                    player -=1
                print(board)
                if gameOver:
                    pygame.time.wait(3000)
                