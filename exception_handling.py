'''
예외 처리

try:
    print(3/2)
except: #예외가 발생한 경우
    print("0으론 나눌 수 없습니다")
else: #예외가 발생하지 않았을 경우
    print("예외 없이 성공적으로 실행 완료")
finally: #예외가 발생했는지의 유무와 상관없이 항상 실행
    print("예외 발생과 상관 없이 출력합니다")
'''

try:
    print(3/0)
except Exception as e: #오류가 발생시 발생한 오류 메세지를 e라는 변수에 담아준다.
    print(e)