score = []

for i in range(5):
    user_choice = int(input(f"Enter score of student {i+1}: "))
    score.append(user_choice)

print("")

for i in range(5):
    if score[i] >= 50:
        print(f"student {i + 1}: {score[i]} --> ผ่าน")
    else:
        print(f"student {i + 1}: {score[i]} --> ไม่ผ่าน")

