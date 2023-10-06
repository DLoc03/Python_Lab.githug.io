from PhanSo import PhanSo

class DanhSachPhanSo():
    def __init__(self) -> None:
        self.dsps = []

    def ThemPhanSo(self, ps: PhanSo):
        self.dsps.append(ps)
    
    def xuat(self):
        for ps in self.dsps:
            print(ps, end = " ")
    
    def DemPSAmTrongDS(self):
        count = 0
        for i in range(0, len(self.dsps)):
            if self.dsps[i].tu / self.dsps[i].mau < 0:
                count += 1
        return count
    def PhanSoDuongNhoNhat(self):
        min = 0
        psmin = self.dsps[0]
        for i in range(0, len(self.dsps)):
            if (self.dsps[i].tu > 0 and self.dsps[i].mau > 0) and (self.dsps[i].tu/self.dsps[i].mau) < min:
                psmin = self.dsps[i]
        return psmin

    def TimViTriPhanSo_x(self, ps: PhanSo):
        lstvt = []
        for i in range(0, len(self.dsps)):
            if self.dsps[i].tu == ps.tu and self.dsps[i].mau == ps.mau:
                lstvt.append(i)
        print(f"Các vị trí của phân số {ps} trong danh sách: ", end = "")
        for vt in lstvt:
            print(vt+1, end = " ")

    def TongCacPhanSoAm(self):
        kq = PhanSo(0, 1)
        for i in range(0, len(self.dsps)):
            if (self.dsps[i].tu < 0 and self.dsps[i].mau < 0):
                kq = kq + self.dsps[i]
        return kq

    def XoaPhanSo_x(self, ps: PhanSo):
        for i in range(0, len(self.dsps)-1):
            if self.dsps[i].tu == ps.tu and self.dsps[i].mau == ps.mau:
                self.dsps.pop(i)

        return self.dsps
    
    def XoaPhanSoCoTu_x(self, tu):
        for i in range(0, len(self.dsps)-1):
            if self.dsps[i].tu == tu:
                self.dsps.pop(i)
        return self.dsps
    
    def SapXepDSPSTang_Tu(self):
        for i in range(0, len(self.dsps)-1):
            if self.dsps[i].tu > self.dsps[i+1].tu:
                tmp = self.dsps[i]
                self.dsps[i] = self.dsps[i+1]
                self.dsps[i+1] = tmp
        return self.dsps

            


dsps = DanhSachPhanSo()   
ps1 = PhanSo(1, 3)
ps2 = PhanSo(4, 7)
ps3 = PhanSo(-3, 2)
ps4 = PhanSo()
ps5 =  PhanSo(0, 1)
ps4.tu = -6
ps4.mau = 3
dsps.ThemPhanSo(ps1)
dsps.ThemPhanSo(ps2)
dsps.ThemPhanSo(ps3)
dsps.ThemPhanSo(ps4)
dsps.ThemPhanSo(ps5)
dsps.xuat()
kq = dsps.DemPSAmTrongDS()
print(f"\nSố phân số âm trong danh sách là: {kq}")
print(f"{ps1} - {ps2} = {ps1-ps2}")
print(f"{ps3} + {ps5} = {ps1-ps5}")
psmin = dsps.PhanSoDuongNhoNhat()
print(f"Phân số dương nhỏ nhất: {psmin}")
dsps.TimViTriPhanSo_x(ps4)
kqpsAm = dsps.TongCacPhanSoAm()
print(f"\nTổng các phân số âm: {kqpsAm}")
# dsps.XoaPhanSo_x(ps2)
# print(f"Danh sách sau khi xóa phân số {ps2}: ", end = "")
# dsps.xuat()

# dsps.XoaPhanSoCoTu_x(1)
# print(f"\nDanh sách sau khi xóa phân số có tử = 1: ", end = "")
# dsps.xuat()
dsps.SapXepDSPSTang_Tu()
dsps.xuat()