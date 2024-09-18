import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

###                        ###
### 02 Filtering & Sorting ###
###                        ###

df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/chipo.csv')

# quantitiy컬럼의 값이 3인 데이터만 첫 5행을 출력
df.loc[df.quantity == 3]

# quantity, item_price 두개의 컬럼으로 구성된 새로운 데이터프레임을 정의
df_new = df[['quantity', 'item_price']].copy()

# item_price 컬럼의 달러표시를 제거하고 float타입으로 저장하여 new_price 컬럼에 저장 ( str은 문자열 함수 사용하기 위해 )
df.loc[:, 'new_price'] = df['item_price'].str.replace('$', '').astype(float)

# new_price 컬럼이 5이하의 값을 가지는 데이터 프레임 추출
df.loc[df['new_price'] < 5]

# 전체 갯수
len(df.loc[df['new_price'] < 5 ])
df.loc[df['new_price'] < 5 ].shape[0]

# 다중조건, new_price값이 9이하이고 item_name값이 'Chicken Salad Bowl'인 데이터프레임 추출
df.loc[(df['new_price'] < 9) & (df['item_name'] == 'Chicken Salad Bowl')]

# (Like) item_name 컬럼 값중 'Chips' 포함하는 경우의 데이터 추출
df.loc[df['item_name'].str.contains('Chips')]
# 'Chips'를 포함하지 않는 경우의 데이터 추출
df.loc[~df['item_name'].str.contains('Chips')]

# item_name 기준으로 중복행이 있으면 첫번째 케이스만 남기기
df.loc[df['item_name'].str.contains('Chips')].drop_duplicates('item_name')
# 마지막 케이스만 남기기
df.loc[df['item_name'].str.contains('Chips')].drop_duplicates('item_name', keep='last')

# item_name 값이 Izze데이터를 Fizzy Lizzy로 수정
df.loc[df['item_name'] == 'Izze', 'item_name'] = 'Fizzy Lizzy'

# choice_description 값이 NaN인 데이터를 'NoData' 값으로 대체
df.loc[df['choice_description'].isnull(), 'choice_description'] = 'NoData' #DataFrame
df.loc[:'choice_description'] = df['choice_description'].fillna('NoData') #Series

# item_name의 문자열이 15이상인 데이터를 인덱싱
df.loc[df['item_name'].str.len() >= 15]

# new_price 값이 lst에 해당하는 경우의 데이터 프레임을 추출 lst =[1.69, 2.39, 3.39, 4.45, 9.25, 10.98, 11.75, 16.98]
lst =[1.69, 2.39, 3.39, 4.45, 9.25, 10.98, 11.75, 16.98]
df.loc[df['new_price'].isin(lst)]


# new_price 컬럼 값에 따라 오름차순으로 정리
df.sort_values('new_price')
# 내림차순
df.sort_values('new_price', ascending=False)


