#Nhập từ bàn phím 3 số, in ra số lớn nhất
k1 = int(input('Nhap so thu nhat\n=> '))
k2 = int(input('Nhap so thu hai\n=> '))
k3 = int(input('Nhap so thu ba\n=> '))

if k1 > k2 and k1 > k3:
    print('so lon nhat la', k1)
elif k2 > k1 and k2 > k3:
    print('so lon nhat la', k2)
else:
    print('so lon nhat la', k3)
