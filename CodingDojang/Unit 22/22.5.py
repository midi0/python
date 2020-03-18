'''
리스트 표현식
a = [i for i in range(10)]
print(a)
b = list(i for i in range(10))
print(b)
c = [i+5 for i in range(10)]
print(c)
d = [i*2 for i in range(10)]
print(d)

a = [i for i in range(10) if i % 2 == 0]
print(a)
# 0 ~ 9 숫자중 홀수의 값 + 5를 하여 리스트 생성
b = [i+5 for i in range(10) if i % 2 == 1]
print(b)

a = [i for i in range(10) if i % 2 == 0]
print(a)
# 0 ~ 9 숫자중 홀수의 값 + 5를 하여 리스트 생성
b = [i+5 for i in range(10) if i % 2 == 1]
print(b)

# 2~9단 리스트 생성
a = [i*j
     for j in range(1,10)
     for i in range(2,10)
     ]
print(a)
ㄴ이 경우 for문이 2개인데, 처리순서가 뒤에서 앞으로 오기에 i를 뒤에 써준다
'''
