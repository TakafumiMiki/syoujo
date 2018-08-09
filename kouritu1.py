import pandas as pd

path = r"C:\Users\karug\Desktop\syoujo\kouhousien.csv"
df = pd.read_csv(path,index_col=0)
res = df.assign(
    sum=df["zinryoku"] + df["zanyaku"] #+ df["haikyu"] + df["parts"]*3
)
#res1 = 時間的最高効率
res1 = df.assign(
    gpm = res["sum"] / res["time"] 
)
res1 = res1.sort_values(by = "gpm", ascending = False)
print(res1)
