'''
https://app.codility.com/programmers/lessons/5-prefix_sums/
[문제내용]
1. 배열 A는 입력받는다.
[0,1,0,1,1]
0의 의미는 오른쪽 방향으로 가는 차를 의미한다.
1의 의미는 왼쪽 방향으로 가는 차를 의미한다.

차들이 몇번 교차가 되는지 횟수를 구하는 문제이다.
첫번째 0은 [1,1,1] 3번을 교차하게 될거고
두번째 0은 [1,1] 2번을 교초하게될거다.
총 5번을 교차할 것임

[문제풀이]
# 1. 최초로 동쪽으로 가는 차를 찾자
# 2. 최초로 교차되는 시점부터 순회한다.
     이때 교차가 된다면(왼쪽으로 오는 차가 있다면) passing_car_num를 하고 오른쪽으로 가는 차가 있다면 east_car_numer를 1개씩 증가시킨다.
# 3. 10억번을 초과한다면 -1을 리턴한다.
'''


def solution(A):
    east_car_numer = 1
    passing_car_num = 0

    try:
        east_car = A.index(0)
    except:
        return 0

    for i in range(east_car + 1, len(A)):
        # 2. 교차가 된다면(왼쪽으로 오는 차가 있다면) passing_car_num를 하고
        if A[i] == 1:
            passing_car_num += east_car_numer
            # 3. 오른쪽으로 가는 차가 있다면 east_car_numer를 1개씩 증가시킨다.
            if passing_car_num > 1000000000:
                return -1
        else:
            # 2. 오른쪽으로 가는 차가 있다면 east_car_numer를 1개씩 증가시킨다.
            east_car_numer += 1
    return passing_car_num


print(solution([0, 1, 0, 1, 1]))
