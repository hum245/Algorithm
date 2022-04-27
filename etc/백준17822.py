from collections import deque
n, m, t = map(int, input().split())

circle = [deque(map(int, input().split())) for _ in range(n)]
    #오 왼 위 아래
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):
        
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
       
        if ny >= m:
            ny = 0
        if ny < 0:
            ny = m-1
        
        if 0<=nx<n and 0<=ny<m and visited[nx][ny] != 1:
            if circle[x][y] == circle[nx][ny] and circle[x][y] != 0 and circle[nx][ny] != 0:
                if [x, y] not in erase:
                    erase.append([x, y])
                if [nx, ny] not in erase:
                    erase.append([nx, ny])
                #erase.append([x, y], [nx, ny])
                #circle[x][y], circle[nx][ny] = 0, 0
                #visited[nx][ny] = 1
     
            
        

for l in range(t):
    visited = [[0 for _ in range(m)] for _ in range(n)]
    x, d, k = map(int, input().split())
    if d == 0: d = 1
    elif d==1: d = -1
    
    cnt = 0
    erase = deque()
    total = 0
    for j in range(len(circle)):
        if (j+1) % x == 0:
            for i in range(k):
                circle[j].rotate(d)
            
    for i in range(n):
        for j in range(m):
            if visited[i][j] != 1:
                visited[i][j] = 1
                bfs(i, j)            
    
    #인접한게 없을때
    if len(erase) == 0:
        for i in range(n):
            for j in range(m):
                if circle[i][j] != 0:
                    total += circle[i][j]
                    cnt += 1
                    
        if total != 0:            
            total = total/cnt
        else:
            print(0)
            exit()
        
        for i in range(n):
            for j in range(m):
                if circle[i][j] != 0:
                    if circle[i][j] > total:
                        circle[i][j] -= 1
                    elif circle[i][j] < total:
                        circle[i][j] += 1
    
    #인접한게 있을때
    else:
        for x, y in erase:
            circle[x][y] = 0
            
result = 0
for i in range(n):
    result += sum(circle[i])
    
print(result)
    
            
            