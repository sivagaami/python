import pandas as pd
ddf = pd.read_csv('C:\\Users\\Admin\\Desktop\\j\\matches.csv')

ddf.head()

#to print columns
ddf.columns

f=ddf['win_by_wickets'].loc[ddf['win_by_wickets']!=0]
print('f')

#mean
f.mean()

#Standard deviation
f.std()

#group by
grouped__df = ddf.groupby(["city", "winner"])
for key,item in grouped__df:
  a_group = grouped__df.get_group(key)
  print(a_group, "\n")
