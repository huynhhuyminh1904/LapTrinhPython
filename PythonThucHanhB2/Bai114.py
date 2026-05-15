import math

# Nhập 2 số nguyên a, b từ bàn phím
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

danh_sach_than_thien = []

# Duyệt qua các số trong khoảng từ a đến b
for num in range(a, b + 1):
    # Tìm số đảo ngược bằng cách đảo chuỗi ký tự
    dao_nguoc = int(str(num)[::-1])
    
    # Nếu ước chung lớn nhất của num và dao_nguoc bằng 1
    if math.gcd(num, dao_nguoc) == 1:
        danh_sach_than_thien.append(num)

# In các số thân thiện tìm được
print("Các số thân thiện trong khoảng là:")
print(*danh_sach_than_thien)

# In số lượng số thân thiện
print(f"Số lượng số thân thiện đã in ra: {len(danh_sach_than_thien)}")