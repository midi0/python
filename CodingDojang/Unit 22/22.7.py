'''
특정 값의 인덱스 구하기
a = (38,21,53,62,19,53)
print(a.index(53))

특정 값의 개수 구하기
a = (38,21,53,62,19,53,21)
print(a.count(21))

반복문으로 요소 출력하기
a = (38,21,53,62,19,53,21)
for i in a:
    print(i, end=' ')

튜플 표현식 사용하기
a = tuple(i for i in range(10) if i % 2 == 0)
print(a)

제너레이터 사용하기 (Unit 40에서 다시 다룸)
a = (i for i in range(10) if i % 2 == 0)
print(a)

tuple에 map 사용하기
a = (1.2,2.5,3.6,7.2)
a = tuple(map(int,a))
print(a)

튜플 내 최소, 최대 합계 구하기
a = (36,45,21,67,26)
print(min(a),max(a),sum(a), end=' ')
'''
a = (36,45,21,67,26)
print(min(a),max(a),sum(a), end=' ')