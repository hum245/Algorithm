import sys

word = list(sys.stdin.readline())

for i in range(97, 123):
    print(word.count(chr(i)))