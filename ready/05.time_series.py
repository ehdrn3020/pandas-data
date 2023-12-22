import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

###                        ###
### 05 Time Series         ###
###                        ###

df= pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/timeTest.csv')

#Yr_Mo_Dy을 판다스에서 인식할 수 있는 datetime64타입으로 변경하라
df.loc[:,'Yr_Mo_Dy'] = pd.to_datetime(df['Yr_Mo_Dy']) # dtype: datetime64
# Month 만 추출
pd.to_datetime(df['Yr_Mo_Dy']).dt.month

## 컬럼에 날짜 형식이나 잘못된 값이 섞여 있는 경우 ##
# errors='coerce' 옵션을 사용하여 잘못된 값이 있을 경우 NaT(Not a Time)으로 대체
df['Yr_Mo_Dy'] = pd.to_datetime(df['Yr_Mo_Dy'], errors='coerce')
# NaT 값이 있는 행 제거
df = df.dropna(subset=['Yr_Mo_Dy'])
df.loc[:,'Yr_Mo_Dy'] = pd.to_datetime(df['Yr_Mo_Dy'], errors='coerce')
df['Yr_Mo_Dy']

# Yr_Mo_Dy에 존재하는 년도의 유일값을 모두 출력하라
df['Yr_Mo_Dy'].dt.year.unique()

# 년도별 각컬럼의 평균값을 구하여라
df.groupby(df['Yr_Mo_Dy'].dt.year).mean()

# 년도 - 월을 기준으로 모든 컬럼의 평균값을 구하여라
df.groupby(df['Yr_Mo_Dy'].dt.strftime('%Y-%m')).mean()

# RPT 컬럼의 값을 일자별 기준으로 1차차분하라 ( 그 다음 행과 비교하여 차이 값을 출력 )
df.loc[:,'diff_1'] = df['RPT'].diff()
