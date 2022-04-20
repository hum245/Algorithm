from collections import deque
from os import TMP_MAX
r, c, t = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(r)]
robot = deque()
robot2 = deque()
for i in range(r):
    for j in range(c):
        if board[i][j] == -1:
            robot.append([i,j])
            robot2.append([i,j])      


def bfs(x, y):
        q = deque()
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<r and 0<=ny<c and board[nx][ny] != -1:
                check[nx][ny] += (board[x][y] // 5)
                cnt += 1
                
        result = board[x][y] - ((board[x][y]//5)*cnt) 
        if result > 0:
            check[x][y]+=result
                      
        #     if 0<=nx<r and 0<=ny<c and board[nx][ny] != -1:
        #         q.append([nx, ny])
                
        # cnt = len(q)         
        # for nx, ny in q:
        #     check[nx][ny].append(board[x][y] // 5)
            
        # result = board[x][y] - ((board[x][y]//5)*cnt) 
        # if result > 0:
        #     check[x][y].append(result)
        

def upmove(dr, start, end):
    while True:
        x, y = robot.popleft()
        nx = x + ux[i]
        ny = y + uy[i]

        if start<=nx<end and 0<=ny<c:
            if board[x][y] == -1 or board[nx][ny] == 0:
                board[nx][ny] = 0
                robot.appendleft([nx, ny])
                continue
            elif board[nx][ny] == -1:
                board[x][y] = 0
                robot.appendleft([nx, ny])
                return
            else:
                board[x][y] = board[nx][ny]
                board[nx][ny] = 0
                robot.appendleft([nx, ny])
            
        else:
            robot.appendleft([x, y])
            return
    # if dr != 3:
    #     while True:
    #         x, y = robot.popleft()
    #         nx = x + ux[i]
    #         ny = y + uy[i]

    #         if start<=nx<end and start<=ny<c:
    #             if board[x][y] == -1 or board[nx][ny] == 0:
    #                 robot.appendleft([nx, ny])
    #                 continue
    #             elif board[nx][ny] == -1:
    #                 board[nx][ny] = 0
    #             else:
    #                 board[x][y] = board[nx][ny]
    #                 board[nx][ny] = 0
    #                 robot.appendleft([nx, ny])
                
    #         else:
    #             robot.appendleft([x, y])
    #             return
    # else:
    #     #tmp = 0
    #     while True:
    #         x, y = robot.popleft()
    #         #board[x][y] = tmp
    #         nx = x + ux[i]
    #         ny = y + uy[i]

    #         if start<=nx<end and start<=ny<c:
    #             if board[x][y] == -1 or board[nx][ny] == 0:
    #                 robot.appendleft([nx, ny])
    #                 continue
    #             elif board[nx][ny] == -1:
    #                 board[x][y] = 0
    #                 robot.appendleft([nx, ny])
    #                 return
    #             else:
    #                 #tmp = board[nx][ny]
    #                 board[x][y] = board[nx][ny]
    #                 board[nx][ny] = 0
    #                 robot.appendleft([nx, ny])
                
    #         else:
    #             robot.appendleft([nx, ny])
    #             return
        
        
def downmove(dr, start, end):
   
    while True:
        x, y = robot.pop()
        nx = x + ux[i]
        ny = y + uy[i]

        if start<=nx<end and 0<=ny<c:
            
            if board[x][y] == -1 or board[nx][ny] == 0:
                board[nx][ny] = 0
                robot.append([nx, ny])
                continue
            elif board[nx][ny] == -1:
                
                robot.append([nx, ny])
                return
            else:
                board[x][y] = board[nx][ny]
                board[nx][ny] = 0
                robot.append([nx, ny])
            
        else:
            robot.append([x, y])
            return
  
                


for k in range(t):                
    #check = [[deque() for _ in range(c)] for _ in range(r)]
    check = [[0]*c for _ in range(r)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    for i in range(r):
        for j in range(c):
            if board[i][j] != 0 and board[i][j] != -1:
                bfs(i, j)
                


    for i in range(r):
        for j in range(c):
            if board[i][j] != -1 and check[i][j] != 0:
                board[i][j] = check[i][j]
                # board[i][j] = 0
            # for k in range(len(check[i][j])):
            #     board[i][j] += check[i][j][k]
                
                
                
    # print("미세먼지 후 ")
    # for i in range(r):
        
    #     print(board[i])

    # print()
    
    #위쪽 공기청정기            

    ux = [-1, 0, 1, 0]
    uy = [0, 1, 0, -1]
    start = 0
    end = robot2[0][0] + 1
    for i in range(4):    
        upmove(i, start, end)


    #아래쪽 공기청정기    

    ux = [1, 0, -1, 0]
    uy = [0, 1, 0, -1]
    start = robot2[1][0]
    end = r
    for i in range(4):
        downmove(i, start, end)
    
    
    # print("공기청정기 후")
    # for i in range(r):        
    #     print(board[i])
    
    # print()
        

answer = 0
for i in range(r):
    for j in range(c):
        if board[i][j] > 0:
            answer += board[i][j]
            
print(answer)