from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())
person = [i for i in range(1, n+1)]
index = 0
result = []

while person:
    index += k-1
    if index >= len(person):
        index = index%len(person)
    
    result.append(person.pop(index))


print("<", ', '.join(map(str, result)), ">", sep="")

