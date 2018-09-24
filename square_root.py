# Implement squareroot function

import unittest

def square_root(num):
	start = 0
	end = num

	square = 0
	mid = -1

	while abs(square - num) > 0.001:
		
		mid = (start+end)/2

		square = mid ** 2

		if square == num:
			return mid
		elif square < num:
			start = mid
		else:
			end = mid

	return mid


data = 234
print(square_root(data))