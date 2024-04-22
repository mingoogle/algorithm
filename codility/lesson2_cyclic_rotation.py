'''
문제 - https://app.codility.com/programmers/lessons/2-arrays/
[문제내용]

[문제풀이]
분할정복법(divide and conquer) 으로 푼다.
- 큰문제를 -> 작은 문제로 쪼개고 -> 작은 문제들을 해결해서 -> 최종적으로 큰문제를 해결한다.

# 1. 배열 A만큼의 길이를 갖는 배열 B를 생성한다.
# 2. K만큼 이동한 값을 배열 B에 저장한다.
'''


def solution(A, K):
    # 1. 배열 A만큼의 길이를 갖는 배열을 생성한다.
    arr_ = list(range(len(A)))

    # 2. K만큼 이동한 값을 배열 B에 저장한다.
    # (i+K)%len(A) -> i+K를 한 값이 배열의 길이를 넘어간다면 맨 처음으로 이동을 시켜야하기때문에 %(나머지)로 처리한다.
    for i in range(len(A)):
        arr_[(i + K) % len(A)] = A[i]
    return arr_


solution([1, 2, 3, 4, 5], 3)
