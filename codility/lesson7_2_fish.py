'''
https://app.codility.com/programmers/lessons/7-stacks_and_queues/
[문제내용]
입력값으로 배열 A와 배열 B를 받는다.
A = [4,3,2,1,5], B = [0,1,0,0,0]

1. 0은 위쪽으로 움직이는 물고기, 1은 아래쪽으로 움직이는 물고기
2. A에 입력값은 물고기의 크기를 의미한다.

충돌(교차)하는 상황에서 더 크기가 큰 물고기 살아남는다.
살아남은 물고기의 개수는 몇개인가?

[문제풀이]
# 1. (물고기 크기, 방향성)을 가지는 이차원 배열을 하나 생성한다.
# 2. 첫번째 물고기를 초기화한다.
# 3. 쎈 물고기는 계속 살아남으니 while절을 한다.
'''


def solution(A,B):
    if len(A) == 1:
        return 1
    # 1. (물고기 크기, 방향성)을 가지는 이차원 배열을 하나 생성한다.
    arr = []
    for i in range(len(A)):
        arr.append((A[i], B[i]))

    # 2. 첫번째 물고기를 초기화한다.
    arr_ = []
    arr_.append(arr[0])

    # 3. 쎈 물고기는 계속 살아남으니 while절을 한다.
    for i in range(1, len(arr)):
        while(True):
            # 충돌을 한다면 작은 물고기는 없앤다.
            if arr[i][1] == 0 and arr_[len(arr_)-1][1] == 1:
                # 기존 물고기가 더 쎄면
                if arr[i][0] < arr_[len(arr_)-1][0]:
                    break
                # 새로운 물고기가 더쎄면
                else:
                    del arr_[len(arr_)-1]
                    if (len(arr_) == 0):
                        arr_.append(arr[i])
                        break
            else:
                arr_.append(arr[i])
                break

    return len(arr_)


print(solution([4,3,2,1,5], [0,1,0,0,0]))
