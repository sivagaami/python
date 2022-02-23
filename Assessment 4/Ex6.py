import pandas as pd
import io
import requests
url="https://jsonplaceholder.typicode.com/todos"
s=requests.get(url).content
c=pd.read_json(io.StringIO(s.decode('utf-8')))

# To display 7 records
c.head(7)
