import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

###                        ###
### 03 Grouping            ###
###                        ###

df= pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/AB_NYC_2019.csv')

# 데이터의 각 host_name의 빈도수를 구하고 host_name으로 정렬하여 상위 5개를 출력하라 ( 내림차순 )
df['host_name'].value_counts().head(5)
# 오름차순
df['host_name'].value_counts().sort_values(ascending=True).head(5)

# 데이터의 각 host_name의 빈도수를 구하고 빈도수 기준 내림차순 정렬한 데이터 프레임을 만들어라. 빈도수 컬럼은 counts로 명명하라
df['host_name'].value_counts().to_frame().rename(columns={'host_name': 'counts'})

# neighbourhood_group의 값에 따른 neighbourhood컬럼 값의 갯수를 구하여라
# 두개의 컬럼을 가져올 때는 DataFrame 이여야 한다.
df[['neighbourhood_group', 'neighbourhood']].groupby(['neighbourhood_group', 'neighbourhood'], as_index=False).size()

# neighbourhood_group 값에 따른 price 최대, 최소 값을 구하여라
df[['neighbourhood_group','price']].groupby('neighbourhood_group').agg(['max', 'min'])

# neighbourhood_group 값이 Queens값을 가지는 데이터들 중 neighbourhood 그룹별로 price값의 최대, 최소값을 구하라
df.loc[df['neighbourhood_group']=='Queens'].groupby('neighbourhood_group')['price'].agg(['max', 'min'])