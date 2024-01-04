#Bài 1: Tại sao thay đổi  dict2 mà dict1 lại cũng bị thay đổi theo? Giải pháp khắc phục
'''>>> dict1 = {'key': 6969}
>>> dict1
{'key': 6969}
>>> dict2 = dict1
>>> dict2
{'key': 6969}
>>> dict2['key'] = 'changed'
>>> dict2
{'key': 'changed'}
>>> dict1
{'key': 'changed'}'''
#Vì hai dict trỏ cùng vào một nơi
dict1 = {'key': 6969}
print (dict1) #{'key': 6969}
dict2 = dict1.copy()
print (dict2) #{'key': 6969}
dict2['key'] = 'changed'
print (dict2) #{'key': 'changed'}
print (dict1) #{'key': 'changed'}

#Bài 2: Nêu sự khác nhau giữa
'''d = {}
d.update({'a': 3})''' #Hoạt động bình 

'''d = {}
d.update(3)''' #Lỗi vì phải là 1 cặp key value



