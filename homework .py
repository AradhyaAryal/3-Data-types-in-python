# Get input from the user
user_input = input("Enter a number: ")

# Convert the input to a float (to handle decimal numbers)
try:
    number = float(user_input)

    # Use conditional statements to check the number's value
    if number > 0:
        print(f"The number {number} is positive.")
    elif number < 0:
        print(f"The number {number} is negative.")
    else:
        print(f"The number {number} is zero.")

except ValueError:
    print("Invalid input. Please enter a valid number.")