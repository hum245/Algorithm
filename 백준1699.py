n = int(input())

dp = [ i for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, i):
        if j*j > i:
            break
        if dp[i] > dp[i-j*j] + 1:
            dp[i] = dp[i-j*j] + 1

print(dp[n])




#틀린코드
# n = int(input())

# array = [i*i for i in range(n)]
# count = 0
# dp = [0]*(n)

# array.reverse()

# while n >= 0:
#     i = 0
#     if array[i] > n :
#         continue
#     else :
#         while n >= 0:
#             n = n-array[i]
            

#     i += 1


# print(array)
# print(dp)
