while True:
	steps = 1
	number = int(input('Enter a number > 1.'))
	
	while number != 1:
		if number % 2 == 0:
			number /= 2
		else:
			number *= 3
			number += 1
		steps+=1
	print(steps)

	try:
		choice = input('Would you like to enter a new number? (y/n): ')
	except:
		print('Please enter a number.')

	if choice == 'y':
		continue
	else:
		break