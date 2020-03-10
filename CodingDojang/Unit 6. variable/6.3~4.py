'''
x = input('변수 x 입력 : ')
print(x)

a = int(input('첫 번째 수 입력'))
b = int(input('두 번째 수 입력'))
print(a + b)


a, b = input('두 개의 문자열 입력').split()
print(a)
print(b)


a, b= input('숫자 두개 입력').split()
print(int(a) + int(b))


a,b = map(int, input('숫자 두 개를 입력 : ').split())
print(a+b)


a,b = map(int, input('숫자 두개를 입력').split(','))
print(a+b)
'''
a = 20
b = 30

c = a+10
print(c)