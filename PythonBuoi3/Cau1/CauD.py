# d) Hàm nhận 1 đối số là số nguyên n. Cho biết n có là bội số của 13 hoặc 19 hay không?
is_boi_so = lambda n: n % 13 == 0 or n % 19 == 0

n = int(input("Nhập n: "))
print(f"{n} có là bội của 13 hoặc 19? {is_boi_so(n)}")
