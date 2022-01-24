import sys

n = int(input())
array = []

for i in range(n):
    name, ko, en, math_score = sys.stdin.readline().split()
    array.append([name, int(ko), int(en), int(math_score)])

array.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(n):
    print(array[i][0])
