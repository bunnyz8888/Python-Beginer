'''with open('printtext.txt', 'w') as f:
     print('printed by print function', file=f)

with open('printtext.txt') as f:
     f.read()
from time import sleep'''

'''# print trong Python 2.X
print('Kteam')
# và nhận được kết quả giống như Python 3.X
print('Kteam')
#Nhưng bản chất là khác nhau
# print trong Python 2.X
print('Kteam')
# tương đương với Python 3.X là
print(('Kteam'))'''

your_name = "Henry"
your_great = "Hello! My name is "

for c in your_great + your_name:
    print(c, end='', flush=True)
    sleep(0.1)
print()
