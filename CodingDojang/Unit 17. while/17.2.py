'''
반복 횟수가 정해지지 않은 경우
a = random.random()
print(a)

a = random.randint(1,6) # 1~6 사이의 정수로 난수를 생성
print(a)

i = 0
while i != 3: # 3이 아닐 경우 계속 while문을 돌림
    i = random.randint(1,6)
    print(i)

'''
import random

dice = [1,2,3,4,5,6]
a = random.choice(dice)
print(a)