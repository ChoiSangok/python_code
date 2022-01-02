# 6. 함수

# 함수의 예

print(1)
type(1)

# 함수를 만드는 이유

a = 1
b = a * 100
b = b ** 2
c = b + 2 * a

# 똑같은 작업을 여러번 반복해야 한다면?

# * 생성방법

# def 함수명(인풋 값):
#     실행 내용

# x 를 입력값으로 넣으면 x + 1 을 출력하는 함수 생성

def func1(x):
    print(x + 1)

func1(1)

# x 를 입력값으로 넣으면 x + 1 을 반환하는 함수 생성

def function2(x):
    result = x + 1
    return result

a = function2(1)
print(a)

# x 를 입력값으로 넣으면 x + 1, x + 2 를 반환하는 함수 생성

def function3(x):
    result1 = x + 1
    result2 = x + 2
    return result1, result2

a, b = function3(1)
print(a)
print(b)

# * 여러개의 입력값을 받고 싶을 때
# 여러개의 입력값을 받아 순서대로 출력

def function4(x):
    for i in x:
        print(i)

a = [1, 3, 5, 7, 4, 'd', 2, 60]
function4(a)

# args 를 이용한 구현

def function5(*args): # *가 필수
    for i in args:
        print(i)

function5(1, 3, 5, 7, 4, 'd', 2, 60)