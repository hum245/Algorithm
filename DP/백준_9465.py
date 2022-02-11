n = int(input())

#테스트케이스(n)만큼 반복
for _ in range(n):  
    m = int(input())
    memo = [[0]*m for _ in range(2)]  #값을 기억할 공간
    dp = [list(map(int, input().split())) for _ in range(2)]  

    if m != 1:
        memo[0][0] = dp[0][0]
        memo[1][0] = dp[1][0]
        memo[0][1] = dp[0][1] + dp[1][0]
        memo[1][1] = dp[1][1] + dp[0][0]
        for i in range(2, m):
            memo[0][i] = dp[0][i] + max(memo[1][i-1], memo[1][i-2])
            memo[1][i] = dp[1][i] + max(memo[0][i-1], memo[0][i-2])           

        print(max(memo[0][m-1], memo[1][m-1]))    
    else:
        print(max(dp[0][0], dp[1][0])) 

     