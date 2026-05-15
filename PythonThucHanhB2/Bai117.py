# Nhập số nguyên dương n từ bàn phím
n_str = input("Nhập số nguyên dương n: ").strip()

S = 0
do_dai = len(n_str)

# Dùng 2 vòng lặp lồng nhau để lấy tất cả các chuỗi con liên tiếp
for i in range(do_dai):
    for j in range(i + 1, do_dai + 1):
        # Cắt chuỗi con từ vị trí i đến j
        sub_str = n_str[i:j]
        
        # Chuyển chuỗi con thành số nguyên
        sub_num = int(sub_str)
        
        # Cộng bình phương của số con vào tổng S
        S += sub_num ** 2

# In kết quả tổng S ra màn hình
print(f"Tổng bình phương của tất cả các số con là S = {S}")