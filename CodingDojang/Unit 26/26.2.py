'''
집합 연산 사용하기
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = set.union(a,b)
합집합 연산
print(a | b) # 123456
print(c) # 123456

교집합 연산
c = set.intersection(a,b)
print(a&b)
print(c)

차집합
c = set.difference(a,b)
print(a-b)
print(c)

대칭 차집합
c = set.symmetric_difference(a,b)
print(a^b)
print(c)

집합 연산 후 할당 연산자 사용하기
a |= {5}
a.update({6})

&=은 현재 세트와 다른 세트 중에서 겹치는 요소만 현재 세트에 저장하며
intersection_update 메서드와 같습니다
a = {1, 2, 3, 4}
a &= {0,1,2,3,}

-=은 현재 세트에서 다른 세트를 빼며 difference_update 메서드와 같습니다.
a = {1, 2, 3, 4}
a -= {0,1,2,3,} # print(a) 하면 4만 출력

^=은 현재 세트와 다른 세트 중에서 겹치지 않는 요소만 현재 세트에 저장하며
symmetric_difference_update 메서드와 같습니다.
a = {1, 2, 3, 4}
a ^= {3,4,5,6} # 1 2 5 6출력

부분 집합과 상위 집합 확인하기
b = a.issubset({1,2,3,4,5})
print(a<={1, 2, 3, 4})

세트가 같은지 다른지 확인하기
print(a == {1,2,3,4}) # True
print(a == {4,3,1,2}) # True
세트는 요소의 순서가 정해져있지 않으므로 내부 요소만 같으면 True이다
a != {1,2,3} # a는 1234를 가지고있으므로 True 출력

disjoint는 현재 세트가 다른 세트와 겹치지 않는지 확인합니다
a.isdisjoint({5,6,7}) # 겹치는게 없으므로 True 반환
a.isdisjoint({2,3,5}) # 2 3 이 겹치므로 False
'''
a = {1, 2, 3, 4}
print(a.isdisjoint({5,6,7}))
