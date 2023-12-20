# Other http methods
# Using post method
import requests
#url=('https://httpbin.org/post')
#req=requests.post(url,data={'key':'value'})
#print(req)

# using put
#url=('https://httpbin.org/put')
#req=requests.put(url,data={'key':'value'})
#print(req)

#using head method
#url=('https://httpbin.org/get')
#req=requests.head(url)
#print(req.headers['Connection'])

#using delete method
url=('https://httpbin.org/delete')
req=requests.delete(url)
json_response=req.json()
print(json_response["args"])
