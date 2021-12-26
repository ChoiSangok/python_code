## 2) 문자형

# 문자형을 만들기 위해서는 문자를 따옴표(') 쌍 따옴표(") 로 감싸준다.

a = 'hello'

a = "hello"

# * 인덱스
# 인덱스는 []를 통해 지정해 줄 수 있으며, 0부터 시작합니다.

a = 'hello python'

# 변수 a 의 첫 번째 문자를 출력하시오.

print(a[0])

# 변수 a 의 마지막 문자를 출력하시오.

print(a[-1])

# * 슬라이스
#  범위를 지정하여 원하는 부분만을 얻을 수 있습니다.

a = 'hello python'

# 변수 a 전체를 출력하시오.

print(a)

# or

print(a[:])

# 변수 a의 6 ~ 8 번째 문자를 출력하시오.

print(a[5:8])
print(a[3:5])

# 변수 a의 처음 ~ 5번째 문자를 출력하시오.

print(a[:5])
print(a[0:5])

# 변수 a의 뒤에서부터 5번째 ~ 마지막 문자를 출력하시오.

print(a[-5:])
print(a[-7:]) # 공백차이구나

# 변수 a의 처음 ~ 뒤에서부터 -5번째 문자를 출력하시오.

print(a[:-4])

# 문자열의 합

a = 'hello'
b = 'python'
print(a + b)

# - 문자열의 곱

a = 'hello'
print(a * 3)

# * 문자형과 숫자형의 혼용

# 문제 : 변수(숫자)를 넣어 'My number is (변수)' 를 출력하시오.

#  방법 1 

a = 'My number is '
b = 1

print(a, b)

# 방법 2

a = 'My number is '
b = 1

print(a + str(b)) # 더해주기 위해서는 형태가 맞아야함 

# 문자형과 숫자형을 더해주기 위해서는 숫자형을 문자형으로 바꾸어 주어야만 한다.

print(a + str(b))

# 방법 3

print('My number is {}'.format(b)) # format 처리 

# 두 개 이상의 값 넣기

print('오늘은 {}월 {}일 입니다.'.format(5, 10))

# 이름을 통한 값 넣기

print('오늘은 {month}월 {day}일 크리스마슈~.'.format(month = 12, day = 25))

a = '오늘은 {month}월 {day}일 크리스마슈~.'.format(month = 12, day = 25)

print(a)

# - 문자열 분해

# 'hello world' 를 'hello'와 'world'로 분리하시오.

a = 'hello world'

a.split()

# 'I am a boy' 를 각 단어를 기준으로 분리하시오.

a = '나는야 신당동 개발자'

a.split()

# 'I.am.a.boy' 를 '.'를 기준으로 분리하시오.

a = '나는야.신당동.개발자'

a.split('.')

a.split('.')