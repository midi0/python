'''
복사
a = [0,1,2,3]
b = a
print(a is b) # True
b[2] = 222
print('a = ',a)
print('b = ',b)

할당
a = [1,2,3,4]
b = a.copy()
print(a is b) # False
print(a == b) # True
b[2] = 99
print('a is =',a)
print('b is =',b)
'''
