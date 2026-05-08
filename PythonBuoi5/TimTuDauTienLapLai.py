s = input("Nhập chuỗi: ")
ds_tu = s.split()
da_thay = set()
ket_qua = "None"

for tu in ds_tu:
    if tu in da_thay:
        ket_qua = tu
        break
    da_thay.add(tu)

print(ket_qua)