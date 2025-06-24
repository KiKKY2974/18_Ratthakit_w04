numbers = [12,15,63,21,24,30,18,36,42,48,54,60,72,84,90]
divisor = 6

print(f"ตัวที่หาร {divisor} ลงตัว : ")
found = 0
for i in numbers:
    if i % divisor == 0:
        print(f"{i} หาร {divisor} ตัวที่หารลงตัวคือ(={i // divisor})")
        found += 1
        
        if found == 3:
            break  # หยุดลูปเมื่อเจอ 3 ตัวที่หารลงตัวแล้ว