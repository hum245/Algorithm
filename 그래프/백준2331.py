a, p = map(int, input().split())

a2 = list(map(int, str(a)))
temp = 0
for i in range(len(a2)):
    temp += a2[i] ** p
    
d = [a, temp]
i = 2
while True:    
    temp = list(map(int, str(d[i-1])))
    temp2 = 0
    for j in range(len(temp)):
        temp2 += temp[j]**p
    
    if temp2 in d:
        break
    d.append(temp2)
    i+=1
    
    
print(d.index(temp2))