fruit_tuple = ("apple", "banana", "cherry", "elderberry", "fig")

try:
	fruit_tuple[0] = "avocado"
except TypeError as e:
	print("Error:", e)
