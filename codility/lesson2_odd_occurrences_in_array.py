'''
문제 - https://app.codility.com/programmers/lessons/2-arrays/
[문제내용]
1. 배열 A가 존재한다. A = [9,3,9,3,9,7,9]
2. 배열 A의 요소들 중에서 짝이 되지않는 값들을 출력해줘
- 9는 4개, 3은 2개, 7은 1개 -> 7은 홀수(짝이X)니 7을 응답한다.

[문제풀이]
분할정복법(divide and conquer) 으로 푼다.
- 큰문제를 -> 작은 문제로 쪼개고 -> 작은 문제들을 해결해서 -> 최종적으로 큰문제를 해결한다.

# 1. key/value 형태의 딕셔너리를 만든다.dict()
# 2. dict()에 요소들을 카운트한다.
# 3. 홀수인 값을 리턴한다.
'''


def solution(A):
    # 1. 딕셔너리를 만든다.
    dict_ = {}
    # 2. dict에 요소들을 카운트한다.
    for i in A:
        if i in dict_:
            dict_[i] += 1
        else:
            dict_[i] = 1

    print(dict_)
    # 3. 홀수인 값을 리턴한다.
    for i in dict_:  # key 값을 순회한다.
        if dict_[i] % 2 == 1:  # 홀수인 값을 찾는다.
            print('return i => ', i)
            return i


solution([9, 3, 9, 3, 9, 7, 9])
