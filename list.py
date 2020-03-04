'''
index(원소) : 리스트 내의 특정한 원소의 인덱스를 찾기
list = ['AAA','BBB','CCC','DDD','EEE']
print(list.index('EEE'))

reverse() : 리스트의 원소를 뒤집기
list.reverse()
print(list)

list = list[::-1]
print(list)

sum(리스트 자료형) : 리스트의 모든 원소의 합
list = [1,2,3]
print(sum(list))

range(시작,끝) : 특별 범위를 지정
list(특정 범위) : 특점 범위의 원소를 가지는 리스트 반환
my_range = range(5,10)
list = list(my_range)
print(list)

all() : 리스트의 모든 원소가 참인지 판별
any() : 하나라도 참인지 판별
list = [True, False, True]
print(all(list))
print(any(list))

enumerate() : 리스트에서 인덱스와 원소를 함께 추출
my_list = ['a','b','c','d','e']
result = list(enumerate(my_list))
print(result)

for i,k in enumerate(my_list):
    print("인덱스 : ",i," / 원소 : ", k)

sort(): 리스트의 원소를 정렬
my_list = ['c','h','g','a','e']
my_list.sort()
print(my_list)

count(): 특정한 원소의 개수를 추출
my_list = ['c','h','a','a','e']
print(my_list.count('a'))

del: 리스트의 특정 원소를 제거
my_list = ['c','h','a','a','e']
del my_list[1]
del my_list[1:3]
print(my_list)

insert(): 리스트에 특정 원소를 삽입
my_list = ['c','h','a','a','e']
my_list.insert(3, '-A-')
print(my_list)

append(): 리스트의 가장 마지막 원소로서 원소를 삽입
'''
my_list = ['123','456','789']
my_list.append('-123')
print(my_list)
