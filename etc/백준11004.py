import sys

n, k = map(int, input().split())

array = list(map(int, sys.stdin.readline().split()))

array.sort()

print(array[k-1])
