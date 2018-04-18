# 1. Multiples of 3 and 5

def find_sum(num):

	total = 0

	for i in range(num):

		if i % 3 == 0 or i % 5 == 0:

			total += i

	return total

print(find_sum(1000))

# 2. Even Fibonacci Numbers