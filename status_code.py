# For raising expcetions while generating the resppnse
import requests


urls = ['https://httpbin.org', 'https://api.github.com/invalid']

for url in urls:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print('Success!')
