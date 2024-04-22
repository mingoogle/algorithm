'''
https://app.codility.com/programmers/lessons/5-prefix_sums/
[문제내용]

1. 정수 [A,B,K]를 입력 받는다.
A = 6, B = 11, K = 2
6~11사이에서 2로 나누어떨어지는 수의 개수를 구해라

[문제풀이]
# 1. A(6)~B(11)을 순회하면서 2로 나누어떨어지는 걸 카운트한다.
'''


def solution(A, B, K):
    # 1. A~B을 순회하면서 2로 나누어떨어지는 걸 카운트한다.
    # 단순 순회를 하면 성능이 안좋다.
    start_num = A / K
    end_num = int(B / K)

    if start_num % 1 != 0:
        start_num = int(start_num) + 1
    else:
        start_num = int(start_num)

    return end_num - (start_num - 1)


print(solution(6, 11, 2))
