from collections import deque
# 익은 : 1
# 익지않은 : 0
# 없음 : -1 

#세로가 n
m,n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
check = deque()
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            check.append((i, j))
            

def dfs(x, y):
    
    check.append((x, y))
    global cnt
    
    while check:
        x, y = check.popleft()         
        
        for i in range(4):
            if x<0 or x>=n or y<0 or y>=m:
                continue
            
            if board[x][y] !=0 or board[x][y] != -1:
                nx = x+dx[i]
                ny = y+dy[i]
                if nx<0 or nx>=n or ny<0 or ny>=m or board[nx][ny] != 0:
                    continue
                else: 
                    board[nx][ny] = board[x][y]+1
                    check.append((nx, ny))
      
        
   

 
if len(check) == (n*m):
    print(0)
    exit()
elif len(check) == 0:
    print(-1)
    exit()
else:
        
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    x, y = check.popleft()
    dfs(x,y)   

    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                print(-1)
                exit()
                
    print((max(map(max, board))-1))

    