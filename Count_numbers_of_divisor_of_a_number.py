collect = int(input("Enter a number: "))
divisor = 1

for count in range(collect):
	if collect % divisor == 0:
		print(divisor)
	divisor += 1
	
	count += 1
print(count)