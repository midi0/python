'''
Sequence : 문자열 / 리스트 / 튜플 등 index 를 가지는 자료형을 말한다
모두 슬라이싱, 인덱스 등의 기법이 사용가능하다.
동일한 자료형일 경우 연산이 가능하다
반복문에서 사용이 가능하다 for, while 등등등 ..
len(시퀀스 자료형) 을 통해 시퀀스 자료형의 길이 출력이 가능

string = "Hello world"
string2 = ", Python"

list = ['H','e','l','l','o','w','o','r','l','d']
tuple = ('H','e','l','l','o','w','o','r','l','d')
print(string + string2)
print(string[0])
print(string[0:5])
print(list[0])
print(list[0:5])
print(tuple[0])
print(tuple[0:5])
for i in list:
    print(i)
'''
list = [1,2,3,4,5]
print(4 in list)

if 3 in list:
    print("3을 포함하고 있습니다.")