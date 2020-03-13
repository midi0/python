'''
if 0:
    print('참')
else:
    print('거짓')  # 0은 거짓

if 1:
    print('참')  # 1은 참
else:
    print('거짓')

if 13.5:  # 실수
    print('참')  # 13.5는 참
else:
    print('거짓')
'''
if 'Hello':  # 문자열
    print('참')  # 문자열은 참
else:
    print('거짓')

if '':  # 빈 문자열
    print('참')
else:
    print('거짓')  # 빈 문자열은 거짓


# 0, None, 빈 문자열 ''을 not으로 뒤집으면 참(True)이 되므로
# if를 동작시킬 수 있습니다.
if not 0:
    print('참')  # not 0은 참
if not None:
    print('참')  # None은 참
if not '':
    print('참')