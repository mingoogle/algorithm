'''
https://app.codility.com/programmers/lessons/7-stacks_and_queues/
[문제내용]
문자열 S를 받는다.
S = (()(())())
정상적인 모양인지 확인한다.
정상적이라면1, 비정상적이라면 0을 리턴한다.

[문제풀이]
# 1. 정상적인 모양인지 검증한다.
# 2. '(' 많은 상황과 or ')'이 많은 상황을 고려해서 1 또는 0을 리턴한다.
'''


def solution(S):
    # empty
    if S == '':
        return 1

    sum = 0;
    for i in S:
        if i == '(':
            sum += 1
        else:
            sum -= 1
            if sum < 0:
                return 0
    if sum == 0:
        return 1
    else:
        return 0


def solution2(S):
    arr = []
    for i in range(len(S)):
        if S[i] == '(':
            arr.append(S[i])
        else:
            if len(arr) != 0 and arr[-1] == '(':
                del arr[-1]
            else:
                arr.append(S[i])

    if len(arr) == 0:
        return 1
    else:
        return 0

