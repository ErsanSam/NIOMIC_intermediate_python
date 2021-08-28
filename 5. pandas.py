import pandas as pd
brics = {'country':['Brazil','Rusia','India','China','South Africa',],
         'capital':['Brasilian','Moscow','New Delhi','Beijing','Prectoria'],
         'area':[8.516,17.10,3.286,9.597,1.221],
         'population':[200.4,143.5,1252,1357,52.98]}
brics = pd.DataFrame(brics)
brics.index = ['BR','RU','IN','CH','SA']
print(brics)
brics = pd.read_csv('brics.csv',index_col=0)
print(brics)