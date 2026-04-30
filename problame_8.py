# Questions : Write a Python program to find an average of two numbers entered by the user.

a = int(input("Enter the first Number : "))
b = int(input("Enter the second Number : "))


def _averageTwoNumber(value1, value2):
    return (value1 + value2) / 2


print("Average Of Number A And B :", _averageTwoNumber(a, b))