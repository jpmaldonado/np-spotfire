"""
Inputs
----------
None: you need to modify the file path to your Excel file.

Output
----------
- df: Table with all projects concatenated.

"""

import pandas as pd
import glob

excel_file = "C:/Users/HP/Desktop/np-spotfire/data/python/Projects.xlsx"
excel_data = pd.read_excel(excel_file, sheet_name=None)
sheets = excel_data.keys()

df = pd.concat([excel_data[sheet] for sheet in sheets])

