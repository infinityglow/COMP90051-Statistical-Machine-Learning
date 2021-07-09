import pandas as pd
from preprocess import preprocess

df = pd.read_csv("../submit.csv")
df_test = pd.read_csv("../data/test-public.csv")

df_test = df_test[['Source', 'Sink']].values

pairs = preprocess("../data/train.txt")
for i in range(df_test.shape[0]):
    if tuple(df_test[i]) in pairs:
        df["Predicted"].iloc[i] = 1.0


df.to_csv("submit1.csv", index=False)
