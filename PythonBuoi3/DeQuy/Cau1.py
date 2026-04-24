# 1. Cho nhập số nguyên n. Tính tổng các chữ số có trong n.
def tong_chu_so(n):
    # Đưa về số dương để tính toán
    n = abs(n)
    # Điều kiện dừng: nếu n còn 1 chữ số
    if n < 10:
        return n
    # Đệ quy: lấy chữ số cuối + tổng các chữ số còn lại
    return (n % 10) + tong_chu_so(n // 10)

# Test
n = int(input("Nhập số nguyên n: "))
print(f"Tổng các chữ số của {n} là: {tong_chu_so(n)}")
