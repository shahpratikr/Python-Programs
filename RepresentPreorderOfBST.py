"""
Problem: Check if a given array can represent Preorder Traversal of Binary Search Tree.

Description: Given an array of numbers, return true if given array can represent preorder traversal
of a Binary Search Tree, else return false. Expected time complexity is O(n).

Examples:
1. Input:  pre[] = {2, 4, 3}
   Output: true
   Given array can represent preorder traversal of below tree
2. Input:  pre[] = {2, 4, 1}
   Output: false
   Given array cannot represent preorder traversal of a Binary Search Tree.
3. Input:  pre[] = {40, 30, 35, 80, 100}
   Output: true
   Given array can represent preorder traversal of below tree
4. Input:  pre[] = {40, 30, 35, 20, 80, 100}
   Output: false
   Given array cannot represent preorder traversal of a Binary Search Tree.
http://www.geeksforgeeks.org/check-if-a-given-array-can-represent-preorder-traversal-of-binary-search-tree/
"""

__author__ = "Pratik Shah"
__maintainer__ = __author__

def check_representation(data_array):
	""" Check if input_array can represent preorder traversal of BST """
	stack_array = []
	root_value = 0
	for index in range(len(data_array)):
		if data_array[index] < root_value:
			return False
		while len(stack_array) > 0 and stack_array[len(stack_array)-1] < data_array[index]:
			root_value = data_array[len(stack_array)-1]
			stack_array.pop()
		stack_array.append(data_array[index])
	return True

if __name__ == '__main__':
	try:
		input_array = raw_input("Enter elements in array: ")
		status = check_representation(map(int, input_array.split(" ")))
		print status
	except Exception:
		pass
