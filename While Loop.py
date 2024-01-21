#Bai 1
five_even_numbers = []
k_number = 1
while len(five_even_numbers) < 5: # vòng lặp vô hạn vì giá trị này là hằng nên ta không thể tác động được
    if k_number % 2 == 0: # nếu k_number là một số chẵn
        five_even_numbers.append(k_number) # thêm giá trị của k_number vào list
    k_number += 1
print(five_even_numbers)
print(k_number)

#Bai 2
'''data = an so dfn Kteam odsa in fasfna Kteam mlfjier
as dfasod nf ofn asdfer fsan dfoans ldnfad Kteam asdfna
asdofn sdf pzcvqp Kteam dfaojf kteam dfna Kteam dfaodf
afdna Kteam adfoasdf ncxvo aern Kteam dfad
idx = 0
length = len(data)
new_content = ''

while idx < length:
	line_list = data[idx].split()
	idline = 0
	length_line = len(line_list)
	while idline < length_line:
		if line_list[idline] == 'Kteam':
			line_list[idline-1] = 'How'
		idline+=1
	new_content += ''.join(line_list) + '\n'
	idx +=1
print(data)'''

#Bai 3
lst = [56, 14, 11, 756, 34, 90, 11, 11, 65, 0, 11, 35]
k = 0
lst1 = []
lst2 = []
while k < len(lst):
    if lst[k] != 11:
        lst1.append(lst[k])
    else:
        lst2.append(k)
    k+=1
lst1.sort()
i=0
while i < len(lst2):
	lst1.insert(lst2[i],'11')
	i+=1
print(lst1)


