import sys
input = sys.stdin.readline
def dfs(index):
    global min_result
    #n//2까지 start 인원이 채워졌으면     
    if index == t:
        sresult = 0
        lresult = 0
        for i in arr:
            if i not in start:
                 link.append(i)
        # link = list(set(arr) - set(start))
        for i in range(t-1):
            for j in range(i+1, t):
                sresult += team[start[i]][start[j]] + team[start[j]][start[i]]
                lresult += team[link[i]][link[j]] + team[link[j]][link[i]]
                
        result = abs(sresult - lresult)
        min_result = min(result, min_result)
        
        link.clear()
        return
    
    for i in range(n):
        #0부터 2개씩 집어넣어야하니..일단 0부터 넣고 dfs를 돌리는데 cnt가 n//2일때
        if i in start:
            continue
        if len(start) > 0 and start[-1] > i:
            continue
       
        start.append(i)
        dfs(index+1)
        start.pop()

n = int(input())
arr = [i for i in range(n)]
team = [list(map(int, input().split())) for _ in range(n)]
start = []
link = []
min_result = 9999
t = n//2
dfs(0)
print(min_result)