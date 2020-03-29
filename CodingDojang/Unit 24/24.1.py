'''
문자열 바꾸기
a = 'Hello world'.replace('world', 'Python')


문자 바꾸기
문자열 'apple'에서 a를 1, e를 2, i를 3, o를 4, u를 5로 바꿉니다.
table = str.maketrans('aeiou', '12345')
a='apple'.translate(table)

문자열 분리하기
a = 'apple, pear, grape'.split(', ')


구분자 문자열과 문자열 리스트 연결하기
a = '-'.join(['apple', 'pear', 'grape'])

문자열 변환 (대문자->소문자, 소문자->대문자)
a = 'python'.upper()
a = 'PYTHON'.lower()

좌측과 우측, 그리고 양쪽 공백 삭제하기
a = '      Hello'.lstrip()
a = 'Hello      '.rstrip()
a = '   Hello   '.strip()

좌측, 우측, 양쪽 특정 문자 삭제하기
a = ',..,.python'.lstrip(',.')
a = 'python,.,.,'.rstrip(',.')
a = ',,,,python....'.strip(',.')


문자열 정렬 (좌 우 중)
a = 'python'.ljust(10) // 우측의 남은 공간 4칸을 공백으로 채움
a = 'python'.rjust(10) // 좌측의 남은 공간 4칸을 공백으로 채움
a = 'python'.center(10) // 좌우 2칸씩을 공백으로 채움

메서드 체이닝
a = 'python'.center(10).upper() 좌우 2칸 공백으로 채우고 문자열은 대문자로

문자열 왼쪽에 0 채우기
a = '12'.zfill(4) // 0012
a = '3.5'.zfill(6) // 0003.5
a = 'python'.zfill(10) // 0000python

문자열 위치 찾기
a = 'apple pineapple'.find('pl') // 처음 pl이 나오는 인덱스인 2를 반환
a = 'apple pineapple'.find('xy') // xy가 나오지 않음, -1 반환

문자열 위치 찾기
a = 'apple pineapple'.index('pl') // 2 반환

우측에서부터 문자열 위치 찾기
a = 'apple pineapple'.rindex('pl') // 12 반환

문자열 개수 세기
a = 'apple pineapple'.count('pl') // pl이 두번 나오므로 2 반환
'''
a = 'apple pineapple'.count('pl')
print(a)