# รับ text จากผู้ใช้
# รับอักขละจากผู้ใช้
# แสดงผลำนวนของอักขระในข้อความ text 

while True:
    name = input("Insert your name : ")

    if name.replace(" ", "").isalpha():
        break
    else:
        print("Please enter letter only")
     
while True:
    target_letter = input("insert your character : ")
    if target_letter.isalpha():
        if len(target_letter) == 1:
            break
        else:
            print("Please enter single character only")
    else:
        print("Please enter letter only")

count = 0
name = name.lower()
target_letter = target_letter.lower()

for current_letter in name:
    if target_letter == current_letter:
        count += 1

print(f"{count} letter {target_letter} found in {name}")