"""
Task 1: Factorial Calculation using Recursion with Input Handling
"""

print("Finding the factorial of a Number")
print("------------------------")

def fact_rec(number):
    result = 1
    #Checking for a negative Integer
    if number == 1:
        return 1
    elif number < 0:
        return "Factorial is Not Defined for negative integers"
    else:
        factorial = number * fact_rec(number-1)
        return factorial

def get_integer_input():
    """
    Prompts the user for input and handles invalid entries gracefully.
    """
    try:
        # Attempts to convert user input to an integer
        return int(input("Enter a Number: "))
    except ValueError:
        # Triggered if the user enters a string, float, or invalid characters
        print("Error: Invalid input! Please enter a valid integer.")
        return None


def main():
    number = get_integer_input()
    print("------------------------")

    # Calling the Function
    factorial = fact_rec(number)
    print(f"Factorial of {number} is: {factorial}")


if __name__ == "__main__":
    main()

