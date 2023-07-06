import pandas as pd

# read_csv
df = pd.read_csv("data.csv")
print(df["Series_reference"])
print(df.columns)
# xoa cot df=df.drop(column = 'Series_reference')
print(len(df))
print(df.query("Magnitude > 6"))
# df.insert(index,ten,gia_tri)
# print(df['Series_reference'].unique())
print(df.head(2))
print(df.tail(4))
print(df.describe())
print(df.dtypes)
# print(df.loc[3:5, ["Period", "Dara_value"]])
# print(df.iloc[3:5,1:3]) khong lay can cuoi
print(df["Series_reference"].value_counts())
df.sort_values(by="Series_reference", inplace=True)
# giam dan them ascending = False
# df.sort_values(by=['Name','old'],ascending=[True,False])
clean_data = df.dropna()
clean_data = df.fillna(0)
print(clean_data)
# print(df["Series_reference"])
