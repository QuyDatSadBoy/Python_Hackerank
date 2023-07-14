import pandas as pd
import numpy as np
from IPython.display import display

if __name__ == '__main__':
    data = pd.read_csv("P4AI_BT1.csv")
    print(data.isna().sum())

    for i in range(len(data.columns)):
        List = data[data.columns[i]].mode()
        data[data.columns[i]].fillna(List[0], inplace=True)

    print(data.isna().sum())
    print(data)
