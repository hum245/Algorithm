def dfs(x):
    global sum
    check[x] = True
    sum += 1
    for i in arr[x]:
        if check[i] == False:         
            dfs(i)     
        
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]
check = [False] * (n+1)
sum = 0

for i in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)
    
for i in range(1, n+1):
    if check[i] == False:
        dfs(i)
        break
    
print(sum-1)        
        
