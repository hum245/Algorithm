import sys

n = int(sys.stdin.readline())

array = []

for i in range(n):
    array.append(list(map(int, sys.stdin.readline().split())))

array.sort()

for i in range(n):
    print(array[i][0], array[i][1])

