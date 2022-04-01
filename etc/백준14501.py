# 퇴사...
# 오늘부터 n+1일째 되는날 퇴사하려고함.. 
# 그래서 남은 N일동안 최대한 많은 상담을 하려고함
# 비서는 하루에 하나씩 서로 다른 사람의 상담을 잡음
# 상담완료하는데 걸리는기간 Ti / 상담했을때 받을 수 있는 금액 Pi

n = int(input())
day = []
pay = []
dp = []
check = []
for i in range(n):
    t, p = map(int, input().split())
    day.append(t)
    pay.append(p)
    dp.append(p)
    
dp.append(0)

for i in range(n-1, -1, -1):
    if day[i] + i > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], pay[i]+dp[i+day[i]])
        
print(dp[0])
    