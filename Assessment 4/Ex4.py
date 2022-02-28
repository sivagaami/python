import pandas as pd
Matches_played = pd.read_csv('C:\\Users\\Admin\\Desktop\\j\\matches.csv')

Matches_played.head()

#to print columns
Matches_played.columns

f=Matches_played['win_by_wickets'].loc[ddf['win_by_wickets']!=0]
print('f')

#mean
f.mean()

#Standard deviation
f.std()

#group by
group = Matches_played.groupby(["city", "winner"])
for key,item in group:
  df_group = group.get_group(key)
  print(df_group, "\n")
  
 # Conditional Probability
Total_matches =(Matches_played['city'].value_counts()['Mumbai'])
Total_matches

Mumbai =(Matches_played['winner'].value_counts()['Mumbai Indians'])
Mumbai

probability = Mumbai / Total_matches
probability
