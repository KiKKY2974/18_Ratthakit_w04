# remove ลบค่าที่ต้องการ
# pop ไม่ใส่ค่า ตัวสุดท้ายจะหาย last in first out
# delete ลบ
colors = ["Red","Green","Blue","Yellow"]
colors_2 = ["Red","Green","Blue","Yellow"]
colors.remove("Red") # ลบตามที่พิมพ์

colors.pop(2) # ลบตามลำดับ

del colors[1] # ลบหายตามลำดับ

colors_2.clear() #ลบออกทั้งหมด

print(colors)