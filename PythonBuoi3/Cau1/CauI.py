# i) Hàm nhận 3 tham số là số nguyên (a, b, c). Cho biết a, b, c có là 3 cạnh hợp lệ của 1 tam giác hay không? Nếu là 3 cạnh hợp lệ của tam giác, cho biết đó là tam giác gì? (thường, cân, đều, vuông, ...).
def loai_tam_giac(a, b, c):
    check_hop_le = lambda a, b, c: a + b > c and a + c > b and b + c > a
    
    if not check_hop_le(a, b, c):
        return "Không phải là tam giác hợp lệ"
    
    # Logic phân loại
    if a == b == c: return "Tam giác đều"
    
    sides = sorted([a, b, c])
    is_vuong = lambda s: round(s[0]**2 + s[1]**2, 5) == round(s[2]**2, 5)
    
    if a == b or b == c or a == c:
        return "Tam giác vuông cân" if is_vuong(sides) else "Tam giác cân"
    if is_vuong(sides):
        return "Tam giác vuông"
    
    return "Tam giác thường"

a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
print(f"Kết quả: {loai_tam_giac(a, b, c)}")
