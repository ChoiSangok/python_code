## 4) 튜플

a = (1, 2, 3) # () 가 특징

print(type(a))

# * 인덱스가 존재!

print(a[1]) 

# * 슬라이스

a = (1, 2, 3)

print(a[:2])

# * 치환하기

a = (1, 2, 3)

a[2] = 0 # 안됌!
# 리스트와 튜플의 차이는 치환문제! 대부분은 리스트 사용 ** 값이 변해야 하기 때문에
# 튜플은 개인정보등 정보가 변하지 않을때 사용 

# * 튜플 더하기

a = (1, 2, 3)
b = (4, 5, 6)

c = a + b
print(c)

# * 튜플 곱하기

a = (1, 2, 3)

b = a * 2
print(b)

#####################

## 5) 딕셔너리

# - 생성방법
# - 딕셔너리(dict)는 Key 와 Value 로 구성

a = {'사자' : 'lion',
     '호랑이' : 'tiger', 
     '용' : 'dragon'
    }

print(a)
print(type(a))
 

#  하나의 Key 에 여러개의 Value 로도 구성이 가능

a = {'car' : ['bus', 'truck', 'taxi'],
    'train' : 'ktx'}

print(a)

# * key 얻기

a = {'car' : ['bus', 'truck', 'taxi'],
    'train' : 'ktx'}

key = a.keys()
print(key)
value =a.values()
print(value)

print(type(key))

print(key[0]) #안됌!
# 형변환을 통해서 리스트 구조로 형 변환후에 값 가져오기 

key2 = list(key)
print(key2)
print(type(key2))

print(key2[0])

# * value 얻기

a = {'car' : ['bus', 'truck', 'taxi'],
    'train' : 'ktx'}

value = a.values()
print(value)

print(type(value))

# print(value[0]) #형변환 통해서 가져오기 
value2= list(value)
print(value2[0])

value2 = list(value)
print(value2)
print(type(value2))

print(value2[0])

# * 요소 추가하기

a = {'car' : ['bus', 'truck', 'taxi'],
    'train' : 'ktx'}

a['plane'] = 'jet'
print(a)

# * 요소 삭제하기

a = {'car' : ['bus', 'truck', 'taxi'],
    'train' : 'ktx'}

del a['car']
print(a)

###############

## 6) 셋

# - 생성방법

a = set([1, 2, 3]) #리스트나 튜플로 둘다 사용 가능~!
print(a)
print(type(a))

# - 또는

a = set((1, 2, 3))
print(a)

# - 중복된 항목을 제거

a = set([1, 1, 2, 3, 3, 4])

print(a)

# -  순서가 없음

a = set([4, 4, 3, 2, 1, 'a', 'b', 'a']) 


print(a)

print(a[0]) 
# 순서 자체가 없어서 인덱스가 존재하지 않음!
# 얻고 싶으면 형변환 후 가져오면됌 예를 들어 리스트

b = list(a)
print(b)

print(b[0])

# - 합집합

a = set([1, 2, 3])
b = set([3, 4, 5])

c = a.union(b)
print(c)

# * 교집합

a = set([1, 2, 3])
b = set([3, 4, 5])

c = a.intersection(b)
print(c)

# * 차집합

a = set([1, 2, 3])
b = set([3, 4, 5])

c = a.difference(b)
print(c)