#To  understand to include custom headers with the help of request-headers
# example url- www.example.com
import requests
url=('https://www.example.com')
custom_headers = {
    'User-Agent': 'MyApp/1.0',  
    'Authorization': 'Bearer YOUR_ACCESS_TOKEN', 
    'Custom-Header': 'Custom-Value'  
}
response=requests.get(url,params="html",headers=custom_headers)
if response.status_code == 200:
    print('Request was successful!')
    print('Response content:\n', response.text)
else:
    print(f'Request failed with status code {response.status_code}')
    print('Response content:\n', response.text)