from math import gcd 

t = int(input())
arr = 0
sum = 0
while t!=0 :
    arr = list(map(int, input().split()))
    for i in range(1, arr[0]):
        for j in range(i+1, arr[0]+1):
            sum += gcd(arr[i], arr[j])
            
    print(sum)
    sum = 0        
    t-=1