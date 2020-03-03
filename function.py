'''
함수 : 입력을 받아 처리한 후 특정 출력을 하는 모듈
함수를 이용하면 특정 소스코드의 반복을 줄일 수 있다
가변 인자 :  함수의 매개변수가 가변적일 경우 사용한다.
파이썬의 경우 함수의 반환 값이 여러개일 수 있으며 이 경우 튜플 형태로 반환된다

def add(a,b): #입력부
    sum = a + b #처리부
    return sum #출력부

print(add(1,2))

def function(*data): # *매개변수명 으로 선언해주고 , 이 경우 튜플형으로 자료가 처리된다.
    print(data)

function(1,2,3)


def add():
    global a  # 전역변수로 사용하겠다는 의미
    a = a+5 #지역변수
a = 2 #전역변수
add()
print(a) # a가 전역변수로 지정되어 7이 출력
'''

def function():
    a = 5
    b = [1,2,3]
    return a,b
a,b = function()
print(a)
print(b)