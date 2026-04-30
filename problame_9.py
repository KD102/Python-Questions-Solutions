#  Questions : Write a Python program to calculate the square of a number entered by the user.

userinput = int(input("Enter A Number Who`s You Want To Square value : "))


def getSquareValue(value):
    return value * value


print(getSquareValue(userinput))


"""
# This Code Use With Loop

def getSquareValue(value):
    return value * value

# how many times you want to run
n = int(input("How many numbers you want to enter: "))

for i in range(n):
    userinput = int(input("Enter a number: "))
    result = getSquareValue(userinput)
    print("Square is:", result)

"""

