# -*- Encoding: utf-8 -*-

a = [10,20,30,40,50,10]

b = [70,50,30]

print(a.count(10)) # count(원소) 리스트 내의 특정 원소가 몇 개 포함되어있는지 반환

print(a.index(50)) # index(원소) 리스트 내 원소의 인덱스를 반환

a.append(25) # append(원소) 리스트의 뒤쪽에 새로운 원소를 삽입
print(a)

a.sort() # 오름차순으로 배열 내부의 원소를 정렬함
print(a)

a.extend(b) # a 리스트의 뒤에 다른 리스트를 삽입
print(a)

a.insert(3,70) # insert(인덱스,원소) : 특정 위치에 원소를 삽입
print(a)

a.remove(10) # 특정 원소를 삭제한다.
print(a)

a.pop(3) # 리스트 내 특정한 인덱스의 원소를 삭제한다
print(a)

a.reverse() # 리스트를 뒤집는다
print(a)