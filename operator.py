'''
파이썬에서의 증감 연산자 : 기존의 증가/감소 기능을 짧게 이용
축약형 -> 증감연산자
C/C++ 증감 연산자 : ++, --

관계 연산자 : 특정 값을 비교
A == B : A와 B가 같은지 판별
A != B : A와 B가 다른지 판별

논리 연산자 : 수식을 논리적으로 연산
A and B : A,B 모두 참인지 판별
A or B : A또는 B가 참인지 판별
not A : A가 거짓인지 판별
'''

'''
a = 10
a += 10
a *= 10
print(a)

a = 3
b = 7
print(a==b)
print(a!=b)
print(a>b)

a="ABC"
b="DEF"
print(a==b)
print(a<b) # 사전순으로 크고 작음을 비교, true 출력

a = True
b = False
print(a and b) #false
print(a or b) #true
print(not a) #false

if 3>5 or 7<10:
    print("하나만 만족해도 출력")
'''