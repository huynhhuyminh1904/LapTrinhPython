#Bài 1:
print("Bài 1:")
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b (b > a): "))

for i in range(a, b + 1):
    if i % 3 == 0:
        continue  # Bỏ qua các số chia hết cho 3
    print(i, end=" ")
print() # Xuống dòng

#Bài 2:
print("\nBài 2:")
n = int(input("Nhập số nguyên n: "))

f1, f2 = 0, 1
while f1 <= n:
    print(f1, end=" ")
    # Tính số tiếp theo bằng tổng 2 số trước
    f1, f2 = f2, f1 + f2
print()

#Bài 3:
print("\nBài 3:")
n = int(input("Nhập số nguyên dương n (n >= 11): "))

for i in range(11, n + 1):
    s = str(i)
    # Kiểm tra nếu tất cả ký tự trong chuỗi đều giống ký tự đầu tiên
    if s == s[0] * len(s):
        print(i, end=" ")
print()
