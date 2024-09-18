# 사전 예제 코드
import pandas as pd
a1 = [60, 84, 80, 70, 19]
a2 = [77, 62, 95, 85, 17]
a3 = [61, 97, 72, 67, 15]
a4 = [75, 65, 95, 51, 18]
cols = ["국어", "영어", "수학", "과학", "나이"]
df = pd.DataFrame([a1, a2, a3, a4], index=list("ABCD"), columns=cols)

# 정렬
# df.sort_values([col1, col2, colN...], ascending=bool)

# [1] 1개의 열을 기준으로 오름차순, 내림차순
df.sort_values("국어") # 오름
df.sort_values("영어", ascending=False) # 내림

# [2] 2개 이상의 열을 기준으로 정렬 (리스트 형식으로 파라미터)
df.sort_values(["수학", "영어"], ascending=False)

# [3] 2개 이상의 열기준 오름&내림 혼합
df.sort_values(["수학", "나이"], ascending=[0, 1])