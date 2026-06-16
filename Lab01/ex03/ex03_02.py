def daonguoc(lst):
    return lst[::-1]
chuoi=input("Nhap danh sach cac so, cach nhau bang dau phay: ")
numbers=list(map(int,chuoi.split(',')))
list_dao_nguoc=daonguoc(numbers)
print("List sau khi dao nguoc: ",list_dao_nguoc)