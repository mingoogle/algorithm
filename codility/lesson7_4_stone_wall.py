'''
https://app.codility.com/programmers/lessons/7-stacks_and_queues/
[문제내용]
배열 H를 입력값으로 받는다.
H = [8,8,5,7,9,8,7,4,8]

각 배열은 각각의 건물의 높이를 의미한다.
같은 높이라면 하나의 블록을 만들 수 있다. 최소한의 블록의 개수는 몇개일까?

[문제풀이]
# 1. 블록의 수와 stack 배열을 선언한다.
# 2.
'''


def solution(H):
    # 1. 블록의 수와 stack 배열을 선언한다.
    block_count = 0
    stack_arr = []

    # 2. 건물을 순회하면서 기존 건물보다 작은 건물이 들어온다면 stack_arr를 작은 블록으로 초기화하고 하나의 블록으로 만드는건 끝났으니 block_count를 +1을 해준다
    for i in range(len(H)):
        while len(stack_arr) > 0 and stack_arr[-1] > H[i]:
            stack_arr.pop()

        if len(stack_arr) == 0 or stack_arr[-1] < H[i]:
            block_count += 1
            stack_arr.append(H[i])

    return block_count


print(solution([8,8,5,7,9,8,7,4,8]))

