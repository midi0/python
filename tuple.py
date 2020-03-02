'''
Tuple : List와 비슷한 자료형 ( 한번 설정한 자료의 값은 변경 불가 )
인덱싱, 슬라이싱 등의 문법 그대로 사용 가능
'''

tuple = (1,2,3)
for i in tuple:
    print(i)

list1 = [1,2,3]
list2 = [4,5,6]
tuple = (list1,list2) # 이차원 배열처럼 출력
tuple[0][1] = 7 #튜플의 값을 바꾸는건 불가능하지만 튜플 내부의 배열값을 바꾸는건 가능
print(tuple)
print(tuple[0][1])

tuple = (1,2,3,4,5,6,7,8)
print(tuple[0:5] * 3)