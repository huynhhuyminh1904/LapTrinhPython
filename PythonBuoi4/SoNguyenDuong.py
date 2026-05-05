import math

# Hàm kiểm tra số nguyên tố (phục vụ câu a)
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# --- NHẬP DỮ LIỆU ---
numbers = []
while True:
    try:
        val = int(input("Nhập một số nguyên: "))
        numbers.append(val)
    except ValueError:
        print("Vui lòng nhập số nguyên hợp lệ!")
        continue
    
    choice = input("Bạn có muốn nhập nữa không? (Y/N): ").strip().upper()
    if choice == 'N':
        break

print("-" * 30)
print(f"Danh sách đã nhập: {numbers}")

# a) In các số nguyên tố
primes = [x for x in numbers if la_so_nguyen_to(x)]
print(f"a) Các số nguyên tố trong list: {primes}")

# b) Tính trung bình cộng số âm và số dương
ds_am = [x for x in numbers if x < 0]
ds_duong = [x for x in numbers if x > 0]

tbc_am = sum(ds_am) / len(ds_am) if ds_am else "Không có số âm"
tbc_duong = sum(ds_duong) / len(ds_duong) if ds_duong else "Không có số dương"

print(f"b) Trung bình cộng số âm: {tbc_am}")
print(f"   Trung bình cộng số dương: {tbc_duong}")

# c) Số lớn nhất, số nhỏ nhất
if numbers:
    print(f"c) Số lớn nhất: {max(numbers)}, Số nhỏ nhất: {min(numbers)}")
else:
    print("c) Danh sách trống.")

# d) Kiểm tra sắp xếp tăng dần
is_sorted = all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-1))
if is_sorted:
    print("d) Danh sách ĐÃ được sắp xếp tăng dần.")
else:
    print("d) Danh sách CHƯA được sắp xếp tăng dần.")
