# Finding Factorial using Function

print("Finding the factorial of a Number")
print("------------------------")

def factorial(number):
    result = 1
    #Checking for a negative Integer
    if number < 0:
        return "Factorial is Not Defined for negative integers"
    #Calculating Factorial
    for i in range(1, number+1):
        result *= i
    return result
num = int(input("Enter a Number: "))
print("------------------------")
#Calling the Function
fact = factorial(num)
print(f"Factorial of {num} is: {fact}")