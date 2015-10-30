"""
Problem: Minimum number of bracket reversals needed to make an expression balanced.

Description: Given an expression with only '}' and '{'. The expression may not be balanced. 
Find minimum number of bracket reversals to make the expression balanced.

Examples:
1. Input:  exp = "}{"
   Output: 2
   Description: We need to change '}' to '{' and '{' to '}' so that the expression becomes
   balanced, the balanced expression is '{}'

2. Input:  exp = "{{{"
   Output: Can't be made balanced using reversals

Algorithm:
1. Check length of expression is odd or even. If odd raise exception.
2. Convert string_expression to list
"""

__author__ = "Pratik Shah"
__maintainer__ = __author__

from Exceptions import OddLengthStringException

def count_reversals_required_to_balance_string(input_string):
	""" Count number of reversals required to balance given expression """
	if len(input_string) % 2:
		raise OddLengthStringException("ERROR: String cannot be balanced because it has odd number" \
			" of characters.")
	open_bracket_count = 0
	number_of_reversals_required = 0

	for index_counter in range(len(input_string)):
		if input_string[index_counter] == "{":
			open_bracket_count += 1
		else:
			if open_bracket_count == 0:
				open_bracket_count += 1
				number_of_reversals_required += 1
			else:
				open_bracket_count -= 1
	number_of_reversals_required += open_bracket_count / 2
	print number_of_reversals_required

if __name__ == '__main__':
	try:
		string_expression = raw_input("Enter string expression: ")
		count_reversals_required_to_balance_string(string_expression)
	except OddLengthStringException as olse:
		print olse
