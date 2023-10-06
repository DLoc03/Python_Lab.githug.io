from hinh_hoc import HinhHoc

class HinhChuNhat(HinhHoc):
    def __init__(self, canh: float, rong: float) -> None:
        super().__init__(canh)
        self.rong = rong
        
    def TinhDienTich(self):
        return self.__canh * self.rong
    
    def xuat(self):
        print(f"Chiều dài: {self.__canh}/nChiều rộng: {self.rong}")
    