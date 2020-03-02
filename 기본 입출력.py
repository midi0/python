# -*- coding: utf-8 -*-

# 공백을 기준으로 input 함수 안의 값을 배열의 원소로 나눠준다

#백준 입/출력 1단계 1000번 문제

a= input().split(' ')

x = int(a[0]) #문자형으로 입력받은 데이터를 형변환

y = int(a[1])

print("x + y = ", x+y)
print("x - y = ", x-y)
print("x * y = ", x*y)
print("x / y = ", x/y)