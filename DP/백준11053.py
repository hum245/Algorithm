# n = int(input())

# array = list(map(int, input().split()))

# dp = []

# dp.append(array[0])

# for i in range(1, n):
#     if array[i-1] < array[i]:
#         dp.append(array[i])
#     else:
#         continue

# print(dp)
# print(len(dp))
############해설보고 다시#############


n = int(input())
array = list(map(int, input().split()))

dp = [1]*n

for i in range(n):    
    for j in range(i): 
        if array[j] < array[i] and dp[i] < dp[j]+1:
            dp[i] = dp[j]+1

print(dp)
print(max(dp))

