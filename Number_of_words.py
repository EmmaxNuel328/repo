collect = "I am Naruto Uzumaki and i want to be the greatest Hokage"
my_list = []
index = -1
add = 0
plus = 0
for words in collect:	
	index += 1
	my_list.append(words)
	longest = my_list[0]
	count = index
	if my_list[index] != " ":
		my_list[index] = my_list[index] + "0"
	if len(my_list[index]) >  len(" "):
		add += 1
	if len(my_list[index])> len(longest):
		longest = add
		
	print(my_list[index],add,longest)