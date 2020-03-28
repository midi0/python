'''
반복문을 사용한 2차원 리스트의 요소 출력
for x,y in a:
    print(x,y)

2중 for문을 사용하여 출력하기
for i in a:        # a에서 안쪽 리스트를 꺼냄
    for j in i:    # 안쪽 리스트에서 요소를 하나씩 꺼냄
        print(j, end=' ')
    print()

for 와 range를 사용하여 출력하기
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()

while 반복문을 사용하기
i = 0
while i < len(a):
    x,y = a[i]
    print(x,y)
    i += 1

while 2회 사용
i = 0
while i < len(a):
    j = 0
    while j < len(a[i]):
        print(a[i][j], end=' ')
        j += 1
    print()
    i += 1
'''
a = [[10,20],
     [30,40],
     [50,60]]
