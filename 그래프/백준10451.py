import sys
input = sys.stdin.readline
sys.setrecursionlimit(2000)

t = int(input())


def dfs(x):
    check_dfs[x] = True
    for i in arr[x]:
        if check_dfs[i] == False:
            dfs(i)
            

for i in range(t):
    sum = 0
    n = int(input())
    arr = [[] for i in range(n+1)]
    temp = list(map(int, input().split()))
    check_dfs = [False] * (n+1)
    for j in range(1, n+1):
        arr[j].append(temp[j-1])
        
    for k in range(1, n+1):
        if check_dfs[k] == False:
            dfs(k)
            sum+=1
           
    
    print(sum)
    
