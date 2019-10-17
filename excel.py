import pandas as pd
import numpy as np


fileNameStr1 = '大表.xlsx'
fileNameStr2 = 'zong.xlsx'
yuanbiao=pd.DataFrame(pd.read_excel(fileNameStr1))
locate=pd.DataFrame(pd.read_excel(fileNameStr2))
# df = pd.read_excel(fileNameStr2)
# print(df.head())
loan_inner=pd.merge(yuanbiao,locate,how='right')
print(loan_inner)
loan_inner.to_excel('zong1.xlsx')