#Exceptions can be reaised if requests time runs out -requests.exception(Timeout)
import requests
from requests.exceptions import Timeout
try:
    reponse=requests.get('https://httbin.org',timeout=1)
except Timeout:
    print("The request timed out")
else:
    print("The request did not time out ")