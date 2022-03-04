from collections import deque
n, k = map(int, input().split())

visit = [0] * 1000001

def bfs(n):
    queue = deque()
    queue.append(n)
    while queue:
        node = queue.popleft()
        if node==k:
            print(visit[node])
            return
        for next in (node-1,node+1,node*2):
            if 0<=next<100001 and not visit[next]:
                visit[next] = visit[node]+1
                queue.append(next)
                
bfs(n)



#  bfs 기본 코드 

# def bfs(graph, start_node):
#     visit = list()
#     queue = list()
    
#     queue.append(start_node)
    
#     while queue:
#         node = queue.pop(0)
#         if node not in visit:
#             visit.append(node)
#             queue.extend(graph[node])
            
#     return visit