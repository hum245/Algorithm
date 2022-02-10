#<시간초과 코드>
# def isPrime(n):
#     if n == 1:
#         return False
#     for i in range(2, n):
#         if n%i == 0:
#             return False
        
#     return True


# M, N = map(int, input().split())

# for i in range(M, N+1):
#     if isPrime(i) == True:
#         print(i)
#     else:
#         continue
                

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
        
    return True


M, N = map(int, input().split())

for i in range(M, N+1):
    if isPrime(i) == True:
        print(i)
    else:
        continue
                