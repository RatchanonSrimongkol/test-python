def calculate_no_return(a, b):
    a + b  # คำนวณเสร็จ แต่ไม่ส่งอะไรกลับ

def calculate_with_return(a, b):
    return a + b  # คำนวณแล้วส่งกลับ

x = calculate_no_return(3, 5)
y = calculate_with_return(3, 5)

print(x)  # None  <- ว่างเปล่า ไม่มีอะไรให้ใช้
print(y)  # 8     <- ได้ค่าจริงมาใช้ต่อได้