for number in range(1,6):
	print(number)

fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    print(fruit)

item_count = 0
for fruit in fruits:
    item_count += 1
    print(fruit)

print(f"Total number of items processed: {item_count}")
