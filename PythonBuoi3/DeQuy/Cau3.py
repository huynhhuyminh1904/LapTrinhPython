# 3. Viết hàm nhận 2 tham số là 2 số nguyên dương a, b. Tính a^b.
def luy_thua(a, b):
    # Điều kiện dừng: số nào mũ 0 cũng bằng 1
    if b == 0:
        return 1
    # Đệ quy: a^b = a * a^(b-1)
    return a * luy_thua(a, b - 1)

# Test
a = int(input("Nhập cơ số a: "))
b = int(input("Nhập số mũ b: "))
print(f"{a}^{b} = {luy_thua(a, b)}")
