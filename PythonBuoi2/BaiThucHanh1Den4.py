from datetime import datetime, date, timedelta

# i. In thông tin hiện tại
now = datetime.now()
print(f"Năm hiện tại: {now.year}")
print(f"Tháng hiện tại bằng chữ: {now.strftime('%B')}")
print(f"Tuần thứ mấy trong năm: {now.strftime('%U')}")
print(f"Tuần thứ mấy trong tháng: {(now.day - 1) // 7 + 1}")
print(f"Ngày thứ mấy trong năm: {now.strftime('%j')}")
print(f"Ngày dương lịch hiện tại: {now.day}")
print(f"Thứ của ngày hiện tại: {now.strftime('%A')}")
print(f"Giờ phút giây hiện tại: {now.strftime('%H:%M:%S')}")

# ii. Tính số ngày cách nhau giữa 2 ngày (nhập từ bàn phím)
d1_str = input("Nhập ngày 1 (dd/mm/yyyy): ")
d2_str = input("Nhập ngày 2 (dd/mm/yyyy): ")
d1 = datetime.strptime(d1_str, "%d/%m/%Y").date()
d2 = datetime.strptime(d2_str, "%d/%m/%Y").date()
print(f"Số ngày cách nhau: {abs((d2 - d1).days)}")

# iii. Chuyển chuỗi S dạng 'Sep 18 2019 2:43PM' sang kiểu ngày
s = input("Nhập chuỗi ngày (định dạng 'Month dd yyyy H:MPM'): ")
obj_date = datetime.strptime(s, "%b %d %Y %I:%M%p")
print(f"Kết quả chuyển đổi: {obj_date}")

# iv. Sử dụng timedelta thêm 5 giây vào thời gian hiện tại
thoi_gian_moi = now + timedelta(seconds=5)
print(f"Thời gian hiện tại: {now.strftime('%H:%M:%S')}")
print(f"Thời gian sau 5 giây: {thoi_gian_moi.strftime('%H:%M:%S')}")