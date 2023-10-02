import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'
token = '6a2bd3ba00b74be00bad71f328d0e388'

'''def test_status_code():
    response = requests.get(f'{host}/trainers',params={'trainer_id': 2368})
    assert response.status_code == 200

def test_part_of_body():
    response = requests.put(f'{host}/trainers', headers={"trainer_token":token},
 json={
    "name": "Канзас",
    "city": "Tokyo"                                
 })
    assert response.json()["message"] == "Информация о тренере обновлена"

@pytest.mark.parametrize('key, value',[("trainer_name","Канзас"),
                                       ("id", "2368"),
                                       ("city", "Tokyo")])
def test_response_json(key, value):
    response = requests.get(f'{host}/trainers', params={'trainer_id': 2368})
    assert response.json()[key] == value'''

def test_status_code():
    response = requests.get(f'{host}/trainers')
    assert response.status_code == 200

def test_part_of_body():
    response = requests.get(f'{host}/trainers',params={'trainer_id': 2368})
    assert response.json()["trainer_name"] == "Канзас"
  
  