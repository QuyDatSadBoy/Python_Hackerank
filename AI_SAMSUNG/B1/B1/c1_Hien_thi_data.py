import pandas as pd
from IPython.display import display

if __name__ == '__main__':
    data = pd.read_csv("P4AI_BT1.csv")
    print(data.to_string())
