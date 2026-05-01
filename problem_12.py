# Qutions : Write a program to detect double space in a string.

a = ["Helllo World", "Kenil  Dhanani", "Where  Are You  From"]
b = 0
for i in a:
    if i.__contains__("  "):
        b += 1

print(b)
