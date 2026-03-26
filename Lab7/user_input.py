user_input = ''
try:
    while True:
        user_input = input("Enter a string (type 'exit' to quit): ")
        if user_input == "exit":
            print("Exiting the loop. Goodbye!")
            break
        print("You entered:", user_input)
finally:
    print("Program terminated successfully.")
