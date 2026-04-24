# h) Hàm nhận 1 đối số là số nguyên n. Cho biết n có là số nguyên tố hay không?
is_nguyen_to = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

n = int(input("Nhập n: "))
print(f"{n} có là số nguyên tố? {is_nguyen_to(n)}")
