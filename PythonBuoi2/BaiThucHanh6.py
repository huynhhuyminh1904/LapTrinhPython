# 1. Nhập chuỗi S (có thể chứa nhiều dòng)
print("Nhập chuỗi S:")
s = input()

# 2. Nhập từ cần tìm (word)
word = input("Nhập từ cần đếm: ")

# 3. Tách chuỗi thành danh sách các từ
words_list = s.split()

# 4. Loại bỏ các dấu câu cơ bản dính vào từ (như , . ! ?) để đếm chính xác hơn
clean_words = [w.strip(",.!?;:") for w in words_list]

# 5. Đếm số lần xuất hiện chính xác từ word
count = clean_words.count(word)

# 6. In kết quả
print(f"số từ {word} là {count}")
