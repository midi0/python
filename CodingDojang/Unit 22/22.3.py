'''
for i in a:
    print(i, end=' ')

for index, value in enumerate(a):
    print(index + 1, value, end=' / ')

for index, value in enumerate(a, start=1):
    print(index, value, end=' / ')

for i in range(len(a)):
    print(a[i], end=' ')

i = 0
while i < len(a):
    print(a[i], end=' ')
    i += 1

# 범위를 <= 로 설정하면 마지막 인덱스는 리스트의 길이보다 1이 작으므로 <를 사용합니다.
# 만약 i <= len(a)처럼 <=을 사용하면 리스트의 범위를 벗어나게 되므로 주의해야 합니다.
i = 0
while i < len(a):
    print(a[i], end=' ')
    i += 1
'''
a = [38,21,53,62,19]
