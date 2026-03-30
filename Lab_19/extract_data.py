import requests

api_url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(api_url)
import json

if response.status_code == 200:
    data = response.json()
    post_info = {"title": data['title'], "body": data['body']}
    
    # Writing data to a JSON file
    with open('post_info.json', 'w') as json_file:
        json.dump(post_info, json_file, indent=4)
    print("Data saved to post_info.json")
