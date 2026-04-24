# c) Hàm nhận 2 đối số là số nguyên (x, y), trả về tích của x và y
tich = lambda x, y: x * y

x = int(input("Nhập x: "))
y = int(input("Nhập y: "))
print(f"Tích của {x} và {y} là: {tich(x, y)}")
