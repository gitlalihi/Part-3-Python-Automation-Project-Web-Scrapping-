# Making a get request to return a Status code
import requests

response= requests.get('https://api.github.com')
#print(response.status_code)
if response.status_code==200:
    print("Sucessful!")
elif response.status_code==404:
    print("Not found")
