# 1. Multiples of 3 and 5

def find_sum(num):

	total = 0

	for i in range(num):

		if i % 3 == 0 or i % 5 == 0:

			total += i

	return total

# 2. Even Fibonacci Numbers

def fibo_even(num):

	total_even = 0

	first = 0
	second = 1
	total = 0

	while total < num:

		if total % 2 == 0:
			total_even += total
			print(total_even)

		total = first + second
		first = second
		second = total
	
