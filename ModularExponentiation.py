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

if __name__ == '__main__':
	try:
		first_value = int(input("Enter first number: "))
		second_value = int(input("Enter second number: "))
		power_value = int(input("Enter power value: "))
	except ValueError:
		print "Input should be in integers"
	