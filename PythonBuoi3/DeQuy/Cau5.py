# 5. Viết hàm nhận tham số là 1 số nguyên dương (n). Tính số hạng thứ n của chuỗi Fibonaci.
def fibonacci(n):
    # Để n=1 và n=2 đều trả về 1 (khớp với dãy 1, 1, 2, 3, 5, 8, 13...)
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Test
n = int(input("Nhập n: "))
print(f"Số hạng thứ {n} là: {fibonacci(n)}")