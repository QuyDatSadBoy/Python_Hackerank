import pandas as pd
from IPython.display import display

data = pd.read_csv("P4AI_BT1.csv")
sample_data = data.sample(frac=0.5, replace=True)
print(sample_data)
