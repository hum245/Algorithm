# r,c는 1부터 시작한다 
# 가장처음에 양분은 5만큼 들었음

# 봄 : 나무가 자기 나이만큼 양분(m) 먹고 / 나이가 1 증가
# 하나의 칸에 여러 나무가 있으면 어린나무부터 양분먹음
# 땅에 양분이 부족해 나이만큼 양분 못먹으면 즉시 죽음 

# 여름 : 봄에 죽은 나무가 양분으로 변함 
# 각각의 죽은 나무마다 나이를 2로 나눈값이 나무가있던칸에 양분으로 추가(소수점버림)
# 가을 : 나무 번식... 번식하는 나무는 나이가 5의배수인경우, 인접한 8개 칸에 나이가 1인 나무 생김
# (r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1)

# 겨울 : 로봇이 땅돌아다니며 양분추가 / 각칸에 추가되는 양분의 양은 winter[r][c], 입력으로 주어짐


from collections import deque
import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
board = [[5]*n for _ in range(n)]
wint = [list(map(int, input().split())) for _ in range(n)]
tree = []

for i in range(m):
    y, x, age = map(int, input().split())
    tree.append([x-1, y-1, age])
   
die = deque()

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def spring():
    global tree
    global die
    for i in range(len(tree)):
        x, y, age = tree.popleft()
        if board[x][y] >= age:
            board[x][y] -= age
            age += 1
            tree.append([x, y, age])
        else:   
            die.append([x, y, age])
        

def summer():
    global die
    for i in range(len(die)):
        x, y, age = die.popleft()
        board[x][y] += (age//2)


def fall():
    global tree
    j = len(tree)    
    for i in range(j):    
        x, y, age = tree.popleft()
        if age % 5 != 0:
            tree.append([x, y, age])
            continue
        
        tree.append([x, y, age])
        for j in range(8):
            nx = x + dx[j]
            ny = y + dy[j]
            
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            
            tree.append([nx, ny, 1])
        
            
        

def winter():
    for i in range(n):
        for j in range(n):
            board[i][j] += wint[j][i]
            


while k!=0:
    tree = deque(sorted(tree, key = lambda x: x[2]))
    spring()
    if die:
        summer()
    fall()
    winter()
         
    k-=1   
    

print(len(tree))
    
            
            
            
    