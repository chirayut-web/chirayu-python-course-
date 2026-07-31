# take real name from user
# count all of the vowels in text (a, e, i, o, u)

# example
# what is your name? : Boonchoo
# output: Your text

letter = input("what is your name:")
vowels = ('a','e','i','o','u','A','E','I','O','U')

i = 0

for character in letter:
    if character in vowels:
        i += 1
        
print(f"Your name have {i} vowels")


