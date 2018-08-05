import pandas as pd

path = r"C:\Users\karug\Desktop\syoujo\kouhousien.csv"
df = pd.read_csv(path,index_col=0)
res = df.assign(
    sum=df["zinryoku"] + df["zanyaku"] + df["haikyu"] + df["parts"]*3
)
"""
#res1 = 時間的最高効率
res1 = df.assign(
    gpm = res["sum"] / res["time"] 
)
res1 = res1.sort_values(by = "gpm", ascending = False)
print(res1)
"""
#res2 = 素材選択型最高効率
def dataSys(name):
    res2 = df.assign(
        selpm = round(res[name] / res["time"],2)
    )
    res2 = res2.sort_values(by = "selpm", ascending = False)
    print(res2)

data = input("欲しいのは何か\n1:人力 2:弾薬 3:配給 4:パーツ")

if data == "1":
    dataSys("zinryoku")

elif data == "2":
    dataSys("zanyaku")
    
elif data == "3":
    dataSys("haikyu")

elif data == "4":
    dataSys("parts")
