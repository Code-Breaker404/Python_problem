num = int(input("Enter the number: "))

# Odd/Even Check
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Grade Check
if num >= 80:
    print("A+")
elif num >= 70:
    print("A")
elif num >= 60:
    print("A-")
elif num >= 50:
    print("B")
elif num >= 40:
    print("C")
else:
    print("Fail")
