# a[x] 가 __getitem__(x) 메소드를 호출하므로 같은 결과가 출력
# print(a[2])
# print(a.__getitem__(2))

# print(a[-5]) # 뒤에서부터 출력

b = a[len(a) - 1]
# print(b) # 배열의 마지막 원소 출력

aa = [1,2,3,4,5,6]
aa[0] = 11
aa[1] = 22
aa[2] = 33
aa[3] = 44
del aa[3]
print(aa)