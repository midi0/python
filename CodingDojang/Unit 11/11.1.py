a = [0,10,20,30,40,50,60]
# print(30 in a)

a = [0,10,20,30]
b = ['aa','bb','cc']
c = a + b
# print(c)

# range 는 리스트나 튜플에 넣어서 합칠 수 있다
al = list(range(0,10)) + list(range(10,20))
aT = tuple(range(20,30)) + tuple(range(30,40))

aa = [0,1,2,3] * 3 # 0123이 각 세번씩 출력
print(aa)