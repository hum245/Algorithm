n = int(input())

dp = [1] * n
array = list(map(int, input().split()))

for i in range(n):
    for j in range(i):
        if array[i]<array[j] and dp[i]<=dp[j]:
            dp[i] += 1

print(dp)

print(max(dp))
