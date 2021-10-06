average = 0
total = 0
howManyEntered = 0
howMany = int(input('how many test scores would you like to average?\n'))
while howManyEntered < howMany:
	testScore = int(input('Enter test score:\n'))
	total += testScore
	howManyEntered += 1
average = total / howMany
print('the average for the test scores youi entered is:')
print(average)
