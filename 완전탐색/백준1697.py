from collections import deque
n, k = map(int, input().split())

d = [0] * 1000001

def bfs(n):
    queue = deque()
    queue.append(n)
    while queue:
        v = queue.popleft()
        if v==k:
            print(d[v])
            return
        for next in (v-1,v+1,v*2):
            if 0<=next<100001 and not d[next]:
                d[next]=d[v]+1
                queue.append(next)
                
bfs(n)