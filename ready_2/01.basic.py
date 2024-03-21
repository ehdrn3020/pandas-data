import pandas as pd
df1 = pd.DataFrame(
    [[3,2,5],[10,0,2],[6,5,3]],
    columns=["사과", "자두", "포도"],
    index=["이성계", "김유신", "이순신"]
)


### values, index, columns 확인 ###
df1.values
# array([[ 3,  2,  5],
#        [10,  0,  2],
#        [ 6,  5,  3]])

df1.index
# Index(['이성계', '김유신', '이순신'], dtype='object')

df1.columns
# Index(['사과', '자두', '포도'], dtype='object')

df1.sum()
# 사과    19
# 자두     7
# 포도    10
# dtype: int64

df1.values > 3
# array([[False, False,  True],
#       [ True, False, False],
#       [ True,  True, False]])

df1 > 3
#       사과	    자두	    포도
# 이성계	False	False	True
# 김유신	True	False	False
# 이순신	True	True	False