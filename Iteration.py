a = [x for x in range(3)]
b = (x for x in range(3))
print (a)
print (b)
print (next(b))
print (next(b))
print (next(b))
#print (b[0]) -> lỗi
c = (x for x in range(8))
print (c)
print (sum(c))
#print (next(c)) -> lỗi. sum rồi ko next đc

print (max(8,89,234,5))
print (min(8,89,234,5))
d = [8,89,234,5]
print (sorted(d))
print (sorted(d, reverse = True))