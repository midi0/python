# -*- Encoding: utf-8 -*-
# 리스트 : 비슷한 성질을 가진 객체의 나열


a = [3.5, 4.3, 2.3, 3.8, 3.2, 4.5]

print(a)

print("인덱스 0 =", a[0])
a[0] = 0.3
print("인덱스 0 =", a[0])


sum = 0
for i in a:
    sum = sum + i
print("평균 : ", sum/len(a))


#이차원 배열
aa = [
    [90, 95, 83, 40, 30, 20, 19, 48, 39, 59],
    [48, 53, 64, 76, 58, 34, 55, 85, 96, 85]
]
sum = 0
english = aa[0]

for i in english:
    sum = sum + i
print("영어 평균 : ", sum/len(english))

sum = 0
math = aa[1]

for i in math:
    sum = sum + i
print("수학 평균 : ", sum/len(math))
