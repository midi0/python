'''
서식 지정자로 문자열 넣기
a = 'I am %s.' %'james' // I am james.

name = 'maria'
a = 'I am %s.' %name // I am maria.

서식 지정자로 숫자 넣기
a = 'I am %d years old.' %20

서식 지정자로 소수점 표현하기
a = '%f' %2.3 // 2.300000
a = '%.2f' %2.3 // 2.30
a = '%.1f' %2.3 // 2.3

서식 지정자로 문자열 정렬하기
a = '%10s' % 'python' // 왼쪽 4만큼 공백 이후 python

a = '%10d' %150 // 공백 7번 출력 후 150출력
a = '%10.2f' % 2.3 // 공백 출력 후 2.3 출력
a = '%-10s' % 'python'
// 'python'은 길이가 6이므로 오른쪽 공간을 공백 4칸으로 채웁니다.

서식 지정자로 문자열 안에 값 여러 개 넣기
a = 'Today is %d %s.' %(3,'April')

format 메서드 사용
a = 'Hello, {0}'.format('world!') // 'Hello, world!'

인덱스 생략하기
a = 'Hello, {0}'.format('python') //'Hello, python'

인덱스 대신 이름 지정하기
a = 'Hello, {language} {version}'.format(language='Python', version=3.6)

문자열 포매팅에 변수를 사용하기
language = 'Python'
version = 3.6
a = f'hello, {language} {version}'

중괄호 출력
a = '{{ {0} }}'.format('Python')

문자열을 지정된 길이로 만든 뒤 왼쪽으로 정렬하고 남는 공간을 공백으로 채웁니다.
a = '{0:<10}'.format('python')

문자열을 지정된 길이로 만든 뒤 오른쪽으로 정렬하고 남는 공간을 공백으로 채웁니다.
a = '{0:>10}'.format('python')

인덱스를 사용하지 않는다면
a = '{:>10}'.format('python')
위와 같이 :(콜론)과 정렬 방법만 지정해도 됩니다.

숫자 개수 맞추기
a = '%03d' %1
a = '{0:03d}'.format(35)
%d는 다음과 같이 %와 d 사이에 0과 숫자 개수를 넣어주면 자릿수에 맞춰서
앞에 0이 들어갑니다. 즉, %03d로 지정하면 1은 '001', 35는 '035'가 됩니다.
{ }를 사용할 때는 인덱스나 이름 뒤에 :(콜론)를 붙이고 03d처럼
0과 숫자 개수를 지정하면 됩니다.

'''
a = '{0:03d}'.format(35)
print(a)