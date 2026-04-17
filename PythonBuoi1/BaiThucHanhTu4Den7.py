#Bài 4:
print("\nBài 4:")
# Nhập số nguyên dương n
n_str = input("Nhập số nguyên dương n: ")

# Khởi tạo biến đếm
chan = 0
le = 0

# Duyệt qua từng chữ số trong chuỗi n_str
for chu_so in n_str:
    so = int(chu_so) # Chuyển ký tự thành số nguyên để kiểm tra
    if so % 2 == 0:
        chan += 1
    else:
        le += 1

# Xuất kết quả
print(f"Số lượng số lẻ: {le}, số lượng số chẵn: {chan}")

#Bài 5:
print("\nBài 5:")
n_str = input("Nhập số nguyên dương n: ")

tong = 0
tich = 1

for chu_so in n_str:
    so = int(chu_so)
    tong += so
    tich *= so

print(f"Tổng = {tong}, Tích = {tich}")

#Bài 6:
print("\nBài 6:")
n_str = input("Nhập số nguyên dương n: ")

# Giả sử chữ số đầu tiên là lớn nhất
max_so = int(n_str[0])

for chu_so in n_str:
    so = int(chu_so)
    if so > max_so:
        max_so = so

print(f"Số lớn nhất = {max_so}")

#Bài 7:
print("\nBài 7:")
n_str = input("Nhập số nguyên dương n: ")

la_may_man = True

for chu_so in n_str:
    if chu_so != '6' and chu_so != '8':
        la_may_man = False
        break # Chỉ cần gặp 1 số khác 6 và 8 là dừng kiểm tra ngay

if la_may_man:
    print(f"{n_str} là số may mắn.")
else:
    print(f"{n_str} KHÔNG phải số may mắn.")