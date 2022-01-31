# #<유클리드 호제법 사용>
A, B = map(int, input().split())
a, b = A, B
while b != 0:
    a = a%b
    a, b = b, a

print(a)
print(A*B//a)


#<math 라이브러리 사용>
# from math import gcd
# a, b = map(int, input().split())
# print(gcd(a, b))
# print(a*b//gcd(a,b))



