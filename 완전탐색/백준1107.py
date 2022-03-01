# n = list(map(int, str(input())))
# m = int(input())
# if m == 0:
#     print(len(n))
#     exit()
    
# broken = list(map(int, input().split()))
# button = [0,1,2,3,4,5,6,7,8,9]
# button = [x for x in button if x not in broken]
# button.sort()
# count = 0
# temp = []

# m = int(''.join(map(str, n)))

# if m == 100:
#     print(0)
    
# elif len(button) == 0:
#     print(abs(100-m))

# elif len(button) == 1 and button[0] == 0:
#     print(m + 1)
# else:
#     for i in range(len(n)):
#         if n[0] == 0:
#             count+=1
#             temp.append(min(button))
#         elif n[i] in button and n[i] > 0:
#             count += 1
#             temp.append(n[i])
#         else:
#             if n[i] == 0 and n[0] not in button:
#                 count+=1
#                 temp.append(max(button))
#             elif n[i]<=5 and n[i]>0 and i!= 0:
#                 count += 1
#                 temp.append(min(button))
#             elif n[i] == 0 and n[0] in button:
#                 count += 1
#                 temp.append(min(button))
#             else:
#                 count += 1
#                 temp.append(max(button))
    
#     temp = ''.join(map(str, temp))
#     n = ''.join(map(str, n))
#     count += abs(int(temp) - int(n))

#     if abs(100-m) < count:
#         print(abs(100-m))
#     else:
#         print(count)
    
    
target = int(input())
ans = abs(100 - target) # ++ or -- 로 이동할 경우 -> 최댓값
M = int(input())
if M: # 고장난게 있을 경우만 인풋을 받음
    broken = set(input().split())
else:
    broken = set()

# 작은수에서 큰수로 이동할땐 500,000 까지만 보면 되지만
# 반대로 큰수에서 작은수로 내려올수도 있으므로 1,000,000 까지 봐야함
for num in range(1000001): 
    for N in str(num):
        if N in broken: # 해당 숫자가 번호를 눌러서 만들 수 없는 경우엔 스탑
            break
    else: # 번호를 눌러서 만들 수 있는 경우엔
        # min(기존답, 번호를 누른 횟수 + 해당 번호로부터 타겟까지의 차이)
        ans = min(ans, len(str(num)) + abs(num - target))

print(ans)