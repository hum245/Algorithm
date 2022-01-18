n = int(input())
array = list(map(int, input().split()))

dp_increase = [1]*n
dp_decrease = [1]*n

for i in range(n):    
    for j in range(i): 
        if array[j] < array[i] and dp_increase[i] < dp_increase[j]+1:
            dp_increase[i] = dp_increase[j]+1

# for i in range(n):
#     for j in range(i):
#         if array[i]<array[j] and dp_decrease[i]<=dp_decrease[j]:
#             dp_decrease[i] += 1

for i in range(n-1, -1, -1):    
    for j in range(n-1, i, -1): 
        if array[j] < array[i] and dp_decrease[i] < dp_decrease[j]+1:
            dp_decrease[i] = dp_decrease[j]+1


result = [0]*n
for i in range(n):
    result[i] = dp_increase[i] + dp_decrease[i]

print(dp_increase)
print(dp_decrease)
print(result)
print(max(result)-1)