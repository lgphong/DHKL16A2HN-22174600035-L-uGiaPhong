class Date:
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        print(f"{self.day}/{self.month}/{self.year}")

    def next(self):
        pass

class NhanVien:
    def __init__(self, ten, ngaysinh, ngayvaocongty):
        self.ten = ten
        self.ngaysinh = ngaysinh
        self.ngayvaocongty = ngayvaocongty

    def display_info(self):
        print(f"Tên nhân viên: {self.ten}")
        print("Ngày sinh:")
        self.ngaysinh.display()
        print("Ngày vào công ty:")
        self.ngayvaocongty.display()

ngaysinh = Date(15, 5, 1990)  
ngayvaocongty = Date(10, 10, 2015)  
employee1 = NhanVien("Nguyen Van A", ngaysinh, ngayvaocongty)
employee1.display_info()
