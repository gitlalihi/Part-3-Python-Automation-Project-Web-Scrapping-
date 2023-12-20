# Using Timeout passed as tuples
import requests
url=('https://httpbin.org')

response=requests.get(url,timeout=(2,5))

print(response)


