# 암호만들기
# 서로 다른 L개의 알파벳 소문자들로 구성되며 최소 1개의 모음과 최소 2개의 자음으로 구성되어있음
# 알파벳이 순서대로 배열되어있음 abc(O) bac(X)
# 암호로 사용했을 법한 문자의 종류가 C가지가 있다고한다. 가능성있는 암호들을 모두 구하는 프로그램을 작성해바

# 조건 첫번째 줄 두 정수 L,C가 주어진다 ( 3<=L<=C<=15)
# 다음 줄에는 C개의 문자들이 주어지며 공백으로 구분한다.
# 주어진 문자들은 소문자이며, 중복되는 것은 없다.
# 각 줄에 하나씩, 사전식으로 가능성 있는 암호를 모두 출력한다 ( 엔터쳐라 )

# p01 입력예시
# 4 6 => 4가 총 암호자릿수 6은 문자의 종류(개수)
# a t c i s w => 문자의 개수의 실체

from itertools import combinations

vowels = ('a','e','i','o','u')
l,c = map(int, input().split()) #첫번쨰 입력했을때

# 암호를 사전식으로 출력해야하니 입력 이후에 정렬 수행
array = input().split(' ') # 두번째입력했을때
array.sort()

for password in combinations(array, l):
    # 모음의 개수를 세기
    count = 0
    for i in password:
        if i in vowels:
            count +=1
    if count >= 1 and count <= l -2:
        print(''.join(password))