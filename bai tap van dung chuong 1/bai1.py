class HinhChuNhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def nhap_du_lieu(self):
        self.chieu_dai = float(input("Nhập chiều dài của hình chữ nhật: "))
        self.chieu_rong = float(input("Nhập chiều rộng của hình chữ nhật: "))

    def tinh_chu_vi(self):
        chu_vi = 2 * (self.chieu_dai + self.chieu_rong)
        return chu_vi

    def tinh_dien_tich(self):
        dien_tich = self.chieu_dai * self.chieu_rong
        return dien_tich

    def in_thong_tin(self):
        print(f"Độ dài hai cạnh của hình chữ nhật: {self.chieu_dai}, {self.chieu_rong}")
        print(f"Chu vi của hình chữ nhật: {self.tinh_chu_vi()}")
        print(f"Diện tích của hình chữ nhật: {self.tinh_dien_tich()}")

hinh_chu_nhat = HinhChuNhat(0, 0)  
hinh_chu_nhat.nhap_du_lieu()  
hinh_chu_nhat.in_thong_tin()  
