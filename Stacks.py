""" Stacks.py: Program for Stack operations """

__author__ = "Pratik Shah"
__maintainer__ = __author__

from Exceptions import StackEmptyException, StackFullException

class Stack():
	""" Main stack class """
	def __init__(self, array_max_size):
		self.top = -1
		self.data_array = []
		self.MAXSIZE = array_max_size

	def check_is_empty(self):
		""" Check if stack is empty or not """
		if self.top == -1:
			return True

	def check_is_full(self):
		""" Check if stack is full or not """
		if len(self.data_array) == self.MAXSIZE:
			return True

	def push(self, data):
		""" Push data to stack """
		self.top += 1
		self.data_array.insert(self.top, data)

	def pop(self):
		""" Pop data from stack """
		if self.check_is_empty():
			raise StackEmptyException("ERROR: Stack is empty")
		data = self.data_array.pop(self.top)
		self.top -= 1
		return data

	def display(self):
		""" Display contents of stack """
		current_top = self.top
		if self.check_is_empty():
			raise StackEmptyException("ERROR: Stack is empty")
		while current_top >= 0:
			print "%s" % self.data_array[current_top]
			current_top -= 1

def show_menu():
	""" Show menu for stack operation """
	choice = 0
	array_size = int(input("Enter size for array as interger value: "))
	stack_object = Stack(array_size)	
	
	while choice >= 0 and choice < 4:
		print "1. Push"
		print "2. Pop"
		print "3. Display"
		print "4. Exit"
		choice = int(input("Enter choice: "))

		try:
			if choice == 1:
				if stack_object.check_is_full():
					raise StackFullException("ERROR: Stack is full")
				data = int(input("Enter integer data: "))
				stack_object.push(data)
			elif choice == 2:
				print "Data popped is: %s" % stack_object.pop()
			elif choice == 3:
				stack_object.display()
		except StackEmptyException as se:
			print se
		except StackFullException as sf:
			print sf

if __name__ == '__main__':
	show_menu()
