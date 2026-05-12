def tongchan(lst):
    tong=0
    for i in lst:
        if i%2==0:
            tong+=i
    return tong
listnumber=input("Nhap danh sach cac so, cach nhau bang dau phay")
numbers=list(map(int,listnumber.split(',')))
tong_chan=tongchan(numbers)
print("Tong cac so chan la: ",tong_chan)