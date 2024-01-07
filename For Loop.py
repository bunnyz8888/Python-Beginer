#Bai 1:
'''iter_ = (x for x in range(3))
for value in iter_:
     print(non_exist_variable)

Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: name 'non_exist_variable' is not defined

 next(iter_) # kết quả là gì? Kết quả là 1. Chính xác là giá trị thứ hai của biến iter_'''

#Bai 2: Sử dụng vòng lặp để tính tổng các số trong set sau đây
set_ = {5, 8, 1, 9, 4}
length = len(set_)
k = 0
for value in set_:
	k += value
print('Tong day so la', k)


#Bai 3: Sử dụng sequence scan để thay đổi phần tử đầu tiên của mỗi phần tử trong List dưới đây thành None
lst = [[1, 2, 3], [4, 5, 6]]
for i in lst:
  i[0] = 'None'
print(lst)

#Bai 4: 
n = int(input('Enter size of matrix: '))
dx, dy = 1,0
x, y = 0,0
spiral_matrix = [[None] * n for j in range(n)]

for i in range(n ** 2):
    spiral_matrix[x][y] = i
    nx, ny = x + dx, y + dy
    if 0 <= nx < n and 0 <= ny < n and spiral_matrix[nx][ny] == None:
        x, y = nx, ny
    else:
        dx, dy = -dy, dx
        x, y = x + dx, y + dy

for y in range(n):
    for x in range(n):
        print("%02i" % spiral_matrix[x][y], end=' ')
    print()

print()
