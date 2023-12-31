class PhanSo:
    def _init_(self,TuSo,MauSo):
        self.TuSo=TuSo
        self.MauSo=MauSo
    
    def NhapSo(self):
        self.TuSo=int(input("Nhap vao tu so : "))
        self.MauSo=int(input("Nhap vao mau so : "))
    def TinhHopLe(self):
           while self.MauSo <= 0:
            print("Mau so khong the bang 0 vui long nhap lai mau so : ")
            self.MauSo=int(input("Nhap vao mau so : "))   
    def InPhanSo(self):
           print(f"{self.TuSo}/{self.MauSo}")
        
kiemtra=PhanSo()
kiemtra.NhapSo()
kiemtra.TinhHopLe()
print("Phan so hop le")
print("Phan so ban vua nhap la:")
kiemtra.InPhanSo()