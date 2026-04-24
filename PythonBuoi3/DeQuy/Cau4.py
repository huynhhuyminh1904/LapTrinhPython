# 4. Viết hàm nhận 2 tham số là 2 số nguyên dương a, b. Tìm ước số chung lớn nhất (greatest common divisor - gcd) của a và b.
def uscln(a, b):
    # Thuật toán Euclid đệ quy
    if b == 0:
        return a
    return uscln(b, a % b)

# Test
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
print(f"Ước chung lớn nhất của {a} và {b} là: {uscln(a, b)}")
