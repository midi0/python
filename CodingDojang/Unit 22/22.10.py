'''
a,b = input().split(' ')
if b > a:
    c = [2**i for i in range(int(a),int(b)+1)]
    del c[1],c[-2]
    print(c)
'''
start,stop = map(int,input().split())
for i in range(start,stop+1):
    i = [2 ** i for i in range(start, stop + 1)]
    i.pop(1),i.pop(-2)
print(i)