"""
Problem: Reverse an array without affecting special characters.

Description: Given a string, that contains special character together with alphabets 
('a' to 'z' and 'A' to 'Z'), reverse the string in a way that special characters are not affected.

Examples:
1. Input:   str = "a,b$c"
   Output:  str = "c,b$a"
2. Input:   str = "Ab,c,de!$"
   Output:  str = "ed,c,bA!$"
"""

__author__ = "Pratik Shah"
__maintainer__ = __author__


def convert_string_to_list(input_string):
	""" Convert given string into the list as we cannot assign characters in string structure """
	output_list = []
	for character in input_string:
		output_list.append(character)
	return output_list

def reverse_string(input_string):
	""" Reverse string without affecting special characters """
	converted_list = convert_string_to_list(input_string)
	start_counter = 0
	end_counter = len(input_string)-1

	while start_counter < end_counter:
		if input_string[start_counter].isalpha() and input_string[end_counter].isalpha():
			temp_start_character = converted_list[start_counter]
			temp_end_character = converted_list[end_counter]
			converted_list[start_counter] = temp_end_character
			converted_list[end_counter] = temp_start_character
			start_counter += 1
			end_counter -= 1
		elif not input_string[start_counter].isalpha():
			start_counter += 1
		elif not input_string[end_counter].isalpha():
			end_counter -= 1
	print "".join(converted_list)

if __name__ == '__main__':
	string_expression = raw_input("Enter input string: ")
	reverse_string(string_expression)
