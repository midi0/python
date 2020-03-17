'''
a = [10,20,30]
a.append(500)
print(a)

a = []
a.append(10)
print(a)

a = [10,20,30]
a.append([500,600])
print(a)

a = [10,20,30]
a.extend([500,600])
print(len(a))

a = [1,2,3]
a.insert(2, 500)
print(a)

a = [1,2,3]
a[1:1] = [500,600]
print(a)

a = [1,2,3]
a.insert(1,[500,555])
print(a)

a = [10,20,30]
print(a.pop())
print(a)

a = [111,222,333]
print(a.pop(1))
print(a)

a = [111,222,333]
print(a.remove(222))
print(a)

from collections import deque
a = deque([111,222,333,212,333])
print(a)
a.append(444)
a.popleft()
print(a)
print(a.index(333))
print(a.count(333))

a = [111,222,333,212,313,232]
a.reverse()
print(a)
a.sort()
print(a)


sort 메서드와 sorted 함수
파이썬은 리스트의 sort 메서드뿐만 아니라 내장 함수 sorted도 제공합니다.
sort는 메서드를 사용한 리스트를 변경하지만,
sorted 함수는 정렬된 새 리스트를 생성합니다.

a = [111,222,333,212,313,232]
a.sort()
print(a)
b = [50,30,55,24,35]
print(sorted(b))

a = [111,222,333,212,313,232]
a.clear()
print(a)
b = [1,2,3,4]
del b[:]
print(b)

a = [1,2,3,4,5,6]
a[len(a):] = [9999]
print(a)

a = [1,2,3,4,5,6]
a[len(a):] = [99,999]
print(a)

a = [1,2,3,4,5,6]
a[len(a):] = [99,999]
print(a)
'''
