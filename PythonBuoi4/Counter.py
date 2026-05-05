from collections import Counter

# Nhập 2 chuỗi S1 và S2
s1 = input("Nhập chuỗi S1: ")
s2 = input("Nhập chuỗi S2: ")

# Câu a
# Sử dụng Counter để tìm ký tự xuất hiện trong cả 2 chuỗi
c1 = Counter(s1)
c2 = Counter(s2)
giao = c1 & c2 # Phép toán & lấy phần giao của 2 Counter
res_a = list(giao.elements()) 
# elements() trả về các ký tự kèm số lần xuất hiện chung
print(f"a) Những ký tự xuất hiện trong cả 2 chuỗi: {''.join(sorted(set(res_a)))}")

# Câu b và c
# Cách làm: Chuyển chuỗi thành dict để dò tìm theo gợi ý
dict1 = {char: True for char in s1}
dict2 = {char: True for char in s2}

# Tìm ký tự có trong S1 nhưng không có trong S2
chi_co_s1 = [char for char in s1 if char not in dict2]
# Tìm ký tự có trong S2 nhưng không có trong S1
chi_co_s2 = [char for char in s2 if char not in dict1]

# Loại bỏ ký tự trùng lặp để in ra và đếm
set_s1_only = sorted(set(chi_co_s1))
set_s2_only = sorted(set(chi_co_s2))

# Kết quả câu b
tong_so_ky_tu = len(set_s1_only) + len(set_s2_only)
print(f"b) Số lượng ký tự khác biệt giữa 2 chuỗi: {tong_so_ky_tu}")

# Kết quả câu c
print(f"c) Các ký tự chỉ có ở S1: {''.join(set_s1_only)}")
print(f"   Các ký tự chỉ có ở S2: {''.join(set_s2_only)}")