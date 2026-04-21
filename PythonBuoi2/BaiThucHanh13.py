import re

# Nhập chuỗi (dùng vòng lặp để nhập nhiều dòng cho đến khi nhập 'END')
print("Nhập văn bản (nhập 'END' ở dòng cuối để kết thúc):")
lines = []
while True:
    line = input()
    if line.upper() == 'END': break
    lines.append(line)

# Xử lý từng dòng
ket_qua = []
for line in lines:
    # 1. Xóa khoảng trắng đầu và cuối dòng (Quy tắc 1 & 4)
    line = line.strip()
    
    if line:
        # 2. Giữa các từ chỉ cách nhau 1 khoảng trắng (Quy tắc 2)
        line = re.sub(r'\s+', ' ', line)
        
        # 3. Dấu chấm, phẩy phải đi liền với từ trước nó (Quy tắc 3)
        line = re.sub(r'\s+([,.])', r'\1', line)
        
        ket_qua.append(line)

# In chuỗi hoàn chỉnh
print("\n--- Chuỗi hoàn chỉnh ---")
print("\n".join(ket_qua))