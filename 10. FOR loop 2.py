import pandas as pd
brics = pd.read_csv("brics.csv", index_col=0)
print(brics)
for val in brics:
    print(val)

print("______")
for lab,row in brics.iterrows():
    print(lab)
    print(row)
print("_______")
for lab, row in brics.iterrows():
    print(lab + " : " + row["capital"])

print("_______")
for lab, row in brics.iterrows():
    brics.loc[lab, "panjang_karakter"] = len(row["country"])
print(brics)