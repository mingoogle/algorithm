'''
https://app.codility.com/programmers/lessons/6-sorting/
[문제내용]
입력값으로 배열 A를 입력 받는다.
A = [-3,1,2,-2,5,6]

이때 3가지 값을 아무거나 골라서 제일 큰값을 구해주면된다.

[문제풀이]
# 1. 정렬을한다.
# 2. 음수인 상황을 고려해서 최소의 음수*음수와 양의 정수 최대값 vs 양의 정수 최대값 중 큰 값을 리턴한다.
'''


def solution(A):
    # 1. 정렬을한다.
    A = sorted(A, reverse=True)

    # 2. 음수인 상황을 고려해서 최소의 음수*음수와 양의 정수 최대값 vs 양의 정수 최대값 중 큰 값을 리턴한다.
    return max(A[0]*A[1]*A[2], A[0]*A[-1]*A[-2])

print(solution([-3,1,2,-2,5,6]))
