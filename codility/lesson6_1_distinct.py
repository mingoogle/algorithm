'''
https://app.codility.com/programmers/lessons/6-sorting/
[문제내용]
1. 배열 A는 입력받는다.
A = [2,1,1,2,3,1]

2. 중복을 제거하고 남은 개수를 구해라

[문제풀이]
# 1. set을 이용해서 중복을 제거한다.
# 2. 중복을 제거한 set데이터의 개수를 구한다.
'''


def solution(A):
    # 1. set을 이용해서 중복을 제거한다.
    A = set(A)

    # 2. 중복을 제거한 set데이터의 개수를 구한다.
    return len(A)


print(solution([2,1,1,2,3,1]))
