import random
import copy
# import pygame

# class Board:
#     def __init__(self, n = 3):
#         self.n = 3
#         self.bombList = []
    
#     def showResult():
#         changeResult()

def changeBoard(board, y, x, n):
    # board[y] = "TEST" # 바꿀 수 있다!
    dy = [1, 1, 1, 0, 0, -1, -1, -1]
    dx = [-1, 0, 1, 1, -1, -1, 0, 1]
    
    if board[y][x] != "E":
        return
    print(y, x)
    count = 0
    adjList = []
    for i in range(8):
        ny, nx = y + dy[i], x + dx[i]
        if ny >= 0 and nx >= 0 and ny <n and nx < n:
            if board[ny][nx] == "M":
                count += 1
            else:
                adjList.append([ny, nx])

    if count != 0:
        board[y] = board[y][:x] + str(count) + board[y][x+1:]

    else:
        board[y] = board[y][:x] + "B" + board[y][x+1:]
        for ny, nx in adjList:
            changeBoard(board, ny, nx, n)
    return

def maskBoard(board):
    bombList = []
    for i, line in enumerate(board):
        for j, c in enumerate(line):
            if c == "M":
                board[i] = board[i][:j] + "E" + board[i][j+1:]
                bombList.append([i, j])
    return bombList

# 일단은 초기화된 지뢰가 들어오고, 사용자가 누른 좌표가 들어왔을 때 지뢰판의 변화된 모습
def clickBoard(board, y, x):
    n = len(board)
    if board[y][x] == "M":
        board[y] = board[y][:x] + "X" + board[y][x+1:]
        return board
    
    changeBoard(board, y, x, n)
    print(board)
    bombList = maskBoard(board)
    print(board)
    print(bombList)
    return board
    


# board1 = ["EEE", "EEE", "EME"]
# clickBoard(board1, 2, 2)
board2 = ["EEEEE", "EEMEE", "EEEEE", "EEEEE", "EEEEE"]
clickBoard(board2, 4, 0)