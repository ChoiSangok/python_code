# 3. 자료형

# - 자료형
# 저장되는 데이터의 형태

a = 1
b = 0.1
c = 'hello'

print(type(a))
print(type(b))
print(type(c))

## 1) 숫자형

# - int
# 정수의 형태

a = 1
print(type(a))

b = 0
print(type(b))

c = -1
print(type(c))

# - float
# 실수의 형태

a = 1.1
print(type(a))

b = 0.0
print(type(b))

c = -1.1
print(type(c))

d = 1.
print(type(d))

# - int 와 float 의 연산 결과는 int 일까, float 일까?  float!

a = 1
b = 1.0

print(type(a))
print(type(b))

print(type(a + b))

# - 연산

# 더하기

a = 10
b = 2

a + b

# 빼기

a = 10
b = 2

a - b

# 곱하기

a = 10
b = 2

a * b

# 나누기

a = 10
b = 2

a / b

# 몫

a = 10
b = 3

a // b

# 나머지

a = 10
b = 3

a % b

# 제곱

a = 10
b = 3

a ** b

# * 할당연산

# 변수 a 는 1 이다. 해당 변수 a 에 1을 더하여라.

a = 1
a = a + 1

print(a)

# 할당연산을 사용한 방법

a = 1
a += 1

print(a)

# 빼기

a = 1
a -= 1

print(a)

# 곱하기

a = 2
a *= 2

print(a)

# 나누기

a = 1
a /= 2

print(a)