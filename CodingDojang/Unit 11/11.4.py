a = [0,10,20,30,40,50,60,70,80]
# print(a[4:-1]) # 인덱스 값 4부터 -1까지 출력
# print(a[2:9:2]) # 인덱스 값 2 4 6 8 을 출력
# print(a[:5]) # 인덱스 값 0 ~ 4 를 출력
# print(a[7:0:-1])

# r = range(10)
# print(list(r[2:5]))

a = range(10)[slice(4,7,2)]

bb = [1,2,3,4,5,6,7,8,0]
bb[4:7] = ['a','b','c','d']
print(bb)