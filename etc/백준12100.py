import sys
from copy import deepcopy
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

def up(board):
    for j in range(n):
        pointer = 0
        for i in range(1, n):
            if board[i][j]: #빈곳이면 패스, 빈곳이 아니면 아래 조건문 실행
                temp = board[i][j]
                board[i][j] = 0
                if board[pointer][j] == 0:
                    board[pointer][j] = temp
                elif board[pointer][j] != temp:
                    pointer += 1
                    board[pointer][j] = temp
                else: 
                    board[pointer][j] *= 2
                    pointer+=1
                    
    return board
                    
    
def down(board):
    for j in range(n):
        pointer = n-1 #2
        for i in range(n-2, -1, -1):
            if board[i][j]:
                temp = board[i][j] # temp = board[1][0]
                board[i][j] = 0
                if board[pointer][j] == 0: #board[2][0]
                    board[pointer][j] = temp
                elif board[pointer][j] != temp:
                    pointer -= 1
                    board[pointer][j] = temp
                else: 
                    board[pointer][j] *= 2
                    pointer-=1
                    
    return board
    
    
def left(board):
    for i in range(n):
        pointer = 0
        for j in range(1, n):
            if board[i][j]:
                temp = board[i][j]   #temp = board[0][1] == 2
                board[i][j] = 0            
                if board[i][pointer] == 0: 
                    board[i][pointer] = temp
                elif board[i][pointer] != temp:
                    pointer += 1
                    board[i][pointer] = temp
                else: 
                    board[i][pointer] *= 2
                    pointer+=1
    return board


def right(board):
    for i in range(n):
        pointer = n-1 # 2
        for j in range(n-2, -1, -1):
            if board[i][j]:
                temp = board[i][j] #board[0][1].board[0][0]
                board[i][j] = 0
                if board[i][pointer] == 0: #board[0][2]
                    board[i][pointer] = temp
                elif board[i][pointer] != temp: #board[0][2] != temp(2)
                    pointer -= 1
                    board[i][pointer] = temp
                else: 
                    board[i][pointer] *= 2
                    pointer-=1
                    
    return board
    
    
def dfs(board, cnt):
    if cnt == 5:
        return max(map(max, board))
    
    return max(dfs(up(deepcopy(board)), cnt+1), dfs(down(deepcopy(board)), cnt+1), dfs(left(deepcopy(board)), cnt+1), dfs(right(deepcopy(board)), cnt+1))


print(dfs(board, 0))
