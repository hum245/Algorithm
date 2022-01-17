n = int(input())
array = list(map(int, input().split()))

dp = [1]*n
memo = [0]*n
memo [0] = array[0]

for i in range(n):    
    for j in range(i): 
        if array[j] < array[i] and dp[i] < dp[j]+1:
            # dp[i] = dp[j]+1
            memo[i] = max(memo[i], memo[j]+array[i])
        else:
            memo[i] = max(memo[i], array[i])


# print("dp: ", dp)
# print("memo: ", memo)


print(max(memo))
