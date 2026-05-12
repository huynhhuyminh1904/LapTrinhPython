def giai_toan_doi_tien():
    menh_gia = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    
    try:
        X = int(input("Nhap so tien X: "))
        X_ban_dau = X
        tong_so_to = 0
        ket_qua = []

        for m in menh_gia:
            so_to = X // m
            X = X % m
            tong_so_to += so_to
            ket_qua.append((m, so_to))

        # In kết quả theo định dạng
        print(f"\nSo tien {X_ban_dau} duoc doi thanh:")
        for m, so_to in ket_qua:
            print(f"Loai {m} gom {so_to} to")
        
        print(f"TONG CONG CO {tong_so_to} TO")

    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ!")

giai_toan_doi_tien()