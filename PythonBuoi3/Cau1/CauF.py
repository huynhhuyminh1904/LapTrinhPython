# f) Hàm nhận 2 đối số là số thực d, r là chiều dài và chiều rộng của hình chữ nhật. Cho biết chu vi hình chữ nhật.
chu_vi_hcn = lambda d, r: (d + r) * 2

d = float(input("Nhập chiều dài: "))
r = float(input("Nhập chiều rộng: "))
print(f"Chu vi hình chữ nhật là: {chu_vi_hcn(d, r)}")
