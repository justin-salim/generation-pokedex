import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon/charmander/") 
print(response.status_code)