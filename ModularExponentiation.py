"""
Problem: Modular Exponentiation (Power in Modular Arithmetic).

Description: Given three numbers x, y and p, compute (xy) % p.

Examples:
1. Input:  x = 2, y = 3, p = 5
   Output: 3
   Explanation: 2^3 % 5 = 8 % 5 = 3.
2. Input:  x = 2, y = 5, p = 13
   Output: 6
   Explanation: 2^5 % 13 = 32 % 13 = 6.

http://www.geeksforgeeks.org/modular-exponentiation-power-in-modular-arithmetic/
"""

__author__ = "Pratik Shah"
__maintainer__ = __author__

import math

def compute_minimum_mod(first_value, second_value, mod_value):
	""" Compute minimum mod value """
	power_value = int(math.pow(first_value, second_value))
	return power_value % mod_value

if __name__ == '__main__':
	try:
		input_first_value = int(input("Enter first number: "))
		input_second_value = int(input("Enter second number: "))
		input_mod_value = int(input("Enter mod value: "))
		output_mod_value = compute_minimum_mod(input_first_value, input_second_value, input_mod_value)
		print "Minimum mod value: %s" % output_mod_value
	except ValueError:
		print "Input should be in integers"
	