# 5. List Comprehension

# 변수 a 에 1 부터 10 까지 삽입하시오.

a = []
for i in range(1, 11, 1):
    a.append(i)
print(a)

a = [i for i in range(1, 11, 1)]
print(a)

# 변수 a 에 1 부터 10 까지의 제곱의 값을 삽입하시오.

a = []
for i in range(1, 11, 1):
    a.append(i ** 2)
print(a)

a = [i ** 2 for i in range(1,10,1)]
print(a)

# 변수 a 에는 A 반의 수학점수가 저장되어 있다. 이 중 80점 이상의 점수만 걸러내어라.

a = [90, 39, 48, 70, 82, 100]

result = [i for i in a] # a
print(result)

res = [i for i in a if i>=80]
print(res)