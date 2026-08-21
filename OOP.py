class SieuNhan:
    def __init__(self, mau, vukhi, sucmanh, phongthu):
        self.mau_sac = mau
        self.vu_khi = vukhi
        self.suc_manh = sucmanh
        self.phong_thu = phongthu
    def xin_chao(self):
        print("Ta la sieu nhan",self.mau_sac,"ta co suc manh", self.suc_manh)

sieu_nhan_A = SieuNhan("Đo", "Kiem",95, 80)
sieu_nhan_B = SieuNhan("Xanh", "Cung ten", 98 , 72)

sieu_nhan_A.xin_chao()
sieu_nhan_B.xin_chao()
print(sieu_nhan_A.phong_thu)
print(sieu_nhan_B.phong_thu)
