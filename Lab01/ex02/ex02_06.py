x = int(input("Nhap x: "))
y = int(input("Nhap y: "))

ketqua = [[0 for j in range(y)] for i in range(x)]
for i in range(x):
    for j in range(y):
        ketqua[i][j] = i * j

print("Ket qua: ", ketqua)

