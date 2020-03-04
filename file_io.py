'''
파일 입/출력
open():파일을 특정한 모드로 여는 함수.
읽을 때는 r , 쓸 때는 w

read():파일 객체로부터 모든 내용을 읽는 함수
readline():파일 객체로부터 한 줄씩 문자열을 읽는 함수
readlines(): 전체 내용을 한 번에 리스트에 담는 함수

with ~ as 구문 : with 구문을 나오는순간 파일의 메모리가 할당 해제된다
with open("input.txt", "r", encoding="UTF-8") as f:
    list = f.readlines()
    for i, data in enumerate(list):
        print("%d번째 줄: %s" % (i + 1, data), end='')
    f.close()



f.seek(9) # 9바이트의 위치부터 파일을 읽겠다는 선언
data = f.read()
print(data)
f.close() # 리소스 사용 정리


count = 0
while count<3:
    data = f.readline()
    count = count + 1
    print("%d번째 줄: %s" %(count,data), end='')
f.close()

list = f.readlines()
for i,data in enumerate(list):
    print("%d번째 줄: %s" %(i+1,data), end='')
f.close()
'''
def process(filename):
    with open(filename, "r") as f:
        #키 : 알파벳 , 값 : 빈도수
        dict = {}
        data = f.read()
        for i in data:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
    return dict
dict = process("input.txt")
#빈도 수를 기준으로 내림차순 정렬 시행
dict = sorted(dict.items(), key=lambda a:a[1], reverse=True)

for data, count in dict:
    if data == '\n' or data == ' ':
        continue
    print("%d번 쓰임: [%c]" %(count, data))