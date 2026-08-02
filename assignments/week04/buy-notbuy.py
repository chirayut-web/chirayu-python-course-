item = []
buy = []
current = 0

print("Enter price of 6 items:")

for i in range(6):
    user_choice = int(input(f"Item {i+1}: "))
    item.append(user_choice)

print("")

total_budget = int(input("Enter total budget: "))

print("")

for i in range(6):
    current += item[i]
    if current <= total_budget:
        print(f"Item {i+1} = {item[i]} --> buy")
        buy.append(item[i])
        print(f"Current total = {current}")
        print("")
    else:
        print(f"Item {i+1} = {item[i]} --> cannot buy")
        current -= item[i]
        print(f"Current total = {current}")
        print("")

print("Bought item: ",buy)
print("Total spent: ",current)
print("remaining budget:",total_budget - current)