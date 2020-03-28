'''
2차원 리스트의 할당 / 복사

copy를 통해 복사하고 b의 요소를 바꾸면 a,b 모두 바뀐다
a = [[10,20],[30,40]]
b = a.copy()
b[0][0] = 500
print(a)
print(b)

2차원 이상의 리스트는 deepcopy를 사용하여 바꿔줘야함
b를 바꿔도 a 리스트에 영향이 가지 않는다.
import copy
a = [[10,20],[30,40]]
b = copy.deepcopy(a)
b[0][0] = 500
print(a)
print(b)

'''
import copy
a = [[10,20],[30,40]]
b = copy.deepcopy(a)
b[0][0] = 500
print(a)
print(b)