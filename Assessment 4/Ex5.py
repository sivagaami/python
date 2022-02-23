url = 'https://jsonplaceholder.typicode.com/todos'

#get the url
res = requests.get(url)

# print only 5 rows
json = res.json()
print(json[0:5])
