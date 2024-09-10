import os
import pandas as pd
from numpy.ma.extras import row_stack

file_path = "09.xlsx"
cols = [1,2,3,4]
file = pd.read_excel("09.xlsx")



a = file._get_column_array(0)
b = set()

print()