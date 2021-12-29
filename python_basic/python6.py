### (1) for 

# for를 이용한 반복문은 아래와 같이 작성합니다.
# for 변수 in 반복 가능한 객체:
    # 반복하여 실행할 내용

# * 여기서 반복 가능한 객체는 아래와 같은 것들을 뜻합니다.

# list range

# 문제 : 1부터 10까지 출력하시오

#  - list 를 이용한 해결

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in a:  
    print(i)

#  * range 를 이용한 해결

for i in range(11):
     print(i)

# 문제 : 1부터 9까지 2씩 증가하면서 출력하시오.
for i in range(1, 10 , 2):
    print(i)

# 문제 : 9부터 1까지 2씩 감소하면서 출력하시오.

for i in range(9, 0, -2):
    print(i)

# 문제 : 1부터 10까지의 자연수의 합을 구하시오.

for i in range(1, 11, 1):
    print(i)

result = 0;
for i in range(1, 11, 1):
    result = result + i 

print(result)

result = 0
for i in range(1, 11, 1):
    result += i
print(result)


# 문제 : 구구단을 출력하시오.

for i in range(2, 10, 1):
    print(i)

for i in range(2, 10, 1):
     for j in range(1, 10, 1):
         print(i * j)

for i in range(2, 10, 1):
    for j in range(1, 10, 1):
        print(i * j)

for i in range(2, 10, 1):
    for j in range(1, 10, 1):
        print('{} 곱하기 {} 은/는 {} 입니다.'.format(i, j, i * j))



#  while
### (2) while

# while을 이용한 반복문은 아래와 같이 작성합니다.
# - while 조건: 반복하여 실행할 내용

# - 문제 : 1부터 10까지 출력하시오.

i = 1
while i < 11:
    print(i)
    i = i + 1

# 문제 : 1부터 9까지 2씩 증가하면서 출력하시오.

i = 1
while i < 10:
    print(i)
    i += 2

# 문제 : 9부터 1까지 2씩 감소하면서 출력하시오.

i = 9
while i > 0:
    print(i)
    i -= 2

# 문제 : 1부터 10까지의 자연수의 합을 구하시오.

i = 1
result = 0
while i < 11:
    result += i
    i += 1
print(result)

# 문제 : 구구단을 출력하시오.

i = 2
while i < 10:
    print(i)
    i += 1


i = 2
while i < 10:    
    j = 1
    while j < 10:
        print(i * j)
        j += 1
    i += 1


i = 2
while i < 10:
    
    j = 1
    while j < 10:
        print(i * j)
        j += 1

    i += 1


i = 2
while i < 10:
    
    j = 1
    while j < 10:
        print('{} 곱하기 {} 은/는 {} 입니다.'.format(i, j, i * j))
        j += 1

    i += 1