'''
딕셔너리의 할당, 복사
x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
y = x
y = x처럼 딕셔너리를 다른 변수에 할당하면, 실제론 딕셔너리 한 개를 공유한다
print(x is y) #True가 출력

y['a'] = 99
y의 값을 변경하면 x의 값에도 반영

copy를 통해 딕셔너리 객체를 두개로 나눈다.
y = x.copy()
y['a'] = 99 #x의 값은 변하지 않고 0

x is y # 두 객체는 다른 객체기 때문에 False 가 출력
x == y # 복사한 키-값은 같아서 True가 출력

중첩 딕셔너리의 할당과 복사
x = {'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
y = x.copy()
y['a']['python'] = '2.7.15'
y의 값을 변경한것이 x에도 반영이 됩니다.

중첩 딕셔너리를 완전히 복사하려면 copy 대신 copy모듈의 deepcopy 함수를 사용합니다.
import copy
y = copy.deepcopy(x)
y['a']['python'] = '2.7.15'
y의 값을 변경해도 x에는 영향을 미치지 않습니다.

'''
import copy
x = {'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
y = copy.deepcopy(x)
y['a']['python'] = '2.7.15'
print(x)