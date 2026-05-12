def truy_cap_phan_tu(data):
    first=data[0]
    last=data[-1]
    return first, last
input_tuple=eval(input("Nhap tuple: "))
first, last=truy_cap_phan_tu(input_tuple)
print("Phan tu dau: ",first)
print("Phan tu cuoi: ",last)