"""
Problem: Reorder a array according to given indexes.

Description: Given two integer arrays of same size, 'arr[]' and 'index[]', reorder elements in
'arr[]' according to given index array. It is not allowed to given array arr's length.

Example:
1. Input:  arr[]   = [10, 11, 12];
           index[] = [1, 0, 2];
   Output: arr[]   = [11, 10, 12]
           index[] = [0,  1,  2] 
2. Input:  arr[]   = [50, 40, 70, 60, 90]
           index[] = [3,  0,  4,  1,  2]
   Output: arr[]   = [40, 60, 90, 50, 70]
           index[] = [0,  1,  2,  3,   4] 
"""

from Exceptions import ArrayLengthNotSameException

def reorder_array(index_array, data_array):
	""" Reorder data array according to index_array """
	if len(index_array) != len(data_array):
		raise ArrayLengthNotSameException("ERROR: Length of index array and data array is not same.")
	for start_counter in range(len(index_array)):
		for ahead_counter in range(len(index_array)):
			if index_array[start_counter] < index_array[ahead_counter]:
				temp_data = index_array[start_counter]
				index_array[start_counter] = index_array[ahead_counter]
				index_array[ahead_counter] = temp_data

				temp_data = data_array[start_counter]
				data_array[start_counter] = data_array[ahead_counter]
				data_array[ahead_counter] = temp_data
	print "data_array: %s" % data_array
	print "index_array: %s" % index_array

if __name__ == '__main__':
	try:
		input_index_array = raw_input("Enter elements in index array seperated by space: ")
		input_data_array = raw_input("Enter elements in data array seperated by space: ")
		reorder_array(map(int, input_index_array.split(" ")), map(int, input_data_array.split(" ")))
	except ArrayLengthNotSameException as alns:
		print alns
