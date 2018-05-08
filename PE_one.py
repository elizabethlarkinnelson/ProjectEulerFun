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

#3. Largest Prime Factor

import math

def largest_prime(n):

	# The below code works, it is not time efficient
	# prime = 1

	# for n in range(2, num + 1):
	# 	for i in range (2, n):
	# 		if n % i == 0:
	# 			break
	# 		else:
	# 			if i > prime:
	# 				prime = n
	# return prime

	#NEED TO COME BACK TO THISE ONE***************************
	return


#4. Largest Palindrome Product

def largest_palindrome():
	'''
	This function returns the largest possible palindrome number from two, three digit products
	'''

	return
