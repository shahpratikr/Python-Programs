"""
Problem: Check if an array can be divided into pairs whose sum is divisible by k

Description: Given an array of integers and a number k, write a function that returns true if
given array can be divided into pairs such that sum of every pair is divisible by k.

Examples:
1. Input: arr[] = {9, 7, 5, 3}, k = 6
   Output: True
   We can divide array into (9, 3) and (7, 5). Sum of both of these pairs is a multiple of 6.
2. Input: arr[] = {92, 75, 65, 48, 45, 35}, k = 10
   Output: True
   We can divide array into (92, 48), (75, 65) and (45, 35). Sum of all these pairs is a multiple
   of 10.
3. Input: arr[] = {91, 74, 66, 48}, k = 10
   Output: False
http://www.geeksforgeeks.org/check-if-an-array-can-be-divided-into-pairs-whose-sum-is-divisible-by-k/
"""

__author__ = "Pratik Shah"
__maintainer__ = __author__

from Exceptions import OddLengthException

def check_array_is_divisible(input_array, divident):
	""" Check if all pairs in array is divisible by divident or not """
	flag_list = []
	visited_list = []
	result = False
	if len(input_array) % 2 != 0:
		raise OddLengthException("ERROR: Array length is odd.")
	for index_counter in range(len(input_array)):
		for ahead_counter in range(index_counter+1, len(input_array)):
			if input_array[index_counter] not in visited_list:
				if input_array[ahead_counter] not in visited_list:
					if (input_array[index_counter]+input_array[ahead_counter]) % divident == 0:
						flag_list.append(True)
						visited_list.append(input_array[index_counter])
						visited_list.append(input_array[ahead_counter])

	if len(flag_list) > 0 and len(input_array)/2 == len(flag_list):
		for index_counter in range(len(flag_list)):
			if flag_list[index_counter]:
				result = True
	return result

if __name__ == '__main__':
	try:
		data_array = raw_input("Enter elements in array seperated by space: ")
		divide_number = int(input("Enter divide number: "))
		print "Result: %s" % check_array_is_divisible(map(int, data_array.split(" ")), divide_number)
	except ValueError:
		print "Divide number should be an Integer"
	except OddLengthException as ol:
		print ol
