import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

###                        ###
### 04 Apply & Map         ###
###                        ###

df= pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/BankChurnersUp.csv')

# Income_Category의 카테고리를 map 함수를 이용하여 다음과 같이 변경하여 newIncome 컬럼에 매핑하라
dic = {
    'Unknown' : 'N',
    'Less than $40K' : 'a',
    '$40K - $60K' : 'b',
    '$60K - $80K' : 'c',
    '$80K - $120K' : 'd',
    '$120K +' : 'e'
}
df.loc[:,'newIncome'] = df['Income_Category'].map(dic)


# Income_Category의 카테고리를 apply 함수를 이용하여 다음과 같이 변경하여 newIncome 컬럼에 매핑하라
def income_mapper(x):
    return dic[x]
df['Income_Category'].apply(income_mapper)


# Education_Level의 값중 Graduate단어가 포함되는 값은 1 그렇지 않은 경우에는 0으로 변경하여 newEduLevel 컬럼을 정의하고 빈도수를 출력하라
df.loc[:,'newEduLevel'] = df['Education_Level'].map(lambda x: 1 if 'Graduate' in x else 0)
df['newEduLevel'].value_counts()


# Marital_Status 컬럼값이 Married 이고 Card_Category 컬럼의 값이 Platinum인 경우 1 그외의 경우에는 모두 0으로 하는 newState컬럼을 정의하라.
def filter(x): # x는 series타입
    return 1 if x['Marital_Status'] == 'Married' and x['Card_Category'] == 'Platinum' else 0
# axis = 0 : 열 / axis = 1 : 행
df.loc[:,'newEduLevel'] = df[['Marital_Status','Card_Category']].apply(filter, axis=1)