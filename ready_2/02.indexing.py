# 예제
import pandas as pd
import numpy as np
a = np.random.randint(0,10,24).reshape(4,6)
df = pd.DataFrame(a, index=list("가나다라"), columns=list("ABCDEF"))

# df["열이름"] : 열만가능
df["A"]
# 가    5
# 나    7
# 다    7
# 라    9
# Name: A, dtype: int64

df[["A","B","C"]]
#    A	B	C
# 가	 5	7	1
# 나	 7	3	9
# 다	 7	3	4
# 라	 9	5	6

# df.loc["행이름", "열이름"]
df.loc["가":"다", "A":"D"]
#    A	B	C	D
# 가  5	7	1	5
# 나  7	3	9	3
# 다  7	3	4	9

df.loc["가":"다", ["A","B","A"]]
#    A	B	A
# 가  5	7	5
# 나	 7	3	7
# 다	 7	3	7

# df.iloc[행번호, 열번호]
df.iloc[0:3,[0,1,0]]
#    A	B	A
# 가  5	7	5
# 나	 7	3	7
# 다	 7	3	7

# drop 함수
df.drop("D", axis=1) # 행=0(default), 열=1
# 	A	B	C	E	F
# 가	5	7	1	5	2
# 나	7	3	9	9	0
# 다	7	3	4	6	3
# 라	9	5	6	4	4

# 문제 : B,D,E,F열과 가,나,다 행의 자료를 추출하라
df.iloc[:3, 1:].drop("C", axis=1)