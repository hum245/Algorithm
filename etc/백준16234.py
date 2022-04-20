from collections import deque
import copy
n, l, r = map(int, input().split())


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
result = 0
cnt = 0
move = False

def bfs(x, y):
    global move
    global check
    global board
    result = board[x][y]
    check[x][y] = True
    cnt = 1
    point.append([x, y])
    temp = []
    temp.append((x, y))
    while point:
        
        x, y = point.popleft()
        for i in range(4):            
            nx = x + dx[i]
            ny = y + dy[i]
                        
            if nx<0 or nx>=n or ny <0 or ny>=n:
                continue
            if check[nx][ny]:
                continue
            if l<=abs(board[x][y] - board[nx][ny])<=r :               
                check[nx][ny] = True
                result += board[nx][ny]
                point.append([nx, ny])
                temp.append((nx, ny))
                cnt += 1
                
    if cnt>1:
        result = result // cnt
        move = True
        for x, y in temp:
            board[x][y] = result
        
    

board = [list(map(int, input().split())) for _ in range(n)]
point = deque()
answer = 0


while True:
    move = False
    check = [[False]*n for _ in range(n)]  
    for i in range(n):
        for j in range(n):
            if check[i][j] == False:
                bfs(i, j)
        
    if move == True:
        answer +=1 
    else:
        break    
            
print(answer)