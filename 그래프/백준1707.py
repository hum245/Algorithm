import sys
input = sys.stdin.readline

n = int(input())
def dfs(x, color):
    check[x] = color
    for i in arr[x]:
        if check[i] == False:
            a = dfs(i, -color)
            if not a:
                return False
        elif check[i] == check[x]:
            return False
    return True
        
    
for _ in range(n):
    v, e = map(int, input().split())
    check = [False] * (v+1)
    arr = [[] for _ in range(v+1)]
    for i in range(e):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
        
    for i in range(1, v+1):
        if check[i] == False:
            result = dfs(i, 1)
            if result == False:
                break
            
    print("YES" if result else "NO")
   
