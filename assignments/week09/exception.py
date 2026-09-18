try:
    num1 = int(input("ตัวเลขที่ 1 :"))
    num2 = int(input("ตัวเลขที่ 2 :"))
    opreation = input("เครื่องหมาย (+, -, *, /): ")


    if opreation == "+":
        results = (num1 + num2)
    elif opreation == "-":
        results = (num1 - num2)
    elif opreation == "*":
        results = (num1 * num2)
    elif opreation == "/":
        results = (num1 / num2)
    else:
        raise ValueError("เครื่องหมายต้องเป็น (+, -, *, /) เท่านั้น")

    print(f"{num1} {opreation} {num2} = {results}")

    if opreation not in ["+", "-", "*", "/"]:
        raise ValueError("ตัวดำเนินการไม่ถูกต้อง")

except ValueError:
    print(f"ข้อมูลต้องเป็นตัวเลขเท่านั้น")

except ZeroDivisionError:
    print(f"ไม่สามารถหารด้วยศูนย์ได้")

except Exception:
    print(f"ข้อมูลต้องเป็นตัวเลขเท่านั้น")

else:
    print("คำนวณข้อมูลเรียบร้อย")

finally:
    print("จบการทำงาน")


 

