import requests

token = "6a2bd3ba00b74be00bad71f328d0e388"
host = 'https://api.pokemonbattle.me:9104'

response = requests.post('https://api.pokemonbattle.me:9104/trainers/reg', json = {
    "trainer_token": token,
    "email": "34522german@dolnikov.ru",
    "password": "Iloveqa34451"
}, headers = {"Content-Type" : "application/json"})

print(response.text)

response_activation = requests.post('https://api.pokemonbattle.me:9104/trainers/confirm_email', 
                                               json = {
     "trainer_token": token
 }, headers = {"Content-Type" : "application/json"})
print(response_activation.status_code)

if response_activation.status_code == 200:
    print('ok!')
else:
    print('not ok!')  
  
response = requests.post(f'{host}/pokemons', json = {
    "name": "generate",
    "photo": "generate"
}, headers = {"Content-Type" : "application/json","trainer_token" : token})

print(response.text)

response = requests.put(f'{host}/pokemons', json = {
    "pokemon_id": "11692",
    "name": "Klaus",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}, headers = {"Content-Type" : "application/json","trainer_token" : token})

print(response.text)

response = requests.post(f'{host}/trainers/add_pokeball', json = {
    "pokemon_id": "11692"
}, headers = {"Content-Type" : "application/json","trainer_token" : token})

print(response.text)