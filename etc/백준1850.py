from math import gcd
import sys

a, b = map(int, input().split())


print("1"*gcd(a,b))