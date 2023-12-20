# Using Timeout parameter
import requests
url=('https://httpbin.org')
response=requests.get(url,timeout=1)

#response=requests.get(url,timeout=3.05)   pass values by float
print(response)


