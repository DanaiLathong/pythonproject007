#character in string
       # 01234567890123
infoA = "Hello SAU 2023"
       # 43210987654321 คือ ติดลบ(-)
print (infoA[6])
print (infoA[-8])
#เข้าถถึงตัวอักษรหลายๆตัวใน string ใช้วิธี slicing ด้วย index number

#SAU
print (infoA[6:9])
print (infoA[-8:-5])

#o SAU 20
print (infoA[4:12])

#string Method
print (infoA.upper()) #ตัวพิมพ์ใหญ่
print (infoA.lower()) #ตัวพิมพ์เล็ก
print (infoA.capitalize()) #
print (infoA.count("l")) #นับจำนวนตัวอักษรหรือจำนวน
print (infoA.isdigit()) #นับว่ามีตัวเลขไหม
print (infoA.islower()) #นับว่ามีตัวพิมพ์เล็กกี่ตัว
infoB = infoA.replace("SAU","IoT")
print (infoB)
print (infoB.replace("Hello","Hi..."))

#String string
print (len(infoA))
print ("SAU",35,end="")
print ("SAU"+str(35))
print ("SAU",35,sep="")
print ("20","02","2023",sep="/")
print ("20","01","2023",sep="-")