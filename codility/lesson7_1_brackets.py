'''
https://app.codility.com/programmers/lessons/7-stacks_and_queues/
[문제내용]
1. S라는 문자열을 받는다.
S = {[()()]}

대괄호, 중괄호, 소괄호가 문법에 맞게 잘열리고 잘닫혔는지 판단해줘
정상적이라면 1, 문법이 틀렸다면 0응 리턴해라

[문제풀이]
# 1. 괄호를 숫자로 만든다.
# 2. 순회를 하면서 정상적으로 닫히거나, 닫힌값이
'''


def solution(S):
    if(len(S) == 0):
        return 1

    arr = []
    for i in S:
        if i == "{":
            arr.append(3)
        elif i == "}":
            arr.append(-3)
        elif i == "[":
            arr.append(2)
        elif i == "]":
            arr.append(-2)
        elif i == "(":
            arr.append(1)
        elif i == ")":
            arr.append(-1)
    print('arr', arr)

    arr_ = []
    arr_.append(arr[0])

    print('### start arr_ =>', arr_)
    for i in range(1, len(arr)):
        print('### for arr_ =>', arr_)
        print('### for arr[i] =>', arr[i])
        if len(arr_) != 0 and arr[i] < 0 and arr[i] == -1 * arr_[len(arr_)-1]:
            del arr_[len(arr_)-1]
        else:
            arr_.append(arr[i])

    if(len(arr_) == 0):
        return 1
    else:
        return 0


print(solution('{[()()]}'))
