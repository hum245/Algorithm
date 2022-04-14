# 3     : 테스트케이스 개수
#>>>case1
# 8     : 체스판 한변의 길이 I .... 체스판은 IxI
# 0 0   : 현재 있는 칸
# 7 0   : 이동하려는 칸
#>>>case2
# 100
# 0 0
# 30 50
#>>>case3
# 10
# 1 1
# 1 1
from collections import deque
import sys
sys.setrecursionlimit(100000)
def bfs():
    
    while check:
        x, y = check.popleft()
        if x == xd and y == yd:
            return board[x][y]
        for i in range(len(dx)):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx == xd and ny == yd:
                return board[x][y] + 1
            if 0<=nx<n and 0<=ny<n:                
                if board[nx][ny] == 0:
                    board[nx][ny] = board[x][y] + 1
                    check.append([nx, ny])
            
                

t = int(input())

dx = [-2, -2, -1, 1, 2, 2, 1, -1]
dy = [-1, 1, 2, 2, 1, -1, -2, -2]

for i in range(t):
    n = int(input())
    board = [[0]*n for _ in range(n)]
    x, y = map(int, input().split())
    xd, yd = map(int, input().split())
    check = deque()
    check.append([x, y])
    print(bfs())
