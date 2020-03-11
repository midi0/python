#튜플

a = (1,2,3,4,5,6,7) # 리스트는 [] , 튜플은 () 로 감싼다.
person = ('세영', 123, 11.333, True)

b = (38) # int 형의 데이터 타입
b = (38,) # tuple 형의 데이터 타입, 튜플의 형태를 유지하기 위한 문법

aa = tuple(range(10))
bb = tuple(range(5,12))
cc = tuple(range(-4,12,2))

a = [1,2,3] # 배열
tuple(a) # 배열을 튜플로 만든다

a = (1,2,3) # 리스트
list(a) # 튜플을 리스트로 만든다

a = list('Hello')
a = tuple('hello')
a,b,c = [1,2,3]
d,e,f = (4,5,6)

x = [1,2,3]
a,b,c = x

x = input().split()
a,b = x
print(a,b)
