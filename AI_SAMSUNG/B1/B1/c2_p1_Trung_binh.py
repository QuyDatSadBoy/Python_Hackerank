import pandas as pd
import numpy as np
from IPython.display import display

if __name__ == '__main__':
    data = pd.read_csv("P4AI_BT1.csv")
    print(data.isna().sum())

    for i in range(len(data.columns)):
        column_dtype = data[data.columns[i]].dtype
        if np.issubdtype(column_dtype, np.floating):
            res = round(data[data.columns[i]].mean(), 1)
            data[data.columns[i]].fillna(res, inplace=True)

    print(data.isna().sum())
    print(data)
