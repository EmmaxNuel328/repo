numbers = input("Enter a number: ")
my_list = []
count = 0
for number in numbers:
	my_list.append(number)
	if my_list[count] % '2' == 0:
		print(my_list[count],end = " ")
	count += 1