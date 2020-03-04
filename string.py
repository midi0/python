'''
문자열 자료형의 기본 함수
문자열 자료형 뒤집기 : 슬라이스를 이용

print(str[::-1])

len() : 문자열의 길이를 출력
print(len(str))
isalpha() :  특정한 문자열이 문자로만 이루어져 있는지 확인 ( 숫자나 공백이 없는지를 검사 )
print(str.isalpha())
isdigit() : 특정한 문자열이 숫자로만 이루어져 있는지 확인
print(str.isdigit())
isalnum() : 특정한 문자열이 문자와 숫자로만 이루어져 있는지 확인
print(str.isalnum())
join(리스트 자료형) : 여러 개의 문자열을 구분자와 함께 합치는 함수
str = "aba123"
list = ['Hello','World','and Python']
print(','.join(list))

sorted(문자열 자료형) : 각 문자를 정렬하는 함수 // 기본적으로 오름차순 정렬
str = "helloworld"
list = sorted(str)
print(''.join(list))
list = sorted(str, reverse=True)
print(''.join(list))
split(토큰) : 문자열을 토큰에 따라서 분리하는 함수
find(서브 문자열) : 문자열 내부에 존재하는 서브 문자열을 찾아주는 함수
str = "I-wanna-watch-a-movie"
list = str.split('-')
print(list)
print(str.find('w')) #처음으로 만나는 문자 값의 인덱스를 출력
print(str.find('w', 5)) #해당 인덱스 이후의 문자를 찾아줌

upper(), lower() : 문자열을 대,소문자로 변환
print(str.upper())
print(str.lower())

strip():좌우로 특정 문자열을 제거하는 함수 // 주로 데이터의 정제가 목적이다
str = " Hello World "
print(str.strip()) #좌우측의 공백이 제거됨
print(str.rstrip()) # 우측의 공백이 제거
print(str.lstrip()) # 좌측의 공백이 제거
str = "AAAAAAAAAHello WorldAAAAAAAAA"
print(str.strip('A')) # 좌우측의 A문자가 모두 제거

eval() : 문자열 수식 계산하는 함수
exp = "(203+705)*3-(30/6)"
print(eval(exp))
'''
