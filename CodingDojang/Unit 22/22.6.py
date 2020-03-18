'''
실수 리스트 값을 정수화
for i in range(len(a)):
    a[i] = int(a[i])
print(a)

for문 대신 map을 사용
a = list(map(int, a))
print(a)

숫자를 만든 후 문자열로 변환
a = list(map(str, range(10)))
print(a)

input로 받은 값이 리스트인지 확인
a = input().split()
print(a)

a = map(int, input().split())
print(a) # 맵 객체는 안의 값을 볼 수 없다.
print(list(a))
'''
