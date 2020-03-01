# -*- coding: utf-8 -*-

a = 25.1
b = 5
c = int("200")

print(a+b) # 결과 값이 실수형으로 자동 형 변환이 이루어짐#
print(a+b+c)

print("a / b = ", a/b)
print("a // b =", a//b) # 몫만 출력#

# 16진수 0x를 붙여서 선언 # 
aa = 0xFFFFFFFF
print(aa)

# 복소수의 곱셈 같은 고급 수학도 구현이 가능 #
aa = ( 1 + 2j)
bb = ( 3 + 4j)
print ( aa * bb )