import pandas as pd
import numpy as np
from IPython.display import display

if __name__ == '__main__':
    data = pd.read_csv("P4AI_BT1.csv")
    df = data.copy()
    dummies = pd.get_dummies(df['variety'])
    print(dummies)
    df.drop(columns=['variety'], inplace=True)
    df = pd.concat([df, dummies], axis=1)
    print(df)
