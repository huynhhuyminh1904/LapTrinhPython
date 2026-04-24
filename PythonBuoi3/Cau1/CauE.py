# e) Hàm nhận 1 đối số là số thực r là bán kính của hình tròn. Cho biết diện tích hình tròn.
import math
dien_tich_tron = lambda r: math.pi * r**2

r = float(input("Nhập bán kính r: "))
print(f"Diện tích hình tròn là: {dien_tich_tron(r):.2f}")
