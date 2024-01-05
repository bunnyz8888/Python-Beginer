file_object = open ('File.txt', mode = 'r')
data = file_object.read()
file_object.seek(2)
data4 = file_object.read()
file_object.close()
file_object = open ('File.txt', mode = 'r+')
data2 = file_object.readlines()
data3 = file_object.write('\nAAAA')
print (data)
print (data2)
print (data3)
print (data4)

'''1. Nêu sự khác nhau giữa mode r+ và w+
 w+ tạo ra một file nếu file đó hiện chưa có
2. Tèo mở file dưới mode vừa đọc và ghi. 
Tèo đang  thắc mắc là vì sao sau khi ghi xong rồi, 
mà Tèo vẫn không đọc được gì cả. Hãy giải đáp giúp Tèo.
Vì khi Tèo ghi xong, con trỏ file nằm ở cuối file > Tèo không đọc được gì. 
Trường hợp đó, ta sử dụng phương thức seek.