#Bài tập rút gọn 
# phần định dạng
'''row_1 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')
row_2 = '| {:<6} | {:^15} | {:>10} |'.format('ID', 'Ho va ten', 'Noi sinh')
row_3 = '| {:<6} | {:^15} | {:>10} |'.format('123', 'Kteam', 'TP HCM')
row_4 = '| {:<6} | {:^15} | {:>10} |'.format('6969', 'Kquiz', 'Da Lat')
row_5 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')

# phần xuất kết quả
print(row_1)
print(row_2)
print(row_3)
print(row_4)
print(row_5)'''

print('+ {:-<6} + {:-^15} + {:->10} +\n'.format('', '', '') + 
	'| {:<6} | {:^15} | {:>11} |\n'.format('ID', 'Ho va ten', 'Noi sinh') + 
	'| {:<6} | {:^15} | {:>10} |\n'.format('123', 'Yui Hatano', 'Japanese') + 
	'| {:<6} | {:^15} | {:>10} |\n'.format('6969', 'Sunny Leone', 'Canada') + 
	'+ {:-<6} + {:-^15} + {:->10} +'.format('', '', ''))