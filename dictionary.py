'''
dictionary : key와 value 한 쌍을 원소로 가지는 자료형

dict = {}
dict['Hello'] = '안녕'
dict['Miracle'] = '기적'
dict['Effort'] = '노력'
dict['Hello'] = '안녕하세요'

keys = dict.keys() #키값만 담는 함수
values = dict.values() #값만을 담는 함수
key_list = list(keys)
value_list = list(values)
print("키 : ", keys)
print("키 : ", key_list)
print("값 : ", values)
print("값 : ", value_list)

if 'Effort' in dict:
    print("Effort 키가 존재합니다.")

del dict['Effort']
dict.clear() # 모든 원소 삭제
print(dict)
print("사전 자료형의 길이", len(dict))

# i = 인덱스 , k = 키값
for i, k in enumerate(dict):
    print("[인덱스 : ", i, "] 영어 : ", k , "/ 한글 : ", dict[k])
'''
scores = {}
scores['aa'] = 95
scores['cc'] = 66
scores['dd'] = 54
scores['bb'] = 84

print(sorted(scores)) # 키로 정렬하기 ( 기본은 오름차순 )
print(sorted(scores, reverse=True)) # 키로 내림차순 정렬
print(sorted(scores.values())) #값을 정렬하기