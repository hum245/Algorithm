import sys

stack_left = list(sys.stdin.readline().rstrip('\n'))
stack_right = []
print(stack_left, stack_right)
n = int(input())
cursor = len(stack_left)

for i in range(n):
    command = sys.stdin.readline().split()   
    if command[0] == 'L':
        if stack_left:
            stack_right.append(stack_left.pop())
            print(stack_left, stack_right)
    elif command[0] == 'D':
        if stack_right:
            stack_left.append(stack_right.pop())
            print(stack_left, stack_right)
    elif command[0] == 'B':
        if stack_left:
            stack_left.pop()
            print(stack_left, stack_right)
    elif command[0] == 'P':
        stack_left.append(command[1])
        print(stack_left, stack_right)
        
#print(''.join(stack_left + list(reversed(stack_right))))
print("".join(stack_left) + "".join(stack_right[::-1]))


# <시간초과 코드>

# import sys

# word = list(sys.stdin.readline().rstrip('\n'))
# n = int(input())

# cursor = len(word)

# for i in range(n):
#     command = sys.stdin.readline().split()   
#     if command[0] == 'L':
#         if cursor == 0:
#             continue
#         else:
#             cursor -= 1
#     elif command[0] == 'D':
#         if cursor == len(word):
#             continue
#         else:
#             cursor += 1
#     elif command[0] == 'B':
#         if cursor == 0:
#             continue
#         else:
#             del word[cursor-1]
#             cursor -= 1
#     elif command[0] == 'P':
#         word.insert(cursor, command[1])
#         cursor += 1
        
# for i in word:
#     print(i, end='')
    

