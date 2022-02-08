n = int(input())

arr = list(map(int, input().split()))
count = 0

for i in arr:
    sum = 0
    if i == 1:
        continue
    for j in range(2, i+1):
        if i % j == 0:
            sum+=1
    
    if sum == 1:
        count += 1    
        
print(count)