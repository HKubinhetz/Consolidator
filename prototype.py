# This code is used for eventual tests.

import tkinter as tk
from tkinter import filedialog as fd, messagebox as mb

import glob

# import tkMessageBox
mb.showinfo(title="Greetings", message="Hello, World!")
root = tk.Tk()
    root.withdraw()

""" 
def get_folder():
    root = tk.Tk()
    root.withdraw()

    # files = glob.glob("C:\\Users\\CS317813\\Desktop\\DadosTBGConsolidados\\*.csv")
    filepath = fd.askdirectory(initialdir="C:\\Users\\CS317813\\Desktop\\DadosTBGConsolidados",
                               title="Selecione a pasta que deseja consolidar os CSVs").replace("/", '\\')

    files = glob.glob(filepath + "\*.csv")

    return files
"""

