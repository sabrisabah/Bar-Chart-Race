import pandas as pd
import os
import numpy as np
import glob

os.chdir("C:\\project")
data_corona = pd.read_csv('cov.csv', index_col = 'date')#
data_corona.head()

cols = ['ANBAR','BABYLON','BAGHDAD-KARKH','BAGHDAD-RESAFA','BASRAH','DAHUK','DIWANIYA','DIYALA','ERBIL','KERBALA','KIRKUK','MISSAN','MUTHANNA','NAJAF','NINEWA','SALAH AL-DIN','SULAYMANIYAH','THI-QAR','WASSIT']
subsetdf = data_corona[cols]

cum_sum_df = subsetdf.cumsum(axis=0)
cum_sum_df.tail(10)

import bar_chart_race as bcr
bcr.bar_chart_race(df=cum_sum_df, filename=None, figsize=(3.5,3), title='Covid by Iraq 2020')
