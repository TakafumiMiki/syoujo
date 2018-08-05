import pandas as pd

path = r"C:\Users\karug\Desktop\syoujo\kouhousien.csv"
df = pd.read_csv(path,index_col=0)
#print(df["zinryoku"])

print(df)
