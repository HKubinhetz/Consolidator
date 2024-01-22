import pandas as pd
import glob
from datetime import datetime

# TODO - Select all CSV Files in the folder after a given specification
# Consider using GLOB - https://docs.python.org/3/library/glob.html
# files_home = glob.glob("C:\\Users\\ricku\\Desktop\\Amostragem\\Smallsample\\*.csv")
files = glob.glob("C:\\Users\\CS317813\\Desktop\\DadosTBGConsolidados\\*.csv")

# Declaring an empty DataFrame list
df_list = []

# For loop to append all selected files.
for f in files:
    csv = pd.read_csv(f, delimiter=";")
    df_list.append(csv)

# Concatenating files and clearing base (setting date column to correct format and removing duplicates)
concatdata = pd.concat(df_list)
concatdata['DateTime'] = pd.to_datetime(concatdata['DateTime'])
concatdata = concatdata.drop_duplicates(subset='DateTime', keep='first')

# Defining Today's Date
todayDate = datetime.today().strftime('%d-%m')

# Exporting to Desktop
concatdata.to_excel('C:\\Users\\CS317813\\Desktop\\Dados Gemini - ' + todayDate + '.xlsx', index=False)


