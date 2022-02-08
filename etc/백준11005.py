# from string import ascii_uppercase


# alphabet = list(ascii_uppercase)

# N, B = map(int, input().split())
# arr=[]
# while N!=0:
#     if N%B >= 10:
#         arr.append(alphabet[(N%B)-10])
#     else:
#         arr.append(N%B)        
#     N = N//B
    

# for i in reversed(arr):
#     print(i, end='')



# <속도 향상을 위해 다시 푼 문제> 

N, B = map(int, input().split())
arr=[]
while N!=0:
    if N%B >= 10:
        arr.append(chr(65 + (N%B) - 10))
    else:
        arr.append(N%B)        
    N = N//B
    

for i in reversed(arr):
    print(i, end='')