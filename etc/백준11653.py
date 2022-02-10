n = int(input())
    
# for i in range(2, n+1):
#     if n % i == 0:
#         while n % i == 0:
#             print(i)
#             n = int(n/i)
  
i = 2
while n!=1:
    if n%i==0:
        print(i)
        n = n//i
    else:
        i+=1
