# **데이터 프레임 생성**

import pandas as pd
# pandas 외부라이브러리 활용

# * Dict 를 통한 데이터 프레임 생성

df = pd.DataFrame({'a': [1, 2, 3], 'b' : [4, 5, 6], 'c' : [7, 8, 9]})

# df 변수 생성 pandas 에 dataframe 활용

type(df)

dummy = {'a': [1, 2, 3], 'b' : [4, 5, 6], 'c' : [7, 8, 9]}

df2 = pd.DataFrame(dummy)

# * List 를 이용한 데이터 프레임 생성

a = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
b = [[1,2,3,],[4,5,6],[7,8,9]]

df3 = pd.DataFrame(a)
df4 = pd.DataFrame(b)

df3.columns = ['a', 'b', 'c']

# * 문제 : 아래 테이블과 같은 데이터 프레임을 만드시오.
a = {'company' : ['abc', '회사', 123], '직원수' : [400, 10, 6]}

df4 = pd.DataFrame(a)

# * 문제 : 아래 테이블과 같은 데이터 프레임을 만드시오.

a = {'company' : ['abc', '회사', 123], '직원수' : [400, 10, 6], '위치' : ['Seoul', NaN, 'Busan']}
# NaN 을 string 처럼 넣으면 에러 발생함 !!

# a = {'company' : ['abc', '회사', 123], '직원수' : [400, 10, 6], '위치' : ['Seoul', , 'Busan']} 에러

# NaN 을 공란처리하면 파이썬 에러 ! 

# numpy를 통한 해결
import numpy as np
# numpy 행렬등 딥러닝에서 사용되는 라이브러리 

a = {'company' : ['abc', '회사', 123], '직원수' : [400, 10, 6], '위치' : ['Seoul', np.NaN, 'Busan']}
# np.NaN 으로 

df5 = pd.DataFrame(a)

# **칼럼명 추출 / 변경** 

# * 데이터 프레임 생성

import pandas as pd

df = pd.DataFrame({'a': [1, 2, 3], 'b' : [4, 5, 6], 'c' : [7, 8, 9]})

# * 칼럼명 얻기

df.columns
# 칼럼명 얻기 

df.columns[1]

# - 문제 : 칼럼명인 a, b, c 를 d, e, f 로 바꾸어라.

# * 치환을 통한 칼럼명 변경

df.columns=(['d','e','f'])

# - 문제 : 칼럼명인 d, e, f 중 d 를 '디' 로 f 를 '에프' 로 바꾸어라.

df.columns=['디','e','에프']

# * rename 을 통한 칼럼명 변경

# 데이터 프레임 재생성
df = pd.DataFrame({'a': [1, 2, 3], 'b' : [4, 5, 6], 'c' : [7, 8, 9]})
df.columns = ['d', 'e', 'f']
# def로 칼럼명 변경

df.rename(columns = {'d' : '디', 'f' : '에프'})

# - inplace = True 로 되어 있어야 저장
df.rename(columns = {'d' : '디', 'f' : '에프'}, inplace = True)

# **copy 를 이용한 데이터 복사**

#  데이터 생성

import pandas as pd
df = pd.DataFrame({'a': [1, 2, 3], 'b' : [4, 5, 6], 'c' : [7, 8, 9]})

# 문제 : 필드명을 a, b, c 에서 d, e, f 로 변경하시오.

df.columns = ['d', 'e', 'f']

#  문제 : 필드명 a 를 '에이' 로 변경하시오.

df = pd.DataFrame({'a': [1, 2, 3], 'b' : [4, 5, 6], 'c' : [7, 8, 9]})

df.rename(columns = {'a' : '에이'}, inplace = True)

#  변수명을 복제하여 해결???

df = pd.DataFrame({'a': [1, 2, 3], 'b' : [4, 5, 6], 'c' : [7, 8, 9]})
df2 = df

# 문제 : 필드명을 a, b, c 에서 d, e, f 로 변경하시오.

df.columns = ['ㅎ', 'g', 'h']

# * deep copy 를 통한 해결

import copy

df = pd.DataFrame({'a': [1, 2, 3], 'b' : [4, 5, 6], 'c' : [7, 8, 9]})
df2 = copy.deepcopy(df)

df.columns = ['d', 'e', 'f']

# 안바뀜! deepcopy 의 중요~
#  변수명을 따로 저장하고 싶을때 머신러닝 등의 전처리 등 보험용 변수명이라고 생각하면 간단~!