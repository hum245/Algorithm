n = int(input())
res=1
for i in range(1, n+1):
    res *= i

res = list(str(res)) [::-1]
sum = 0
for i in res:
    if i == '0':
        sum+=1
    else:
        break    
    
print(sum)
    