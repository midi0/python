'''
count = int(input('반복 횟수 입력'))
i = 0
while True:
    print(i)
    i += 1
    if i == count:
        break

count = int(input('홀수 출력'))
i = 0
while i < count:
    if i % 2 == 1:
        print(i)
    i += 1
'''
count = int(input('반복할 횟수를 입력하세요: '))

for i in range(count + 1):
    if i % 2 == 0:
        continue
    print(i)