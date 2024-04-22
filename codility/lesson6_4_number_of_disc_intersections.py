'''
https://app.codility.com/programmers/lessons/6-sorting/
[문제내용]
디스크가 여러개가 존재하는데 디스크간에 서로 몇개가 포함이 되는지를 구하는 문제
A = [1,5,2,1,4,0]

[문제풀이]
# 1. 배열을 순회하면서 오른쪽, 왼쪽 방향에 대한 배열을 만든다.
'''


def solution(A):

    arr = []
    for i, v in enumerate(A):
        # 1. 배열을 순회하면서 오른쪽, 왼쪽 방향에 대한 배열을 만든다.
        arr.append((i+v, 1))
        arr.append((i-v, -1))
    arr.sort()
    print(arr)

    # 2. intersect 교차될떄 카운트 수, intervals 원이 열린개수
    intersect = 0
    intervals = 0

    for i,v in enumerate(arr):
        if v[1] == 1:
            intervals -= 1
        if v[1] == -1:
            intersect += intervals
            intervals += 1

    if intersect > 10000000:
        return -1

    return intersect

print(solution([1,5,2,1,4,0]))
