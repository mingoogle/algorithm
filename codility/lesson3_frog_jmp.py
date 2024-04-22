'''
https://app.codility.com/programmers/lessons/3-time_complexity/
[문제내용]
총 입력값으로 양수 [X,Y,X]의 값을 입력받는다.
X = 10,
Y = 85
D = 30

현재 개구리의 위치는 10(X)이며, 85(Y)까지 이동해야한다. 한번에 30(D)만큼 점프를 할 수 있다. 몇 번 점프를 해야 85(Y)까지 도달할까?
1번 점프하는 경우 10+30 = 40
2번 점프하는 경우 10+30+30+ = 70
3번 점프하는 경우 10+30+30+30+ = 100 => 적어도 3번은 점프해야 Y값에 도달한다.

[문제풀이]
# 1. (Y-X)/D로 도달하는 점프 횟수를 구하면된다.
# 실수값이 나올 수 있기때문에 올림처리를 해준다.
'''


def solution(X, Y, D):
    # 1. (Y-X)/D로 도달하는 점프 횟수를 구하면된다.
    a = (Y - X) / D
    print(a)

    # 실수값이 나올 수 있기때문에 올림처리를 해준다.
    if a % 1 == 0:
        return int(a)
    else:
        return int(a) + 1


solution(10, 85, 30)
