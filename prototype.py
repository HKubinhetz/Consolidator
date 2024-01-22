# This code is used for eventual tests.

import tkinter as tk
from tkinter import filedialog as fd
import glob

root = tk.Tk()
root.withdraw()

filepath = fd.askdirectory(initialdir="C:\\Users\\CS317813\\Desktop\\Dados TBG - Amostragem",
                           title="Escolha seu Arquivo!").replace("/", "\\")

files = glob.glob(filepath + "*.csv")
print(files)

print(type(filepath))


