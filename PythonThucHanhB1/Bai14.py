def giai_toan_thoi_tien():
    menh_gia = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    
    try:
        a = int(input("Nhap so tien hang (a): "))
        b = int(input("Nhap so tien khach tra (b): "))
        
        if a > b:
            print(f"So tien khach hang con thieu la: {a - b}")
        elif a == b:
            print("Cam on khach hang. Hen gap lai")
        else:
            X = b - a
            print(f"\nSo tien {X} duoc doi thanh:")
            
            tong_so_to = 0
            so_loai_tien = 0
            
            for m in menh_gia:
                so_to = X // m
                X = X % m
                
                if so_to > 0:
                    print(f"Loai {m} gom {so_to} to")
                    tong_so_to += so_to
                    so_loai_tien += 1
            
            print(f"TONG CONG CO {tong_so_to} TO")
            print(f"Tong so loai = {so_loai_tien}")
            
            input("\nNhan Enter de ket thuc...")
            print("Cam on khach hang. Hen gap lai")

    except ValueError:
        print("Vui long nhap so nguyen hop le!")

giai_toan_thoi_tien()