'''
https://app.codility.com/programmers/lessons/5-prefix_sums/
[문제내용]
입력 값으로 배열 A를 입력 받는다.
A = [4,2,2,5,1,5,8]
    (0,1,2,3,4,5,6]

P,Q는 A 배열의 원소값 사이를 의미한다.
P = 1, Q=2 이면 A원소의 1~2번째에 있는 값의 평균값을 구한다 = 2/2 = 1

[문제풀이]
# 1. a<=b 인 경우 a,b의 평균은 a보다 큰 수가 나온다는 특성이 있다.
위의 특성을 고려하면 아래의 결론을 지을 수 있다.
-> (a,b,c,d)를 A(ab) <= B(cd)라면 [ab]보다 큰수가 나올 것이고
-> (a,b,c,d)를 A(ab) >= B(cd)라면 [cd]보다 큰수가 나올 것이고

# 2. 만약에 (a,b,c)의 경우 범위를 ab 와 c로 나눌 수는 없으니 3가지 경우의 수를 모두 봐야한다.
'''


def solution(A):
    # 1. a<=b 인 경우 a,b의 평균은 a보다 큰 수가 나온다는 특성을 이용한다.
    min_value = sum(A[0:2]) / 2
    min_index = 0

    for i in range(len(A)):
        try:
            if min_value > (A[i + 1] + A[i]) / 2:
                min_value = (A[i + 1] + A[i]) / 2
                min_index = i

            # 2. 만약에 (a,b,c)의 경우 범위를 ab 와 c로 나눌 수는 없으니 3가지 경우의 수를 모두 봐야한다.
            if min_value > (A[2 + i] + A[1 + i] + A[i]) / 3:
                min_value = (A[2 + i] + A[1 + i] + A[i]) / 3
                min_index = i
        except:
            break
    return min_index


print(solution([4, 2, 2, 5, 1, 5, 8]))
