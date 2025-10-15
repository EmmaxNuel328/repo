collect = input("Enter anything: ")
count = 0
for characters in collect:
	count += 1
	print(characters,  end = " ")
	print(ord(characters))