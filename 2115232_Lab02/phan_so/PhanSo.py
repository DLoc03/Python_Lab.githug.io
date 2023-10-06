import HamXuLyPhanSo as xlps

class PhanSo:
    def __init__(self, tuso = 1, mauso = 1) -> None:
        self.tu = tuso
        if mauso == 0:
            raise Exception("Mẫu số không được bằng 0")
        else:
            self.mau = mauso

    def RutGon(self):
        kq = xlps.TimUCLN(abs(self.tu), abs(self.mau))
        self.tu = self.tu // kq
        self.mau = self.mau // kq     

    def __str__(self) -> str:
        self.RutGon()
        return f"{self.tu}/{self.mau}"
        
    def __add__(self, other):
        ps = PhanSo()
        
        ps.tu = self.tu * other.mau + other.tu * self.mau
        ps.mau = self.mau*other.mau
        return ps

    def __sub__(self, other):
        ps = PhanSo()
        
        ps.tu = self.tu * other.mau - other.tu * self.mau
        ps.mau = self.mau*other.mau
        return ps

    def __mul__(self, other):
        ps = PhanSo()
        
        ps.tu = self.tu * other.tu
        ps.mau = self.mau*other.mau
        return ps

    def __truediv__(self, other):
        ps = PhanSo()
        
        ps.tu = self.tu * other.mau
        ps.mau = self.mau * other.tu
        return ps


        






        
# tu = int(input("Mời nhập tử số: "))
# mau = int(input("Mời nhập mẫu số: "))
# ps = PhanSo(tu, mau)
# print("Phân số thứ nhất: ", end = "")
# print(ps)
# tu2 = int(input("Mời nhập tử số thứ hai: "))
# mau2 = int(input("Mời nhập mẫu số thứ hai: "))
# ps2 = PhanSo(tu2, mau2)
# print("Phân số thứ hai: ", end = "")
# print(ps2)

# print("Kết quả phép cộng: ", end = "")
# ps.Add(ps2)
# print(ps)

# print("Kết quả phép trừ: ", end = "")
# ps.Sub(ps2)
# print(ps)

# print("Kết quả phép nhân: ", end = "")
# ps.Mul(ps2)
# print(ps)

# print("Kết quả phép chia: ", end = "")
# ps.TrueDiv(ps2)
# print(ps)
