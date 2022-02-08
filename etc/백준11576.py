A, B = map(int, input().split())

m = int(input())

arr = list(map(int, input().split()))
sum = 0
result = []
arr.reverse()

sum += arr[0] * 1
for i in range(1, m):
    sum += (arr[i] * (A**i))
 
while sum!=0:
    result.append(str(sum%B))
    sum = sum//B
    
result.reverse()

print(' '.join(result))