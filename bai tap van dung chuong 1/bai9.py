class DaGiac:
    def __init__(self, so_canh):
        self.so_canh = so_canh
        self.canh = [0] * so_canh

    def nhap_canh(self):
        self.canh = [float(input(f"Nhập độ dài cạnh {i + 1}: ")) for i in range(self.so_canh)]

    def tinh_chu_vi(self):
        return sum(self.canh)

class HinhBinhHanh(DaGiac):
    def __init__(self):
        super().__init__(4)

    def tinh_dien_tich(self):
        return self.canh[0] * self.canh[1]

class HinhChuNhat(HinhBinhHanh):
    def __init__(self):
        super().__init__()

class HinhVuong(HinhChuNhat):
    def __init__(self):
        super().__init__()

hinh_vuong = HinhVuong()
hinh_vuong.nhap_canh()
chu_vi = hinh_vuong.tinh_chu_vi()
dien_tich = hinh_vuong.tinh_dien_tich()

print(f"Chu vi của hình vuông là: {chu_vi}")
print(f"Diện tích của hình vuông là: {dien_tich}")
