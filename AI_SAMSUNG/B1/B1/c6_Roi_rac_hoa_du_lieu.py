import pandas as pd
import numpy as np
from IPython.display import display

if __name__ == '__main__':
    data = pd.read_csv("P4AI_BT1.csv")
    df = data.copy()
    bins = [4.0, 5.0, 6.0, 7.0, 8.0]
    labels = ["Very Low", "Low", "Medium", "High"]
    df["sepal.length"] = pd.cut(
        df["sepal.length"], bins=bins, labels=labels)
    display(df)
