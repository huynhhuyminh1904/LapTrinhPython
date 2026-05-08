import zlib
import os

thu_muc_hien_tai = os.path.dirname(__file__)
duong_dan_file = os.path.join(thu_muc_hien_tai, 'test.txt')

def giai_bai_tap():
    try:

        with open(duong_dan_file, 'r', encoding='utf-8') as f:
            noi_dung = f.read()
        
        du_lieu_byte = noi_dung.encode('utf-8')

        du_lieu_nen = zlib.compress(du_lieu_byte)
        file_nen = os.path.join(thu_muc_hien_tai, 'file_nen.dat')
        with open(file_nen, 'wb') as f:
            f.write(du_lieu_nen)
        print(f"Thành công! Đã tạo file nén tại: {file_nen}")

        with open(file_nen, 'rb') as f:
            du_lieu_doc_duoc = f.read()
            
        giai_nen_byte = zlib.decompress(du_lieu_doc_duoc)
        van_ban_goc = giai_nen_byte.decode('utf-8')

        print("\n--- Nội dung văn bản ban đầu ---")
        print(van_ban_goc)

    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file 'test.txt' tại {duong_dan_file}")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

giai_bai_tap()