user_data = {
	"name": "John Doe",
	"email": "john.doe@example.com",
	"age": 30
}

import requests
url = "https://httpbin.org/post"
response =requests.post(url, json=user_data)

if response.status_code == 200:
    print("Request was successful!")
else:
    print(f"Request failed with status code: {response.status_code}")

# Parse the JSON response
response_data = response.json()

# Output the entire response data for inspection
print("Response Data:", response_data)

# Example: Print specific part of the response
print("Extracted Data:", response_data['json'])
