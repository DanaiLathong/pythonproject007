# primitive data type
# number , boolean , string

# non - primitive data type / collection / data structure ชนิดข้อมูล
# list , tuple , set , dictionnary

# data type จะเอามาใช้การเขียนโปรแกรมในเครื่องมือ ตัวแปร พารามิเตอร์ ฟังก์ชั่น 

# ---------------- List = ทำได้ทุกอย่าง ----------------
#            0    1    2      3     4           5
my_list1 = [ 10 , 20 , True , 10 , "SAU" , [ 20 , "IoT" ]]
#            6    5     4     3     2           1   คือ ติดลบ ( - )

# ---------------- Tuple = แก้ไขไม่ได้ ----------------
#             0    1    2      3     4           5
my_tuple1 = ( 10 , 20 , True , 10 , "SAU" , ( 20 , "IoT" ))
#             6    5     4     3     2           1   คือ ติดลบ ( - )

# ---------------- Set = ซ้ำกันไม่ได้ ถ้าเท่ากับตัวเดียวกัน ไม่มีลำดับ แก้ไม่ได้ ----------------
my_set1 = { 10 , 20 , True , 10 , "SAU" , ( 20 , "IoT" )}

# ---------------- *** Dictionnary = ที่เป็น Key:value แก้ไขได้ ไม่มีindexกำกับ ซ้ำได้  ----------------
# key = string / number (int) , value = all type
#                 key:value     key:value  key:value   key:value    key:value
my_diction1 = { "name":"mod" , "age":"30" , 555:999 , "fla":True , "wow":[10,20,30]}