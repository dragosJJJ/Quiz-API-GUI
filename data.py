import requests

parameters = {
    "amount": 10,
    "type": "boolean"

}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)

question_data = response.json()
question_data = question_data["results"]
response.raise_for_status()


