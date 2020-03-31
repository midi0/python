'''
세트 만들기
fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
세트는 요소의 인덱스가 정해져있지 않아서
매 출력시마다 요소의 순서가 다르게 나온다.
또 , 세트의 요소는 중복이 불가능

세트에 같은 요소를 두번 넣어도 실제론 하나만 들어간다
fruits = {'orange', 'orange', 'cherry'}

튜플, 딕셔너리와 달리 [] 로 특정 요소를 출력할 수는 없다.
print(fruits[0])

세트의 특정 값 확인하기
'orange' in fruits
'peach' not in fruits

set를 이용하여 세트 만들기
a = set('apple') # a p l e만 세트로 만들어짐 (중복인 p는 하나만)
b = set(range(5)) # 0 1 2 3 4
c = set() # 빈 세트생성 c = {}를 쓰면 딕셔너리로 생성되므로 주의
d = set('안녕하세요') # 안/녕/하/세/요 랜덤하게 요소출력

프로즌 세트 (내용을 변경할 수 없는 세트)
 a = frozenset(range(10))  요소의 추가 삭제 연산이 불가능

세트 안에 세트를 넣고 싶을때 사용한다
a = frozenset({frozenset({1, 2}), frozenset({3, 4})})
'''
a = frozenset({frozenset({1, 2}), frozenset({3, 4})})
print(a)