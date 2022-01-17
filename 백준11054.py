n = int(input())
array = list(map(int, input().split()))

dp = [1]*n

for i in range(n):    
    for j in range(i): 
        if array[j] < array[i] and dp[i] < dp[j]+1:
            dp[i] = dp[j]+1


for k in range(dp.index(max(dp))+1, n):
    dp[k] = 1


for i in range(dp.index(max(dp)), n):
    for j in range(i):
        if array[i]<array[j] and dp[i]<=dp[j]:
            dp[i] = dp[i-1]+1



print(dp)
print(max(dp))