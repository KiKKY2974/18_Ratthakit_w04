# # เปรัยบเทียบ > < == !=

# num_1 = 12
# num_2 = 23

# # print(f"{num_1 < num_2}")

# name_1 = "admin"
# name_2 = "user"

# print(f"{name_1 < name_2}")

fruits  = ["apple","banana","papaya","orange"]
find_fruit = input(str("ใส่ชื่อรายการที่ค้นหา : "))

if find_fruit in fruits:
    print(f"มี {find_fruit} อยู่ในรายการ")
else: 
    print(f"ไม่มี {find_fruit} ในรายการ")