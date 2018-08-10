import pandas as pd

path = r"C:\Users\miki\Desktop\syoujo\kouhousien.csv"
df = pd.read_csv(path,index_col=0)

#res3 = 全素材最高効率表
def allSys(num):
    res3 = df.assign(
        zpm = round(df["zinryoku"] / df["time"],2),
        dpm = round(df["zanyaku"] / df["time"],2),
        hpm = round(df["haikyu"] / df["time"],2),
        ppm = round(df["parts"] / df["time"],2),
        apm = (df["zinryoku"] + df["zanyaku"] + df["haikyu"] + df["parts"]*3) /df["time"] 
    )
    #今は適当
    res3 = res3.sort_values(["apm",num[0],num[1],num[2],num[3]], ascending = [False,False,False,False,False])
    print(res3)
    res3.to_csv("select.csv")

def numchenge(getnum):
    for i in range(4):
        if getnum[i] == "1":
            getnum[i] = "zpm"
        elif getnum[i] == "2":
            getnum[i] = "dpm"
        elif getnum[i] == "3":
            getnum[i] = "hpm"
        elif getnum[i] == "4":
            getnum[i] = "ppm"
    allSys(getnum)
#優先度の順を決める
getnum = []
print("優先度の選択\n1:人力 2:弾薬 3:配給 4:パーツ")
for num in range(4):
    getnum.append(input())

numchenge(getnum)
print(getnum)
