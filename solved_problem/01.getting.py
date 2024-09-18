# 롤 랭킹 데이터 : https://www.kaggle.com/datasnaek/league-of-legends
# DataUrl = ‘https://raw.githubusercontent.com/Datamanim/pandas/main/lol.csv’

import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

###                           ###
### 01 Getting & Knowing Data ###
###                           ###

# 데이터 로드, 데이터는 \t을 기준으로 구분
df = pd.read_csv("https://raw.githubusercontent.com/Datamanim/pandas/main/lol.csv", sep="\t")

# 제공 메소드 확인
dir(df) # help(df)

# 데이터의 행과 열의 갯수
df.shape
# (51490, 61) -> tuple

# 컬럼 확인
df.columns[2:6]

# 데이터 타입 확인
df.info()
df['creationTime'].dtype # dtype('int64')
df[df.columns[1]].dtype

# 3번째 컬림의 4번째 값
df[df.columns[2]][3] # 인덱스는 0부터 시작
df.iloc[3,2] # [행, 열]


# 데이터 로드, 한글데이터(utf-8 > cp949 > euc-kr > latin)
df_kr = pd.read_csv("https://raw.githubusercontent.com/Datamanim/pandas/main/Jeju.csv", encoding='euc-kr')

# 3번째 컬럼의 10~20번째 값
df_kr.iloc[10:20,4]

# 수치형 변수(int64, float64)를 가진 컬럼을 출력
df_kr.select_dtypes(include=[int, float], exclude=object).columns # (include, exclude)

# 각 컬럼의 null 값의 수를 파악
df_kr.isnull().sum()

# 수치형변수의 분포(사분위, 평균, 표준편차, 최대, 최소)를 확인
df_kr.describe()

# 읍면동명의 유일 값을 출력 (series)
df_kr['읍면동명'].unique()
