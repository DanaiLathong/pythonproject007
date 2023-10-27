# ---------------- Tuple ----------------
#            0    1    2      3     4           5
my_tuple = [ 10 , 20 , True , 10 , "SAU" , [ 20 , "IoT" ]]
#            6    5     4     3     2           1   คือ ติดลบ ( - )
print (my_tuple[4])
print (my_tuple[-2])
print (my_tuple[5])
print (my_tuple[-1])
print (my_tuple[5][1])
print (my_tuple[-1][-1])

# call slicing => List
print (my_tuple[1:4]) # 20 , True , 10
print (my_tuple[3:]) # 10 , 'SAU' , [ 20 , "IoT"]
print (my_tuple[:3]) # 10 , 20 , True

# เข้าถึงทึกข้อมูล
for info in my_tuple :
    print (info, end=",")

# ถ้าจะแก้ข้อมูลใน Tuple
my_list = list(my_tuple)
my_list[4] = "IoT"
my_tuple = tuple(my_list)
print (my_tuple)

# Tuple Method
print (my_tuple.count(10)) # 2
print (my_tuple.index(True))

# list function => len() , min() , max()
my_tuple3 = [ 10 , 20 , 10 , 30 , True ]
print (len(my_tuple3))
print (min(my_tuple3))
print (max(my_tuple3))