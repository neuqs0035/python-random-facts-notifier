# Importing necessary libraries
from requests import get
from time import sleep
from plyer import notification

# API endpoint and query parameters
url = "https://numbersapi.p.rapidapi.com/6/21/date"
querystring = {"fragment": "true", "json": "true"}

# Headers for making the API request
headers = {
    "X-RapidAPI-Key": "6f1b7fb970msh81d2c2a9ae83d69p17d60djsn2a51191e0314",
    "X-RapidAPI-Host": "numbersapi.p.rapidapi.com"
}

# Infinite loop to keep fetching and displaying facts
while True:
    # Making a GET request to the Numbers API
    response = get(url, headers=headers, params=querystring)

    # Checking if the request was successful (status code 200)
    if response.status_code == 200:
        # Parsing the JSON response
        data = response.json()

        # Displaying a desktop notification with the retrieved fact
        notification.notify(
            message=data['text'],
            app_name="Facts",  # Setting the app name for the notification
            timeout=10  # Setting the notification timeout in seconds
        )

    # Sleeping for 2 hours (7200 seconds) before making the next request
    sleep(7200)
