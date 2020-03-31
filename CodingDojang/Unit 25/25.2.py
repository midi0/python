'''
키만 출력된다
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for i in x:
    print(i, end=' ')
    
키와 값이 출력
for key, value in x.items():
    print(key,value)
    
for key, value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.items():
    print(key, value)
결과는 같다

키만 출력2
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for key in x.keys():
    print(key, end=' ')

값만 출력하기
for value in x.values():
    print(value, end=' ')
'''
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for key in x.keys():
    print(key, end=' ')