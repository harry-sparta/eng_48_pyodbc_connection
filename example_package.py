import requests

url = 'https://www.bbc.co.uk/'

response = requests.get(url)

print(response.content)

print(response)

