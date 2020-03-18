'''
리스트중 최솟값 구하기
smallest = a[0]
for i in a:
    if i < smallest:
        smallest = i
print(smallest)


최대
largest = a[0]
for i in a:
    if i > largest:
        largest = i
print(largest)

정렬 후 최대 최소
a.sort()
print(a[0])
a.sort(reverse=True)
print(a[0])

내장 함수 이용
print(min(a))
print(max(a))

리스트의 합 구하기
x = 0
for i in a:
    x += i
print(x)

내장함수 이용
print(sum(a))

'''
a = [30,20,50,80,20]

