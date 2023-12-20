#Inspecting the request  by different methods

import requests

response=requests.post('https://httpbin.org/post',json={'key':'value'})
json_data=response.json()
print(json_data)

#We can view  the PreparedRequest by accessing .request:
print(response.request.headers['Content-Type'])

# To get request url
print(response.request.url)

#To get response body
response.request.body

#Using a Proxy for Inspection:
#example
'''url = 'https://example.com'
proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}
response = requests.get(url, proxies=proxies)'''

if response.status_code == 200:
    print(response.text)
else:
    print(f"Request failed with status code {response.status_code}")