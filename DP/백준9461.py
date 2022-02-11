n = int(input())

for _ in range(n):    
    k = int(input())
    dp = [0] * 101
    
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2

    for j in range(6, k+1):
        dp[j] = dp[j-5] + dp[j-1]

    print(dp[k])