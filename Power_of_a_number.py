collect = int(input("Enter a number: "))
exponent = 1
for exponent in range(21):
	power = collect ** exponent
	print(collect, "^", exponent, "=" ,power)
	exponent += 1