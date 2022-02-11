def dfs(x):
    print(x, end=' ')
    check_dfs[x] = True
    for i in arr[x]:
        if check_dfs[i] == False:
            dfs(i)
            

def bfs(x):
    check_bfs[x] = True
    queue = deque([x])
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in arr[v]:
            if check_bfs[i] == False:
                queue.append(i)
                check_bfs[i] = True    


from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
check_dfs = [False] * (n+1)
check_bfs = [False] * (n+1)
arr = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)


for i in range(1, n+1):
    arr[i].sort()
            
dfs(v)
print()
bfs(v)

# 출처:https://goplanit.site/42.%20Algorithm(1260_py)/