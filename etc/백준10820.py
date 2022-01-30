import sys

sentence = []

while True:
    sentence = sys.stdin.readline().rstrip('\n')
    up = lo = num = sp = 0  #한 문자열이 끝날때마다 갱신
    if not sentence:
        break
    for i in sentence:
        if i.isupper() == True:
            up += 1
        elif i.islower() == True:
            lo += 1
        elif i.isdigit() == True:
            num += 1
        elif i.isspace() == True:
            sp += 1

    print(lo, up, num, sp)

    
    

    