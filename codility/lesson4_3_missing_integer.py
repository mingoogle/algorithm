'''
https://app.codility.com/programmers/lessons/4-counting_elements/
[문제내용]
 중간에 빠져있는 양의 정수 추출하기

1. 배열 A를 입력 받는다.
A = [1,3,6,4,1,2] 5가 없으니 5를 리턴
A = [1,2,3] 이라면 다음 값인 4를 리턴
정수이기 때문에 A= [-1,-3]이 들어올 수 있다 이때 1을 리턴한다.


[문제풀이]
# 1. 중복을 제거하기위해서 set을 한다.
# 2. set한 값을 배열로 만들고 정렬한다.
# 3. 처음 양의 정수를 찾고나서 순차적으로 탐색해 빠져있는 양의 정수를 구한다.
# 4. 빠진 원소 값이 없다면 다음 값을 리턴
# 5. 음수만 존재한다면 1을 리턴
'''


def solution(A):
    # 1. 중복을 제거하기위해서 set을 한다.
    A = set(A)
    # 2. set한 값을 배열로 만들고 정렬한다.
    A = sorted(A)

    try:
        # 3. 처음 양의 정수를 찾고나서 순차적으로 탐색해 빠져있는 양의 정수를 구한다.
        a = A.index(1)
        tmp = A[a:]
        b = 1
        for i in tmp:
            if i == b:
                b += 1
            else:
                return b
        # 4. 빠진 원소 값이 없다면 다음 값을 리턴
        return b
    except:
        # 5. 음수만 존재한다면 1을 리턴
        return 1


print(solution([1, 3, 6, 4, 1, 2]))
