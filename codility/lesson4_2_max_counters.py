'''
https://app.codility.com/programmers/lessons/4-counting_elements/
[문제내용]
1. 정수 N과 배열 A를 입력받는다.
- N = 5, A[3,4,4,5,1,4,4]

2. N만큼의 배열을 만든다.

3. 배열의 원소값에 해당하는 N배열의 위치 값을 +1을 한다.
4. 만약 배열의 요소보다 1높은(6)의 값이 들어있다면 현재 기준에서 가장큰 max_counter값으로 모든 원소의 값을 변경한다.

[문제풀이]
# 1. 배열 A를 순회를 하면서 N만큼의 배열에 카운트를 해준다.
# 2. 6이 들어오면 배열의 원소 값중 제일 큰값으로 초기화한다.
'''


def solution(N, A):
    # 1. 카운터해야할 counters 배열을 선언하고
    # 2. 6이 들어오게되면 모든 배열에 값을 max_counter로 바꿔주는 작업을 하기위해 next_max_counter와 max_counter를 선언한다.
    counters = N * [0]
    next_max_counter = 0
    max_counter = 0

    # 3. counters 배열에 카운트한다.
    for i in A:
        try:
            current_counter = counters[i - 1] = max(counters[i - 1] + 1, max_counter + 1)
            next_max_counter = max(current_counter, next_max_counter)
        except:
            max_counter = next_max_counter

    # 4. 순회를 하면서 max_counter가 적용되어야하는데 적용되지 못한 원소가 있다면 적용한다.
    for i in range(len(counters)):
        if max_counter > counters[i]:
            counters[i] = max_counter

    return counters


print(solution(5, [3, 4, 4, 6, 1, 4, 4]))
