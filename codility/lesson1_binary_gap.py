'''
문제 - https://app.codility.com/programmers/lessons/1-iterations/
[문제내용]
1. 양수 N이 존재한다.
2. N을 이진수로 변환한 값에서 1과 1사이의 0의 개수를 카운트 한다.
3. 이때 가장 큰 0의 개수를 구해라

[문제풀이]
분할정복법(divide and conquer) 으로 푼다.
- 큰문제를 -> 작은 문제로 쪼개고 -> 작은 문제들을 해결해서 -> 최종적으로 큰문제를 해결한다.

# 1. 양수 N을 이진수로 변환한다.
# 2. 변환된 이진수에서 1들의 위치를 찾아서 배열에 넣는다.
# 3. 배열의 값들을 비교해서 가장 큰 값을 응답한다.
'''


def solution(N):
    # 1. 양수 N을 이진수로 변환한다.
    binary_num = bin(N)
    # 2. 변환된 이진수에서 1들의 위치를 찾아서 배열에 넣는다.
    arr_ = []
    for i in range(2, len(binary_num)):
        if binary_num[i] == '1':
            arr_.append(i)
    # 3. 배열의 값들을 비교해서 가장 큰 값을 응답한다.
    max = 0
    for i in range(0, len(arr_) - 1):
        # [개선 포인트] gap = arr_[i+1] - arr_[i] - 1로 하면 abs()를 안써도 된다.
        gap = abs(arr_[i] - arr_[i + 1]) - 1
        if (gap > max):
            max = gap;
    print('### binary_num =>', binary_num)
    print('### max =>', max)
    return max
