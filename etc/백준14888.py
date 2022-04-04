
def dfs(cnt, result, plus, minus, multiply, divide):
    global max_result
    global min_result
    if cnt == n:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
    if plus > 0:
        dfs(cnt+1, result + number[cnt], plus-1, minus, multiply, divide)
    if minus > 0:
        dfs(cnt+1, result - number[cnt], plus, minus-1, multiply, divide)
    if multiply > 0:
        dfs(cnt+1, result * number[cnt], plus, minus, multiply-1, divide)
    if divide > 0:
        dfs(cnt+1, -(-result // number[cnt]) if result<0 else result // number[cnt],
            plus, minus, multiply, divide-1)
        
        
        
n = int(input())
number = list(map(int, input().split()))
plus, minus, multiply, divide = map(int, input().split())
arr = []
max_result = -99999999999
min_result = 99999999999
dfs(1, number[0], plus, minus, multiply, divide)

print(max_result)
print(min_result)