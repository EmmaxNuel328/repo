number = 1
sum = 0
for _ in  range(1,100):
	sum = sum + number
	average = float(sum/number)
	number += 1
print(sum)
print(average)