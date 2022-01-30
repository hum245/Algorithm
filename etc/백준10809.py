# 첫번째 성공 코드
word = list(input())

for i in range(97, 123):
    try:
        print(word.index(chr(i)))
    except ValueError :
        print(-1)


# # 참고 코드
# word = input()
# alphabet = list(range(97, 123))

# for i in alphabet:
#     print(word.find(chr(i)))

        #index는 찾는 문자가 없을경우 ValueError를 발생시키지만, find함수는 -1을 출력한다.
        #find가 해당 문제의 조건에서는 더 간단함! 