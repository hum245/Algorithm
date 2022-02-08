from curses.ascii import isdigit

n, b = input().split()

n = ''.join(n[::-1])
b = int(b)

sum = 0
for i in range(len(n)):
    if n[i].isdigit() :
        sum += int(n[i]) * (b**i)
    else :
        sum += (ord(n[i])-55) * (b**i)  
        
        
print(sum)
        