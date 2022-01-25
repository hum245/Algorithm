import sys
n = int(input())

stack = []
for i in range(n):
    command = list(map(str, sys.stdin.readline().split()))

    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1]) #stack.pop()을 하면 배열에서 빼내버림.... 그냥 출력하는거니까 이렇게해줘야함 