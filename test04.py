# ---------------- List = ทำได้ทุกอย่าง ----------------
#            0    1    2      3     4           5
my_list1 = [ 10 , 20 , True , 10 , "SAU" , [ 20 , "IoT" ]]
#            6    5     4     3     2           1   คือ ติดลบ ( - )

print (my_list1[4])
print (my_list1[-2])
print (my_list1[5])
print (my_list1[-1])
print (my_list1[5][1])
print (my_list1[-1][-1])

# call slicing => List
print (my_list1[1:4]) # 20 , True , 10
print (my_list1[3:]) # 10 , 'SAU' , [ 20 , "IoT"]
print (my_list1[:3]) # 10 , 20 , True

# เข้าถึงทุกข้อมูล
for info in my_list1 :
    print (info, end=",")

print ( )

print (my_list1)
my_list1[4] = "Thailand"
print (my_list1)

# list Method
my_list2 = [ 10 , 20 , True , 10 , "SAU" , [ 20 , "IoT" ]]
my_list2.append("wow")
print (my_list2)
my_list2.append([111,222,333]) #เพิ่มห้อง
print (my_list2)
my_list2.extend([444,555]) #ไม่เพิ่มห้อง
print (my_list2)
my_list2.remove(10) #ลบตัวที่เจอตัวแรก
my_list2.remove("SAU")
my_list2.remove([111,222,333])
print (my_list2)
my_list2.pop()
my_list2.pop()
my_list2.pop()
print (my_list2)
my_list2.pop(2) # 2 is index = 10
print (my_list2)

# list function => len() , min() , max()
list3 = [ 10 , 20 , 10 , 30 , True ]
print (len(list3))
print (min(list3))
print (max(list3))

# Tuple 