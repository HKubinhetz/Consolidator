import pandas as pd
import numpy as np
import glob

files = glob.glob("C:\\Users\\ricku\\Desktop\\Amostragem\\Smallsample\\*.csv")

df_list = []

for f in files:

    csv = pd.read_csv(f, delimiter=";")
    df_list.append(csv)

sales = pd.concat(df_list)

sales['DateTime'] = pd.to_datetime(sales['DateTime'])
print(sales.dtypes)

df_list.

pd.df_list.to_csv()

