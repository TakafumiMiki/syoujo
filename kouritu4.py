import pandas as pd

path = r"C:\Users\miki\Desktop\syoujo\kouhousien.csv"
df = pd.read_csv(path,index_col=0)

#res4 = 全素材最大数
def allSys(num):
    res4 = df.sort_values(num, ascending = False)
    print(res4)

def numchenge(getnum):
    if getnum == "1":
        getnum = "zinryoku"
    elif getnum == "2":
        getnum = "zanyaku"
    elif getnum == "3":
        getnum = "haikyu"
    elif getnum == "4":
        getnum = "parts"
    allSys(getnum)
#優先度の順を決める

print("優先度の選択\n1:人力 2:弾薬 3:配給 4:パーツ")
getnum = input()

numchenge(getnum)
print(getnum)
