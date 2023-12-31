class ThiSinh:
    def __init__(self):
        self.ho_ten = ""
        self.diem_toan = 0
        self.diem_ly = 0
        self.diem_hoa = 0
    
    def nhap_thong_tin(self):
        self.ho_ten = input("Nhập họ tên của thí sinh: ")
        self.diem_toan = float(input("Nhập điểm môn Toán: "))
        self.diem_ly = float(input("Nhập điểm môn Lý: "))
        self.diem_hoa = float(input("Nhập điểm môn Hoá: "))
    
    def tinh_tong_diem(self):
        return self.diem_toan + self.diem_ly + self.diem_hoa

n = int(input("Nhập số lượng thí sinh: "))
danh_sach_thi_sinh = []
for i in range(n):
    thi_sinh = ThiSinh()
    thi_sinh.nhap_thong_tin()
    danh_sach_thi_sinh.append(thi_sinh)
diem_chuan = 20
thi_sinh_trung_tuyen = [ts for ts in danh_sach_thi_sinh if ts.tinh_tong_diem() >= diem_chuan]
thi_sinh_trung_tuyen.sort(key=lambda x: x.tinh_tong_diem(), reverse=True)

# In danh sách thí sinh trúng tuyển
print("Danh sách thí sinh trúng tuyển:")
for ts in thi_sinh_trung_tuyen:
    print(f"Họ tên: {ts.ho_ten}, Tổng điểm: {ts.tinh_tong_diem()}")
