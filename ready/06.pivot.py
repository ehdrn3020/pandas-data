import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

###                        ###
### 06 Pivot               ###
###                        ###

# 국가별 5세이하 사망비율 통계
df= pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/timeTest.csv')

# Indicator을 삭제하고 First Tooltip 컬럼에서 신뢰구간([]대괄호)에 해당하는 표현을 지워라
df_new = df.drop(columns=['Indicator'])
df_new['First Tooltip'] = df_new['First Tooltip'].str.split('[').str[0].astype('float')

# Dim1에 따른 년도별 사망비율의 평균을 구하라, unstack()-> blog형식의 표
df_new.groupby(['Location','Period','Dim1']).mean().unstack()