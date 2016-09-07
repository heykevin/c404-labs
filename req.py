import requests

response = requests.get('https://raw.githubusercontent.com/heykevin/c404-labs/master/req.py');

print response.text