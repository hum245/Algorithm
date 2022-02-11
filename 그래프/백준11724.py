def dfs(x):
    check[x] = True
    for i in arr[x]:
        if check[i] == False:
            dfs(i)    
    

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
check = [False] * (n+1)
arr = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
    
i = 1
sum = 0
while i!=(n+1):
    if check[i] == False:
        dfs(i)
        sum+=1        
    i+=1

print(sum)