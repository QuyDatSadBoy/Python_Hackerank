import pandas as pd
import numpy as np
from IPython.display import display

if __name__ == '__main__':
    data = pd.read_csv("P4AI_BT1.csv")
    df = data.copy()
    for i in range(len(df.columns)):
        column_dtype = df[df.columns[i]].dtype
        if np.issubdtype(column_dtype, np.floating):
            Max = df[df.columns[i]].max()
            print(Max)
            Min = df[df.columns[i]].min()
            print(Min)
            df[df.columns[i]] = round((df[df.columns[i]]-Min)*1.0/(Max-Min), 1)
    print(df)


