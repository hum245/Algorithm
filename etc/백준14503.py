# N X M 크기 직사각형
# 벽 또는 빈칸으로 이루어져있음
# 청소기는 동서남북 
# 지도의 각 칸은(r_북쪽, c_서쪽) 
# 현재위치 청소 -> 현재위치에서 왼쪽방향부터 차례대로 인접칸 탐색 
# 왼쪽에 아직 청소하지않았다면, 그 방향으로 회전한다음 한칸 전진, 청소함
# 또 왼쪽으로 돌아서 청소안했으면 회전 후 전진 청소 
# 반복
# 왼쪽방향에 청소 다됐으면, 일단 회전 후 거기서 또 왼쪽 탐색 ?? 
# 모두 청소가 되있다면,, 혹은 벽이면,,, 한칸 후진 후 또 왼쪽방향부터 탐색 
# 뒤가 벽이라 후진도 안되면 작동 멈춤 
# 이미 청소된 칸을 청소하지않으며, 벽 통과 불가 

from collections import deque
# import sys
# input = sys.stdin.readline
# #sys.setrecursionlimit(1000000)

# 0:북 / 1:동 / 2:남 / 3:서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(direction):
    global answer
    x, y = robot.popleft()
    if board[x][y] == 0:
        board[x][y] = 2 #벽이아닌, 청소한곳은 2     
        answer += 1    

    for i in range(4):
        nd = (direction+3)%4
        nx = x+dx[nd]
        ny = y+dy[nd]        

        # 청소안된곳 청소하고 회전 후 전진, 청소 반복 = bfs
        if board[nx][ny] == 0:
            robot.append([nx, ny])
            bfs(nd)
            return
        direction = nd
        
    #네방향 모두 청소가 되어있거나 벽인경우       
    nd = (direction+2) % 4    
    nx = x + dx[nd]
    ny = y + dy[nd]
    if board[nx][ny] != 1 :
        robot.append([nx, ny])
        bfs(direction)        
    #후진도 안됌
    else:
        return
        
       
            

n, m = map(int, input().split())
r, c, d = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

robot = deque()

robot.append([r, c])

answer = 0
bfs(d) 
print(answer)