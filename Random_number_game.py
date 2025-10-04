import random

for x in range(1,6):
    gessNumber=int(input("Enter your guess number 1 to 6 :"))
    randomNumber=random.randint(1,6)
    if gessNumber== randomNumber :
        print("You have Won")
    else:
        print("You have lose")

    print("Random Number is :",randomNumber)    
