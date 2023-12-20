# To see content after getting the reponse from the URL
import requests
url=('https://api.github.com')
response=requests.get(url)

#print(response.content)

'''To see the content in text format-.text()
print(response.text)'''

'''To deserialize content from the text-json() method
print(response.json())'''

