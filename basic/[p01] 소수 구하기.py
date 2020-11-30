# 에라토스테네스의 체
# 첫째 줄에 M과 N이 빈칸을 사이에 두고 주어ㅣㄴ다 ( 1<=M <=N <= 1000000
# 한 줄에 하나씩 증가하는 순서대로 소수를 출력한다 ( 엔터쳐야되 )

import math

m,n = map(int, input().split())

array = [True for i in range(1000001)]
array[1] = 0 # 1은 소수가아니야

for i in range(2, int(math.sqrt(n))+1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i*j] = False
            j += 1


for i in range(m, n+1):
    if array[i]:
        print(i)