'''
딕셔너리에 키, 기본 값 저장하기
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.setdefault('e')
x.setdefault('f',100)

딕셔너리에 키의 값 수정
update는 키-값 쌍 여러 개를 콤마로 구분해서 넣어주면 값을 한꺼번에 수정할 수 있습니다.
x.setdefault('e')
x.update(e=50)
x.update(a=900, f=60)

update(키=값)은 키가 문자열일 때만 사용할 수 있습니다.
만약 키가 숫자일 경우에는 update(딕셔너리)처럼
딕셔너리를 넣어서 값을 수정할 수 있습니다.
y = {1: 'one', 2: 'two'}
y.update({1: 'ONE', 3: 'THREE'})
print(y)

리스트와 튜플을 이용
y = {1: 'one', 2: 'two'}
y.update([[2,'two'],[4,'FOUR']])
print(y)

y = {1: 'one', 2: 'two'}
y.update(zip([3,4],['three','four']))

setdefault ㅡ 이미 들어온 키의 값은 수정 불가
update ㅡ 들어와있는 키의 값 수정가능
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.setdefault('a', 90) // a의 값이 변경되지 않는다.

키-값 삭제하기
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.pop('a')
또는
del x['a']

딕셔너리의 모든 키/값 삭제
x.clear()

딕셔너리의 키의 값 가져오기
x.get('a')

items: 키-값 쌍을 모두 가져옴
x.items()

keys: 키를 모두 가져옴
x.keys()

values: 값을 모두 가져옴
x.values()

리스트, 튜플로 딕셔너리 만들기
keys = ['a', 'b', 'c', 'd']
x = dict.fromkeys(keys) // 값은 None으로 저장
y = dict.fromkeys(keys, 100) // 값은 100으로 저장

from collections import defaultdict
y = defaultdict(int)
y['a','b','c']
'''
from collections import defaultdict
y = defaultdict(int)
y['a','b','c']
print(y)