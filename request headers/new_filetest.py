import requests

response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json'},
)


json_response = response.json()
repository = json_response['items'][0]
print(f'Text matches: {repository["text_matches"]}')
