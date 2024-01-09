#Bai 1: Dùng hàm help để xem cú pháp của hàm sorted? Sau đó cho biết parameter nào là positional only? Parameter nào là keyword only?
#help(sorted)
#orted(iterable, /, *, key=None, reverse=False) => positional only là iterable, còn keyword only là key và reverse

#Bai 2: Cho một list, mỗi phần tử là một tuple gồm hoành độ (x0) và tung độ (y0), kiểm tra xem đồ thị hàm số y = f(x) có đi qua điểm đó hay không. Nếu có thì đưa sang list A, 
#trường hợp không thì đưa phần tử đó sang list B. Sau khi kết thúc, tính tổng các tung độ (y0) của hai list A và B rồi in ra trị tuyệt đối của hiệu tổng tung độ hai list đó.

lst = [(-5, -20), (-4,-15), (-3, 4), (-2, 9), (-1, 7), (0, 1), (1, -7), (2, -9), (4, 81), (5,130)]
lst_A = []
lst_B = []
def f_x (x):
	return x**3 +2*x**2 - 4*x + 1
def check_point (x ,y):
	if y == f_x(x):
		return True
	return False
def fil_point (lst_point):
	for i in lst:
		if check_point(*i):
			lst_A.append(i)
			continue
		lst_B.append(i)
	return lst_A, lst_B
def cal_sum (lst):
	s = 0
	for value in lst:
		s += value [1]
	return s
lst_A_after, lst_B_after = fil_point(lst)
print (abs(cal_sum(lst_A_after) - cal_sum(lst_B)))

#Bai 3: Cho 5 biến với giá trị mỗi biến là một số tự tự nhiên, gọi m là giá trị lớn nhất trong 5 số đó. In ra màn hình 2m -1
a, b, c, d, e = 32, 59, 8, 24, 15
def find_max (x, y):
	return int((x + y + abs(x - y))/2)
_max = find_max(find_max(find_max(find_max(a, b), c), d), e) 
print (2*_max -1)

def GTLN(*args, m = 0):
    for max_value in args:
        if max_value > m:
            m = max_value
    print(2*m - 1)
GTLN(a, b, c, d, e)