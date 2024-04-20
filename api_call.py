import swisseph as swe
import requests
import json

# URL to which the request will be sent
url = 'http://127.0.0.1:5000/natal_chart'

# Data to be sent in JSON format
data = {
    'date': '05/02/93',
    'time': '03:30',
    'location': 'Barcelona, España'
}
# Convert data dictionary to JSON
json_data = json.dumps(data)
# Headers you might want to send along with the request
headers = {
    'Content-Type': 'application/json',  # This header informs the server about the type of the content
    'Custom-Header': 'value'             # Example of a custom header
}
# Making the POST request
response = requests.post(url, data=json_data, headers=headers, )
# Printing the response from the server
print(response.text)

