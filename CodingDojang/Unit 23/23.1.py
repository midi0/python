'''
2차원 리스트
a = [[10,20], [30,40], [50,60]]
print(a)

2차원 리스트의 요소 추가
a = [[10,20], [30,40], [50,60]]
print(a[0][0], a[0][1])
a[0][1] = 1000
print(a[0][1])

톱니형 리스트
a = [[10, 20],
     [500, 600, 700],
     [9],
     [30, 40],
     [8],
     [800, 900, 1000]]
a[0].append(30)
a[0].append(40)
print(a)

2차원 튜플
a = ((10, 20), (30, 40), (50, 60))    # 튜플 안에 튜플을 넣은 2차원 튜플
b = ([10, 20], [30, 40], [50, 60])    # 튜플 안에 리스트를 넣음
c = [(10, 20), (30, 40), (50, 60)]    # 리스트 안에 튜플을 넣음
튜플은 내용을 변경할 수 없으므로
a는 안쪽과 바깥쪽 모두 요소를 변경할 수 없습니다.
b는 안쪽 리스트만 요소를 변경할 수 있고,
c는 바깥쪽 리스트만 요소를 변경할 수 있습니다.
'''
from pprint import pprint
a = [[10, 20], [30, 40], [50, 60]]
pprint(a, indent=4,width=20)