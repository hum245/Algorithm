n, m = map(int, input().split())

arr = [[False]* m for i in range(n)]

arr[n-1][0] = True

night = [n-1, 0]

move = [[-2, 1], [-1, 2], [1, 2], [2, 1]]
sum = 0

night_visit = [[0, 0], [0, 0], [0, 0], [0, 0]]



for i in range(4):
    for j in range(2):
        night_visit[i][j] = night[j] + move[i][j]
        

while True:    
        
    if night[0] < 0 or night[1] < 0 or night[0] >= n or night[1] >= m:
        break
    
    else:
        arr[night[0]][night[1]] = True
        sum += 1
            
    
        
print(sum)