'''
파이썬의 다양한 내장 함수
input() :  사용자로부터 콘솔로 입력을 받는 함수
int() : 정수 자료형으로 변환
float() :  실수 자료형으로 변경
max(), min() : 시퀀스 자료형에 포함된 원소중 최대 or 최소값을 반환
bin(), hex() : 10진수 -> 2진수 변환, 10진수 -> 16진수 변환, 이때 반환값은 문자열
round() : 반올림을 수행
type() : 자료형의 종류
'''

'''
user_input = input('정수를 입력하세요 : ')
print("제곱 : ", int(user_input) ** 2)
a = "12345"
print(int(a))
b = 12.5
print(int(b))
list = [5,6,3,1,2,5,6,7,8,9]
print(max(list))
print(min(list))

print(bin(128))
print(hex(230))
print(int('0xe6', 16))

print(round(123.456,2))
print(round(123.456))
print(round(123.456, -1))

int = 1
str = "문자열"
list = [1,2,3]
dic = {'apple' : '사과'}
print(type(int))
print(type(str))
print(type(list))
print(type(dic))
'''
