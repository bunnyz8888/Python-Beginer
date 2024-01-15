'''a = {1, 2}
b = a
b.clear()
a # tại sao lại trở thành set rỗng?
set()'''

#a và b cùng trỏ vào một chỗ. Do đó thay đổi b thì a cũng sẽ bị tác động
a = {1, 2}
b = a.copy()
b.clear()
print(b) #set()
print(a) #{1, 2}
