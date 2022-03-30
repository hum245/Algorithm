# 시험장 n개
# 총감독관 - B명 응시가능 / 부감독관 - C명 응시가능
# 각 시험장에 총감동관 1명(필), 부감독관 여러명 가능 
# 모든 응시생 감시... 필요간 감독관 수 최솟값은? 
# 뭐지 완탐인가 

def solution(n, person, b, c):
    count = 0

    for i in range(n):
        temp = person[i] - b
        count += 1
        if temp>0:
            count += temp // c
            if temp % c:
                count+=1
                
    return count
            
            
n = int(input())
person = list(map(int, input().split()))
b, c = map(int, input().split())

print(solution(n, person, b, c))
