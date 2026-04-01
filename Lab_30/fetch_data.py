import requests
response = requests.get('https://jsonplaceholder.typicode.com/posts')

if response.status_code == 200:
	data = response.json()
	print(f"Fetched {len(data)} records")
else:
	print("Failed to fetch data")
processed_data = [{"userId": post["userId"], "title": post["title"]} for post in data]
user_posts = [post for post in processed_data if post["userId"] == 1]
print(f"User 1 has {len(user_posts)} posts")


import csv

with open('user_posts.csv', 'w', newline='') as csvfile:
    fieldnames = ["userId", "title"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for post in user_posts:
        writer.writerow(post)
import logging

logging.basicConfig(filename='app.log', level=logging.INFO)

try:
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    response.raise_for_status()
    logging.info("Data fetched successfully")
except requests.exceptions.RequestException as e:
    logging.error(f"Error fetching data: {e}")
    exit(1)

import argparse

parser = argparse.ArgumentParser(description='Fetch and process API data')
parser.add_argument('--user_id', type=int, default=1, help='User ID to filter posts by')

args = parser.parse_args()

user_posts = [post for post in processed_data if post["userId"] == args.user_id]
