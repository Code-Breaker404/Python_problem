c = input("Enter a letter: ")

vowels = "aeiouAEIOU"

if c.isalpha():  
    if c in vowels:
        print(c, "is a Vowel")
    else:
        print(c, "is a Consonant")
else:
    print("Please enter a valid letter!")
