import math

class HinhHoc:
    def __init__(self, canh: float) -> None:
        self.__canh = canh
        
    def __hinhhoc__(self, cd: float):
        return cd
    
    def __tinhdientich__(self, cd: float):
        return self.__canh * cd
    
    def xuat(self):
        print (f"{self.__canh}")