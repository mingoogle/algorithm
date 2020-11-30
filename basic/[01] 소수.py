# -*- coding: utf-8 -*-
# Question : 과연 에라토스테네스의 체가 만능일까?

# 소수란?
# 2보다 큰 자연수 중에서 1과 자기 자신을 제외한 자연수로는 나뉘어 떨어지지 않는 자연수
# => 자기 자신 값보다 작은 값들을 차례대로 대입하면서 안나눠지면 소수겠다. ( 조건 : 2보다 크면서 1을 제외한 작은 값들 )


# O(x) => x값을 기준으로 작은 값들을 순차적으로 실행하기 때문에 x양이 커질수록 오래걸린다. ex) 10000개 일때 10000개를 다검사
def is_prime_number(x):
    # 2부터 x보다 작은 값을 확인한다. range(시작값,끝값) : 시작값부터 끝값-1까지 반복한다. => 2부터 x-1까지 반복
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

print(is_prime_number(5))
print(is_prime_number(6))
print(is_prime_number(7))


# O(x) 보다 효율적으로 처리하기위해서 x값의 제곱근 값까지만 계산하면 된다. ex) 10000개 일때 1000개만 검사
# 8의 약수는 1x8 2x4 | 4x2 8x1 => 즉, 약수들은 대칭을이루기때문에 반만 검사하면된다. 반만(제곱근)
# O(x1/2)
import math

def is_prime_number2(x):
    # 2부터 x의 제곱근까지의 수들만 확인
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

print(is_prime_number2(4));
print(is_prime_number2(7));


# 에라토스테네스의 체 O(NloglogN)
# 1. 2부터 N까지의 모든 자연수를 나열한다.
# 2. 남은 수 중 아직 처리하지 않은 가장 작은 수 i를 찾는다.
# 3. 남은 수 중에서 i의 배수를 모두 제거한다 (i는 제거 X)
# 4. 더 이상 반복할 수 없을 때까지 2,3번을 반복한다.

# @@ 에라토스테네스의 체는 매우 빠르게 동작한다. 하지만 단점은??
# 보면 리스트를 생성한다. n값이 클수록 리스트가 커지기때문에 메모리가 많이 필요해진다.
# 따라서 10억 이상의 소수를 찾으려면 에라토스테네서의 체를 이용하긴 어렵다. ( 이론상 400만번정도 연산가능하기때문에 n값이 100만이내일경우 사용하자 )

n = 10
array = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n))+1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i*j] = False
            j += 1

for i in range(2, n+1):
    if array[i]:
        print(str(i))
