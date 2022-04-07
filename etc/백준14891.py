from collections import deque
    
    
def dfs(i, d):    
    
    if circle[i][2] == circle[i+1][-2]:
        if d==1:
            circle[i].rotate(2)
        else:
            circle[i].rotate(-2)
        dfs(2, -d)

    if circle2[0][2] == circle3[0][-2]:
        if d==1:
            circle2.rotate(2)
        else:
            circle2.rotate(-2)
        dfs(3, -d)
    if circle2[0][-2] == circle1[0][2]:
        if d==1:
            circle2.rotate(2)
        else:
            circle2.rotate(-2)
        dfs(1, -d) 
        
        
circle = deque()
for i in range(4):
    circle.append(list(map(int, str(input()))))
       

k = int(input())
for i in range(k):
    num, d = map(int, input().split())
    dfs(num, d)
    