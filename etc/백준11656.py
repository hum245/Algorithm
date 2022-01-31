import sys

word = sys.stdin.readline()
result = []

for i in range(len(word)-1):
    result.append(word[i:-1])

result.sort()

for i in result:
    print(i)
    
