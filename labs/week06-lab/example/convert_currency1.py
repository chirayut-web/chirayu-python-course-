#เขียนฟังก์ชั่นที่สามารถแปลงสกุลเงินจาก THB <--> USD : 1 USD = 32 THB, THB <--> JPY: 100 JYP = 22  THB 
# 4 ฟังก์ชั่น โดยใช้ชื่อและการใช้งาน functtion convert_currency(100, USD) bath to USD

#เช็คว่าจะแปลงเป็นค่าเงินอะไร
#เช็คว่าเงินที่ได้ติดลบไหม
#รับค่าและแปลง
#test again

def convert_currency(type, value):

    usb = 33.19
    jpy = 4.80
    thb = 0.21
    
    if type == "THB to USD":
        return f"{value/usb:.2f}"

    if type == "USD to THB":
        return f"{value*usb:.2f}"

    if type == "THB to JPY":
        return f"{value*jpy:.2f}"

    if type == "JPY to THB":
        return f"{value*thb:.2f}"

TU = "THB to USD"
UT = "USD to THB"
TJ = "THB to JPY"
JT = "JPY to THB"

print(convert_currency(TU, 120))
print(convert_currency(UT, 120))    
print(convert_currency(TJ, 120))
print(convert_currency(JT, 120))