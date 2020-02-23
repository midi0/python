fruit = ["사과", "사과", "바나나", "바나나", "딸기", "키위", "복숭아", "복숭아", "복숭아"]

d = {} #딕셔너리에 키와 밸류값을 받아서 과일을 카운팅을 해준다

for f in fruit:

    if f in d: # "사과" 라는 key 값이 딕셔너리에 들어있는지 확인한다 
         d[f] = d[f] + 1 # "사과" 값이 있으면 갯수를 하나 증가시켜준다
    else:
         d[f] = 1 # 만약 사과라는 값이 없으면 딕셔너리에 넣고 밸류를 1로 만든다

print(d)

#자료구조(리스트/튜플/딕셔너리 비교)
