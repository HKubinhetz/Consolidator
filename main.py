import pandas as pd
import glob

# TODO - BUILD A FILE SELECTOR
files = glob.glob("C:\\Users\\ricku\\Desktop\\Amostragem\\Smallsample\\*.csv")

# Declaring an empty DataFrame list
df_list = []

# For loop to append all selected files.
for f in files:
    csv = pd.read_csv(f, delimiter=";")
    df_list.append(csv)

# Concatenating files and clearing base (setting date column to correct format and removing duplicates)
sales = pd.concat(df_list)
sales['DateTime'] = pd.to_datetime(sales['DateTime'])
sales = sales.drop_duplicates(subset='DateTime', keep='first')
print(sales)

# sales.to_csv('Consolidated.csv')


