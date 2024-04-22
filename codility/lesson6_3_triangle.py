'''
https://app.codility.com/programmers/lessons/6-sorting/
[문제내용]
1. 배열 A는 입력받는다.
A = [10,2,5,1,8,20]

2. 위의 배열이 트라이앵글이라면 1, 아니라면 0을 리턴해라

트라이앵글이란?
- 배열의 순서에 상관없이 3개의 값을 고르고, 모든 상황에서 2개의 합이 1개의 값보다 큰 경우 트라이앵글이라고 한다.

[문제풀이]
# 1. 정렬을 한다.
# 2. 제일 작은 수2(a,b)개가 제일 큰수(c)가 있는 경우 a+b > c의 조건에 맞는지만 검증하면됨
'''


def solution(A):
    # 1. set을 이용해서 중복을 제거한다.
    A = sorted(A)

    print(A)
    # 2. 제일 작은 수2(a,b)개가 제일 큰수(c)가 있는 경우 a+b > c의 조건에 맞는지만 검증하면됨
    for i in range(len(A)-2):
        if A[i] + A[i+1] > A[i+2]:
            return 1
    return 0

print(solution([10,2,5,1,8,20]))
