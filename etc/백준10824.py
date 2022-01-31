import sys

number = list(map(str, sys.stdin.readline().split()))

print(int(number[0]+number[1]) + int(number[2]+number[3]))


#살짝 다른 코드, 더 느림
# import sys
# a, b, c, d = map(str, sys.stdin.readline().split())
# print(int(a+b) + int(c+d))