n , l = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
check = []
answer = 0
i = 0

#가로
for i in range(n):
    for j in range(n):
        #앞쪽이 작은수일때
        if board[i][j] != board[i][j-1] and board[i][j] - board[i][j-1] == 1:
            tmp = board[i][j-1]
            for k in range(l-1, -1, -1):
                if tmp != board[i][k+j] :
                    break
        elif board[i][j] != board[i][j-1] and board[i][j] - board[i][j-1] == -1:
            tmp = board[i][j-1]
            for k in range(l-1, -1, -1):
                
            
                
                
            
#세로               
for j in range(n):
    check.clear()
    stop = True
    for i in range(n):                     
        if check and check[-1] != board[i][j]:            
            tmp = check[-1]
            for k in range(l-1, -1, -1):
                if len(check) < l or abs(tmp - board[i][j]) != 1 or check[k] != tmp:
                    stop = False
                    break
            check.append(board[i][j])
            if stop==False:
                break
        else:
            check.append(board[i][j])
        
        if i == n-1:
            if len(check) == n:
                answer += 1
print(answer)