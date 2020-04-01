'''
세트의 할당과 복사
a = {1,2,3,4}
b = a
b.add(5) # a와 b 모두 5가 추가
print(a is b) 

b = a.copy()
print(a is b) # 내부 요소는 같지만 서로 다른 객체로 False 출력
print(a == b) # 내부 요소는 같아서 True 출력
'''

a = {1,2,3,4}
b = a.copy()
print(a is b)
print(a == b)