import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
person = deque([i for i in range(1, n+1)])
result = []

while person:
    person.rotate(-k+1)
    result.append(str(person.popleft()))

sys.stdout.write("<"+", ".join(result)+">")