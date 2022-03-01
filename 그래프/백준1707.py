def dfs(x):
    check[x] = 1
    for i in arr[x]:
        if check[i] == False:
            dfs(i)
        
    
n = int(input())

while n!=0:
    v, e = map(int, input().split())
    check = [False] * (v+1)
    arr = [[] for _ in range(v+1)]
    for i in range(e):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
        
    for i in range(1, v+1):
        if check[i] == False:
            dfs(i)
            
               
    n -= 1
        