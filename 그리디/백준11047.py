n, k = map(int, input().split())

m = []
for i in range(10):
    m.append(int(input()))
num = 0
for i in range(n-1, -1, -1):
    if k == 0:
        break
    if k<m[i]:
        continue
    num += k//m[i]
    k = k % m[i]
    
print(num)