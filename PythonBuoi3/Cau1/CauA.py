# a) Hàm nhận 1 đối số là số nguyên n và trả về trị tuyệt đối của n
tri_tuyet_doi = lambda n: abs(n)

n = int(input("Nhập n: "))
print(f"Trị tuyệt đối của {n} là: {tri_tuyet_doi(n)}")