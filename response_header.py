# To access headers- gives-Cache-control,date,Server, etc
import requests
url=('https://httpbin.org')
response=requests.get(url)
print(response.headers)
#print(response.headers['content-type'])

