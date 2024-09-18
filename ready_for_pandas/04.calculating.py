# numpy의 연산은 똑같은 배열의 크기 일 때 가능하지만, 열의 크기가 같을 때 행은 자동적으로 확장한다.
# 예제
# 0 1 2     0 1 2     0 1 4
# 1 2 3  X         =  0 2 6
# 2 3 4               0 3 8

# pandas는 열의 자리가 달라도 라벨링 되어있기에 열의 자리는 중요하지 않다.
# A B C     B A     A B C
# 0 1 2     1 0     0 1 nan
# 1 2 3  X  1 0  =  0 2 nan
# 2 3 4             nan anan nan

import pandas as pd
a1 = [[1,2,3], [4,5,6,], [7,8,9]]
df1 = pd.DataFrame(a1, columns=list("ABC"), index=list("가나다"))
df2 = df1.reindex(columns=list("BCA"), index=list("나다가")).copy()
sr1 = df1.loc["가"]
df3 = df1.iloc[:2,:2]

# [1] 기본 예제
df1 + df3
# >>>
#   A	B	 C
#가	2.0	4.0	 NaN
#나	8.0	10.0 NaN
#다	NaN	NaN	 NaN

# [2] fill_value : NaN일 때의 기본값을 정하고 싶을 때
df1.add(df3, fill_value=0)
#   A	B	C
#가	2.0	4.0	 3.0
#나	8.0	10.0 6.0
#다	7.0	8.0	 9.0

# [3] 행(1)과 열(0)을 기준으로 broadcasting 연산
df1.add(sr1, axis=1)