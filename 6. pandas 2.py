import pandas as pd
brics = pd.read_csv("brics.csv", index_col=0)
print(brics[["country"]])
print(brics[1:4])
print(brics.loc[["RU"]])
print(brics.loc[["RU","BR"]])
print(brics.loc[['BR','RU','IN'],['capital','area']])
print("____")
print(brics.iloc[[1,2],[1]])