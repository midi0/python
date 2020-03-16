'''
계단식 출력
for i in range(5):
    for j in range(5):
        if j <= i:
            print('*', end='')
    print()


for i in range(5):
    for j in range(5):
        if j == i:
            print('*', end='')
    print()
'''
for i in range(5):        # 0부터 4까지 5번 반복. 세로 방향
    for j in range(5):    # 0부터 4까지 5번 반복. 가로 방향
        if j == i:                # 세로 방향 변수와 같을 때
            print('*', end='')    # 별 출력. end에 ''를 지정하여 줄바꿈을 하지 않음
        else:                     # 세로 방향 변수와 다를 때
            print(' ', end='')    # 공백 출력. end에 ''를 지정하여 줄바꿈을 하지 않음
    print()