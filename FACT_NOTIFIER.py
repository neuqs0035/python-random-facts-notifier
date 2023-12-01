from requests import get
from time import sleep
from plyer import notification

url = "https://numbersapi.p.rapidapi.com/6/21/date"

querystring = {"fragment": "true", "json": "true"}

headers = {
    "X-RapidAPI-Key": "6f1b7fb970msh81d2c2a9ae83d69p17d60djsn2a51191e0314",
    "X-RapidAPI-Host": "numbersapi.p.rapidapi.com"
}

while True:
    response = get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        data = response.json()
        notification.notify(
            message=data['text'],
            app_name = "Facts",
            timeout=10
        )
    sleep(7200)
