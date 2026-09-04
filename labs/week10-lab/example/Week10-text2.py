print("Welcome to Password Security Testing!")

isdigit = False
isalpha = False
emoji = False
password = input("Insert your password : ")

for current_letter in password:
    if current_letter.isdigit():
        isdigit = True
    if current_letter.isalpha():
        isalpha = True
    if current_letter == '@':
        emoji = True

if len(password) > 8 and isdigit and isalpha and emoji == True:
    print("Your Password is strong")
else:
    print("Your Password is weak")

