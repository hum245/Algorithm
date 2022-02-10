check = [True * i for i in range(1000000)]

for i in range(2, 1001):
    if check[i] == True:
        for j in range(i+i, 1000001, i):
            check[j] = False
            
while True:
    n = int(input())
    if n==0:
        break

    a = 0
    b = n
    for _ in range(1000000):
        if check[a] and check[b]:
            print()