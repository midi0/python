'''
딕셔너리 표현식 사용하기
keys = ['a','b','c','d']
x = {key: value for key, value in dict.fromkeys(keys).items()}

키만 가져온 후 값으로 0을 할당
x = {key: 0 for key in dict.fromkeys(['a', 'b', 'c', 'd']).keys()}
값을 키로 사용
x = {value: 0 for value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.values()}
키와 값의 자리를 바꿔서 사용
x = {value: key for key, value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.items()}

딕셔너리 표현식에서의 if문 사용
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for key, value in x.items():
    if value == 20:
        del x[key]
위 for문은 반복 도중 딕셔너리의 크기가 바뀌면서 에러가 출력된다.

즉, 딕셔너리는 for 반복문으로 키-값을 삭제하면 안돼고
x = {key: value for key, value in x.items() if value != 20}
딕셔너리 표현식 내에서 if문을 통해 위와 같이 삭제할 값을 제외해준다.

'''
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x = {key: value for key, value in x.items() if value != 20}
print(x)