# 롤 랭킹 데이터 : https://www.kaggle.com/datasnaek/league-of-legends
# DataUrl = ‘https://raw.githubusercontent.com/Datamanim/pandas/main/lol.csv’

import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# 데이터를 로드하라. 데이터는 \t을 기준으로 구분되어있다.
df = pd.read_csv("https://raw.githubusercontent.com/Datamanim/pandas/main/lol.csv", sep="\t")
