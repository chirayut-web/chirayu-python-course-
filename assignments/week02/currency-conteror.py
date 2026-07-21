print("Please Choose you conversion direction ")
print("THB to USD")
print("USD to THB")

User_Choice = input("Enter THB to USD or USD to THB:")

if User_Choice == "THB to USD":
    thb = float(input("Enter the amount in THB :"))
    usd = thb / 35.5

    print(f"Formula: {thb:.2f} THB / 35.5")
    print(f"Result: {usd:.2f} USD")

elif User_Choice == "USD to THB":
    usd = float(input("Enter the amount in USD :"))
    thb = usd * 35.5

    print(f"Formula: {usd:.2f} USD × 35.5")
    print(f"Result: {thb:.2f} THB")

else:
    print("Invalid choice. Please enter THB to USD or USD to THB")

