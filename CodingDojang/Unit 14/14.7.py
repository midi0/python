korean, english, mathematics, science = map(int, input().split(' '))
avg = int((korean + english + mathematics + science)/4)

if  0 <= korean <= 100 and \
    0 <= english <= 100 and \
    0 <= mathematics <= 100 \
    and 0 <= science <= 100:
    if avg >=80:
        print('합격')
    else:
        print('불합격')
else:
    print('잘못된 점수')

'''
if a > 100 or b > 100 or c > 100 or d > 100:
    print('잘못된 점수')
elif avg >= 80:
    print('합격')
elif avg < 80:
    print('불합격')
'''