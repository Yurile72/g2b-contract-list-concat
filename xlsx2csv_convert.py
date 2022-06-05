import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import os
import glob

excel_files = glob.glob('*.xlsx') # assume the path
# print(excel_files)
for excel in excel_files:
    # out = excel.split('.')[0]+'.csv'
    df = pd.read_excel(excel) # if only the first sheet is needed.
    df.to_csv(f'{excel}.csv')
