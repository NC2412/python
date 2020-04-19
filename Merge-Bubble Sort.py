def main():
	sort_list = input('Enter a list, separated by commas(,), to be sorted.\n')
	sort_list = sort_list.split(',')
	sorted_list = []

	for i in range(len(sort_list)):
		sort_list[i] = int(sort_list[i])
	
	choice = input('Merge or bubble sort?: ')
	if choice[0].lower() == 'm':
		sorted_list = merge_sort(sort_list)
	else:
		sorted_list = bubble(sort_list)

	printList(sorted_list)

'''
	MERGE SORTING
'''
def merge_sort(list):
	# Base case for merge_sort. Checks if the length of list is less than two, so it doesnt call merge()
	if len(list) < 2:
		return list

	mid = len(list)//2
	left = list[:mid]
	right = list[mid:]

	left = merge_sort(left)
	right = merge_sort(right)

	return merge(left, right)


def merge(left, right):
	# i is for the left list
	# j is for the right list
	i = j = 0


	temp_list = []

	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			temp_list.append(left[i])
			i+=1
		else:
			temp_list.append(right[j])
			j+=1

	try:
		temp_list.extend(left[i:])
	except:
		pass
	try:
		temp_list.extend(right[j:])
	except:
		pass

	return temp_list

'''
	BUBBLE SORTING
'''
def bubble(list):
	for i in range(len(list)):
		for x in range(len(list)-1):
			if list[x] > list[x+1]:
				temp = list[x+1]
				list[x+1] = list[x]
				list[x] = temp
	return list

def printList(list):
	for x in list:
		print(x)


if __name__ == '__main__':
	main()