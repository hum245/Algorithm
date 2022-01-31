word = list(input())

result = []
for i in word:
    if i.isupper() == True:
        if ord(i)+13 <= 90:
            result.append(chr(ord(i) + 13))
        else:
            result.append(chr(ord(i) - 13))
    
    elif i.islower() == True:
        if ord(i)+13 <= 122:
            result.append(chr(ord(i) + 13))
        else:
            result.append(chr(ord(i) - 13))
    else:
        result.append(i) #띄어쓰기 꼭 추가해줘야함

for i in result:
    print(i, end='')