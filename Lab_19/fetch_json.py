import requests

api_url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(api_url)

if response.status_code == 200:
    # Parsing JSON data
    data = response.json()
    print("Fetched Data as Dictionary:")
    print(data)
else:
    print("Failed to retrieve data. Status code:", response.status_code)
