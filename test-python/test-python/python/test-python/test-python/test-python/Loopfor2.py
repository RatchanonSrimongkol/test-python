Lob = int(input('ใส่จำนวนชื่อที่ต้องการกรอก '))

Krangname = []

for i in range(Lob):
    Lobs = i + 1
    newname = input (f'คนที่ {Lobs} ชื่อว่า')
    jj = ('hello  '+ newname)  
    Krangname.append(jj)
    print(Krangname)