print (3>1)
print(10 == 10)
print(10 != 5)
print('python' == 'Python')
print(1==1.0) # True
print(1 is 1.0) # false

print(id(1)) # 메모리 주소를 구함
print(id(1.0))

'''
값을 비교할 때는 is를 사용하면 안 됩니다.
다음과 같이 변수 a에 -5를 할당한 뒤 a is -5를 실행하면
True가 나오지만 다시 -6을 할당한 뒤 a is -6을 실행하면 False가 나옵니다.

>>> a = -5
>>> a is -5
True
>>> a = -6
>>> a is -6
False
'''