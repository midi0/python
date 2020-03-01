# -*- coding: utf-8 -*-
a = "HELLO WORLd"
b = a.replace("HELLO", "Hi") #문자를 대체하는 함수
c = a.strip("HELLO") # HELLO가 지워져서 출력
d = a.split(" ") # 하나의 문자열을 여러개의 문자열로 나누는데, 단순 나눔이 아니라 배열형태로 결과를 반환 #
e = a.zfill(20) # 기존의 문자열보다 작으면 빈칸을 0으로 채운다

aa = "6457"
bb = int(aa) # 문자열을 숫자로 형변환시켜줌#

print(a.count('L')) # 특정 문자의 부분 문자열의 수를 반환, L이 3번 들어가므로 3 출력

print(a.find("WOR")) # 특정 문자열의 위치를 반환, WOR이 시작하는 인덱스 값 6이 출력

print(a.upper()) # 대문자로 바꿔서 출력

print(a.lower()) # 소문자로 바꿔서 출력


print(b)
print(c)
print(d) # 공백을 기준으로 문자열을 반환해서 HELLO와 WORLD 로 출력한다. #
print(e)
print(bb+505)