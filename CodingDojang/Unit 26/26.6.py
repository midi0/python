'''
세트 표현식 사용하기
a = {i for i in 'apple'} #중복되는 p는 하나만 요소로 들어간다

표현식과 if 조건문 사용
a = {i for i in 'pineapple' if i not in 'apl'} # e i n이 요소로 들어감
'''
a = {i for i in 'pineapple' if i not in 'apl'}
print(a)