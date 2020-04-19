import random
'''
	MONKEY SORT
'''
def monkey_sort():
	data = open('Monkey Sort Data.txt', 'w+')

	for rep in range(2, 10):
		list = []
		ideal_list = []

		for i in range(rep):
			list.append(i)
			ideal_list.append(i)

		random.shuffle(list)
		tries = 0
		Sorting = True

		printList(ideal_list)
		while Sorting:
			

			if list == ideal_list:
				print('Correct list')
				Sorting = False
			else:
				random.shuffle(list)
				tries += 1 
				
		data.write(str(rep) + '\t' + 'Tries: ' + str(tries) + '\n')

def printList(list):
	temp = ''
	for x in list:
		temp += str(x) + ','
	print(temp)


if __name__ == '__main__':
	monkey_sort()