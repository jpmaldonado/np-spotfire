import pandas as pd
import glob

directory_name = "C:/Users/HP/Desktop/np-spotfire/data/python"
files = glob.glob(glob.escape(directory_name) + "/*.csv")

df = pd.concat(map(pd.read_csv, files))
