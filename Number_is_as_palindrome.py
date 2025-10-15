collect = input("Enter numbers not less than 1: ")
my_list = []
index = 0
for numbers in collect:
	my_list.append(numbers)
	if(my_list[0] == my_list[-1] ):
		#if(my_list[1] == my_list[-2]):
			print(my_list[1])#"it is a palindrome")
	index += 1