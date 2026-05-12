so_gio_lam=float(input("Nhap so gio lam "))
luong_theo_gio=float(input("Nhap luong theo moi gio"))
gio_vuot_chuan=0
if so_gio_lam>44:
    gio_vuot_chuan=so_gio_lam-44
luong=44*luong_theo_gio + gio_vuot_chuan*luong_theo_gio*1.5
print("Luong thuc te: ",luong)