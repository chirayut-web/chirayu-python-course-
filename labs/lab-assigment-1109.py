def calculate_electricity_cost(units):
    cost = 0.00

    if units > 200:
        cost += 50 * 2.50
        units -= 50

        cost += 50 * 3.00
        units -= 50

        cost += 100 * 3.50
        units -= 100

        cost += units * 4.00
        cost += 25
        print("รายละเอียดค่าไฟ:")
        print("1-50 หน่วย: 125 บาท")
        print("51-100 หน่วย: 150 บาท")
        print("101-200 หน่วย: 300 บาท")
        print(f"201-{units} หน่วย: {units * 4.00} บาท")
        print("ค่าบริการ: 25.00 บาท")
        print(f"รวมค่าไฟ {cost}")
        units -= units

    elif units > 100 and units <= 200:
        cost += 50 * 2.50
        units -= 50

        cost += 50 * 3.00
        units -= 50

        cost += units * 3.50
        cost += 25
        print("รายละเอียดค่าไฟ:")
        print("1-50 หน่วย: 125 บาท")
        print("51-100 หน่วย: 150 บาท")
        print(f"101-{units} หน่วย: {units * 3.50} บาท")
        print("ค่าบริการ: 25.00 บาท")
        print(f"รวมค่าไฟ {cost}")
        units -= units

    elif units > 50 and units <= 100:
        cost += 50 * 2.50
        units -= 50

        cost += units * 3.00
        cost += 25
        print("รายละเอียดค่าไฟ:")
        print("1-50 หน่วย: 125 บาท")
        print(f"51-{units} หน่วย: {units * 3.00} บาท")
        print("ค่าบริการ: 25.00 บาท")
        print(f"รวมค่าไฟ {cost}")
        units -= units

    elif units > 0 and units <= 50:
        cost += units * 2.50
        cost += 25
        print("รายละเอียดค่าไฟ:")
        print(f"1-{units} หน่วย: {units * 2.50} บาท")
        print("ค่าบริการ: 25.00 บาท")
        print(f"รวมค่าไฟ {cost}")
        units -= units

    return cost



while True:
    print("===== โปรแกรมคำณวนค่าไฟ =====")
    print("1. คำณวนค่าไฟ")
    print("2. ออกจากเมนู")
    user_choice = int(input("เลือกเมนู: "))
    if user_choice == 1:
        units = int(input("กรอกจำนวนค่าไฟ: "))
        if units < 0:
            print("จำนวนหน่วยไฟฟ้าต้องไม่ติดลบ")
            continue

        cost = calculate_electricity_cost(units)

    elif user_choice == 2:
        break
    else:
        print("เลือกเมนูไม่ถูกต้อง")