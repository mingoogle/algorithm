'''
https://app.codility.com/programmers/lessons/5-prefix_sums/
[문제내용]
배열 [S, P, Q]를 입력받는다.
S = [A,C,G,T]로 되어있는 문자열로 구성되어있다. A=1, C=2, G=3, T=4를 의미한다.
P = [2,5,0], Q[4,5,6] 처럼 P,Q는 같은 m만큼의 배열의 길이를 갖는다.

P,Q의 각 인덱스별로 문자열을 가져오고 가장 작은 값을 구해라
ex) p,q의 0번째인덱스는 [2,4]이다 스트링[2:4]까지 가져와서 최소값을 구해라

[문제풀이]
# 1. A(6)~B(11)을 순회하면서 2로 나누어떨어지는 걸 카운트한다.
'''


def solution(S, P, Q):
    M = len(P)

    return_arr = []

    for i in range(M):
        arr = S[P[i]:Q[i] + 1]
        print(arr)
        try:
            arr.index('A')
            return_arr.append(1)
        except:
            try:
                arr.index('C')
                return_arr.append(2)
            except:
                try:
                    arr.index('G')
                    return_arr.append(3)
                except:
                    arr.index('T')
                    return_arr.append(4)

    print('return_arr =>', return_arr)

    return return_arr


print(solution('CAGCCTA', [2, 5, 0], [4, 5, 6]))
