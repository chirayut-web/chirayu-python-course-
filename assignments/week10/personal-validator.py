"""
Create a Personal Information Validator program that:
    Asks user for their name, age, and phone number FN
    Validates that name contains only alphabetic characters and spaces FN
    Converts age from string to integer and validates it's between 18-65 FN
    Validates phone number contains exactly 10 digits FN
    
    Uses appropriate string methods for validation
    Displays formatted output with proper string formatting
    
    USE: isalpha(), isdigit(), .upper(), string formatting with % or .format()
    
Example Result

=== PERSONAL INFORMATION VALIDATOR ===
Enter your name: John Doe
Enter your age: 25
Enter your phone number: 9876543210

Validation Results:
Name: Valid (contains only letters and spaces)
Age: Valid (25 years old)
Phone: Valid (10-digit number)

Formatted Information:
Name: JOHN DOE
Age Group: Young Adult (18-30)
Phone: +91-9876543210

"""

print("=== PERSONAL INFORMATION VALIDATOR ===")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
phone_number = input("Enter your phone number: ")

for letter in name:
    if letter.isalpha() or letter.isspace():
        check_name = True
    else:
        check_name = False

if 18 <= age <= 65:
    check_age = True
else:
    check_age = False

if len(phone_number) == 10:
    check_number = True
else:
    check_number = False
print("")        
print("Validation Results:")
if check_name == True:
    print("Name: Valid (contains only letters and spaces)")
else:
    print("Name: InValid")

if check_age == True:
    print(f"Age: Valid ({age} years old)")
else:
    print("Age: InValid")

if check_number == True:
    print("Phone: Valid (10-digit number)")
else:
    print("Phone: InValid")
print("")
print("Formatted Information:")
print(f"Name: {name.upper()}")
if 18 <= age <= 30:
    print(f"Age Group: Young Adult (18-30)")
elif 31 <= age <= 60:
    print(f"Age Group: Adult (31-60)")
else:
    print("Age Group: Senior")
print(f"Phone: +91-{phone_number}")
