import requests
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')


if response.status_code == 200:
	print("Requests was successful!")
else:
	print(f"Request failed with status code: {response.status_code}")
data = response.json()
print(f"Title: {data['title']}")
print(f"Body: {data['body']}")
