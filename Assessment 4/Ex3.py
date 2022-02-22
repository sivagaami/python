import pandas as pd
ddf = pd.read_csv('C:\\Users\\Admin\\Desktop\\j\\nba.csv')
ddf.head()
ddf.shape
ddf.dtypes
ddf.describe()
ddf.median()
ddf['Age'].median()
