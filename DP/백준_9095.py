n = int(input())

input_list = []

for i in range(n) :
    input_list.append(int(input()))

dp = [0] * 11
dp[0] = 1
dp[1] = 2
dp[2] = 4

for i in range(3, max(input_list)+1) :
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for j in input_list:
    print(dp[j-1])

