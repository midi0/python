# -*- coding: utf-8 -*-

a = "HELLO WORLD"

print(a) # 전체 다 출력

print(a[0]) # H만 출력

print(a[7]) # O만 출력

print(a[-3]) # R만 출력 (뒤에서부터 -1-2-3카운팅)

#슬라이싱 ( 문자열을 부분으로 나눔 )#
print(a[2:9]) #LLO WOR까지 출력, 뒤의 인자는 끝낼때의 인덱스 +1 을 해주는것에 유의

print(a[2:]) # 2부터 끝까지 출력

print(a[:-2]) # 뒤의 2만 빼고 출력 

print(a[:]) # 전문 출력

#스탭을 적용한 슬라이스 (스탭 - 건너뛰겠다) #

print(a[0:7:2]) #시작, 끝, 2만큼 건너뛰기, HLOW 출력