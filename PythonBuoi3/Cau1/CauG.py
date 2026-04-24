# g) Hàm nhận 1 đối số là số nguyên n. Cho biết n có là số chính phương hay không? (số chính phương là số có căn bậc hai là 1 số nguyên như: 4, 9, 16, ...).
import math
is_chinh_phuong = lambda n: n >= 0 and math.isqrt(n)**2 == n

n = int(input("Nhập n: "))
print(f"{n} có là số chính phương? {is_chinh_phuong(n)}")
