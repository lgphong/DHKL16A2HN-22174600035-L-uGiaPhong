class TamGiac:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def ChuVi(self):
        return self.a + self.b + self.c
    
    def DienTich(self):
        S = (self.a+self.b+self.c) / 2
        return (S * (S - self.a) * (S - self.b) * (S - self.c))**0.5

class TamGiacCan(TamGiac):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def la_tam_giac_can(self):
        return self.a == self.b or self.a == self.c or self.b == self.c

class TamGiacVuong(TamGiacCan):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def TamGiacVuong(self):
        sides = [self.a, self.b, self.c]
        sides.sort()
        return sides[0]**2 + sides[1]**2 == sides[2]**2