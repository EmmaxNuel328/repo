collect = int(input("Enter a number: "))
divisor = 1
for _ in range (collect):
	if collect % divisor == 0:
		print(divisor)
	divisor += 1