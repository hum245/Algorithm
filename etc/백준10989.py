# <메모리 초과 코드>

# import sys

# n = int(input())
# array = []

# for i in range(n):
#     array.append(int(sys.stdin.readline()))

# array.sort()

# for i in array:
#     print(i)


import sys

n = int(input())

array = [0]*10001

for i in range(1, n+1):
    array[int(sys.stdin.readline())] += 1

for i in range(10001):
    if array[i] != 0:
        for j in range(array[i]):
            print(i)