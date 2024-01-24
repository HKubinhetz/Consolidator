import pandas as pd
import glob
from datetime import datetime
import tkinter as tk
from tkinter import filedialog as fd

# -------------- Function Declarations ------------


def get_folder():
    # Creates a Tkinter window to select a folder directory with desired files,
    # then returns the compiled list.
    root = tk.Tk()
    root.withdraw()

    filepath = fd.askdirectory(initialdir="C:\\Users\\CS317813\\Desktop\\DadosTBGConsolidados",
                               title="Selecione a pasta que deseja consolidar os CSVs").replace("/", '\\')

    filelist = glob.glob(filepath + "\*.csv")

    return filelist


# ----------------- Main Procedure  -----------------

# Function calling
files = get_folder()

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


