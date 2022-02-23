import requests
import json

url = 'https://jsonplaceholder.typicode.com/posts/1'
data = {'userId':1, 'id':10, 'Address and Pincode':'Chennai_58', 'Completed': 'True' }
headers = {'Content-Type':'application/json; charset=UTF-8'}
response = requests.put(url, data=json.dumps(data), headers=headers)


# 200
print(response.status_code)

# True
print(response.ok)

print(response.content)

print(response.text)

# <class 'str'>
print(type(response.text))

# https://jsonplaceholder.typicode.com/posts
print(response.url)

# application/json; charset=utf-8
print(response.headers['Content-Type'])

# utf-8
print(response.encoding)
