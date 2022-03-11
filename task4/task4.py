if __name__ == '__main__':
	path_nums = input('Путь до файла c числами: ')
	with open(path_nums) as f:
		nums = f.readlines()
		numbers = [int(num) for num in nums]
	numbers.sort()
	median = len(numbers) // 2
	result = 0
	print(sum(abs(n - numbers[median]) for n in numbers))
