data_dict = [
	{"Name": "Alice", "Age":28, "City": "New York"},
	{"Name": "Bob", "Age": 34, "City": "Chicago"},
	{"Name": "Charlie", "Age": 22, "City": "San Francisco"}
]


import csv

# Open a file in write mode
with open('people.csv', 'w', newline='') as file:
    # Specify the fieldnames (columns)
    fieldnames = ["Name", "Age", "City"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    # Write the header
    writer.writeheader()
    
    # Write data rows
    for row in data_dict:
        writer.writerow(row)
