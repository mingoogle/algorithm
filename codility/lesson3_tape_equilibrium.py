'''
https://app.codility.com/programmers/lessons/3-time_complexity/
[문제내용]
1. 배열 A를 입력 값으로 받는다.
2. 배열을 특정 번째 기준으로 나누면 2개의 배열이 생길텐데 2개의 배열의 차이값을 절대값으로 치환하여 [가장 최소의 값]을 출력해라
ex) [3,1,2,4,3] 인 경우 [3]-[1+2+4+3] -> |3-10| -> 7


[문제풀이]
# 1. 첫번쨰 위치부터 차례대로 두 배열 사이의 절대 값을 구한다.
'''


def solution(A):
    # 1. 배열의 요소가 2개라면 1번만 나눌 수 있다.
    if len(A) == 2:
        return abs(A[0] - A[1])

    # 2. 새로운 배열들어 두 배열 사이의 절대 값을 구한다.
    arr_ = []
    temp_1 = 0
    temp_2 = sum(A)

    for i in range(len(A) - 1):
        temp_1 = temp_1 + A[i]
        temp_2 = temp_2 - A[i]
        arr_.append(abs(temp_1 - temp_2))
    print(arr_)

    return min(arr_)


print(solution([3, 1, 2, 4, 3]))
