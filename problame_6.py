# Questions: Write a Python program to find the remainder when a number is divided by z.

a = int(input("Enter A Number : "))
b = int(input("Enter B Number Division : "))


def getRemainderTwoNumbers(a, b):
    return a % b


print("The Number [A] Divide By Number [B] Get Remainder was :",getRemainderTwoNumbers(a, b))
