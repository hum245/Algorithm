n = int(input())

wine = []
for i in range(n):
    wine.append(int(input()))

memo = [0]*n
memo[0] = wine[0]

for i in range(1, n):
    if i == 1:
        memo[1] = wine[0]+wine[1]
    elif i == 2:
        memo[2] = max(wine[i-2]+wine[i], wine[i-1]+wine[i], memo[1])
    else :
        memo[i] = max(memo[i-3]+wine[i-1]+wine[i], memo[i-2]+wine[i], memo[i-1])

print(memo[n-1])

