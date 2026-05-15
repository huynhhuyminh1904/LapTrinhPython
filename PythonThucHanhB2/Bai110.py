import sys

def main():
    print("=== CHƯƠNG TRÌNH KHÔI PHỤC CHUỖI GỐC (PLAIN TEXT) ===")
    print("Nhập 'exit' hoặc 'q' để thoát chương trình.\n")
    
    while True:
        # 1. Nhập chuỗi mã hóa từ bàn phím
        cipher = input("Nhập chuỗi mã hóa (cipher text): ").strip()
        
        if cipher.lower() in ['exit', 'q', '']:
            print("Đã thoát chương trình.")
            break
            
        plain = ""
        i = 0
        n = len(cipher)
        loi_cu_phap = False
        
        # 2. Xử lý giải nén chuỗi
        while i < n:
            if cipher[i] == "#":
                if i + 2 < n:
                    try:
                        count = int(cipher[i + 1])
                        char = cipher[i + 2]
                        
                        plain += char * count
                        i += 3
                    except ValueError:
                        print("Lỗi: Ký tự ngay sau '#' phải là một chữ số từ 1-9!")
                        loi_cu_phap = True
                        break
                else:
                    print("Lỗi: Chuỗi kết thúc thiếu thông tin sau dấu '#'!")
                    loi_cu_phap = True
                    break
            else:
                # Ký tự bình thường, giữ nguyên
                plain += cipher[i]
                i += 1
                
        # 3. In kết quả ra màn hình nếu không có lỗi cấu pháp
        if not loi_cu_phap:
            print(f"=> Kết quả plain text : {plain}")
        print("-" * 40)

if __name__ == "__main__":
    main()