"""
Problem: Find the maximum subarray XOR in a given array.

Description: Given an array of integers. Find the maximum XOR subarray value in given array.
Expected time complexity O(n).

Examples:
1. Input: arr[] = {1, 2, 3, 4}
   Output: 7
   The subarray {3, 4} has maximum XOR value
2. Input: arr[] = {8, 1, 2, 12, 7, 6}
   Output: 15
   The subarray {1, 2, 12} has maximum XOR value
3. Input: arr[] = {4, 6}
   Output: 6
   The subarray {6} has maximum XOR value
http://www.geeksforgeeks.org/find-the-maximum-subarray-xor-in-a-given-array/
"""

__author__ = "Pratik Shah"
__maintainer__ = __author__

def maxSubarrayXOR(input_array):
	""" Function to calculate maximum subarray XOR """

	result = 0
	for index_counter in range(len(input_array)):
		current_xor = 0
		for counter in range(index_counter, len(input_array)):
			current_xor = current_xor ^ input_array[counter]
			result = max(result, current_xor)
	print "Max subarray XOR is: %s" % result

if __name__ == '__main__':
	data_array = raw_input("Enter elements in array seperated by space: ")
	maxSubarrayXOR(map(int, data_array.split(" ")))
