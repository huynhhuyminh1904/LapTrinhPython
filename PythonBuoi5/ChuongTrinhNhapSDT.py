s = input("Nhập số điện thoại: ")
tat_ca = {str(i) for i in range(10)}

con_thieu = sorted(list(tat_ca - set(s)))

print(f"Các ký số không xuất hiện: {con_thieu}")