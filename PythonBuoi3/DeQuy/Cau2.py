# 2. Viết hàm tính giai thừa (factorial number) của một số nguyên dương (n).
def giai_thua(n):
    # Điều kiện dừng
    if n == 0 or n == 1:
        return 1
    # Đệ quy: n! = n * (n-1)!
    return n * giai_thua(n - 1)

# Test
n = int(input("Nhập số nguyên dương n: "))
if n < 0:
    print("Vui lòng nhập số lớn hơn hoặc bằng 0")
else:
    print(f"{n}! = {giai_thua(n)}")
