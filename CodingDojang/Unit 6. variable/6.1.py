x = 10
y = 'hello world'

print(type(x))
print(type(y))

x,y,z = 10,20,30
print(x,y,z)

x = y = z = 10
print(x,y,z)

x,y = 10,20
x,y = y, x
print(x,y) #x, y로 20 10이 출력

x = 10
del x
# print(x) 컴파일 에러

x = None
print(x)