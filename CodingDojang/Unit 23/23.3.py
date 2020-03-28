'''
for 반복문으로 1차원 리스트 생성
a = []
for i in range(10):
    a.append(0)
print(a)

for 2차원 리스트 생성
for i in range(3):
    line = []
    for j in range(2):
        line.append(0)
    a.append(line)
print(a)

리스트 표현식으로 2차원 리스트 만들기
a = [[0 for j in range(2)] for i in range(3)]
print(a)
또는
a = [[0] * 2 for i in range(3)]
print(a)

가로 크기가 불규칙한 jagged list(톱니형 리스트) 만들기
a = [3,1,3,2,5]
b = []
for i in a:
    line = []
    for j in range(i):
        line.append(0)
    b.append(line)
print(b)

sorted 를 이용하여 2차원 리스트 정렬하기
'''
students = [
    ['john', 'C', 19],
    ['maria', 'A', 25],
    ['andrew', 'B', 7]
]
# 안쪽 리스트의 인덱스 1을 기준으로 정렬
print(sorted(students, key=lambda student: student[1]))
# 안쪽 리스트의 인덱스 2를 기준으로 정렬
print(sorted(students, key=lambda student: student[2]))