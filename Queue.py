""" Queue.py: Program for Queue operations """

__author__ = "Pratik Shah"
__maintainer__ = __author__

from Exceptions import QueueEmptyException, QueueFullException

class Queue():
	""" Main queue class """
	def __init__(self, array_size):
		self.rear = 0
		self.front = -1
		self.data_array = []
		self.MAXSIZE = array_size

	def check_is_empty(self):
		""" Check if queue is empty or not """
		if self.rear == self.front+1:
			return True

	def check_is_full(self):
		""" Check if queue is full or not """
		if self.front == self.MAXSIZE-1:
			return True

	def insert(self, data):
		""" Insert data in queue """
		self.front += 1
		self.data_array.insert(self.front, data)

	def remove(self):
		""" Delete data from queue """
		if self.check_is_empty():
			raise QueueEmptyException("ERROR: Queue is empty")
		data = self.data_array.pop(self.rear)
		self.front -= 1
		return data

	def display(self):
		""" Display elements of queue """
		current_top = 0
		while current_top <= self.front:
			print "%s" % self.data_array[current_top]
			current_top += 1
			if self.check_is_empty():
				raise QueueEmptyException("ERROR: Queue is empty. Can't show elements in queue.")

def show_menu():
	""" Show menu for queue operation """
	choice = 0
	array_size = int(input("Enter size for array as interger value: "))
	queue_object = Queue(array_size)
	
	while choice >= 0 and choice < 4:
		print "1. Insert"
		print "2. Delete"
		print "3. Display"
		print "4. Exit"
		choice = int(input("Enter choice: "))

		try:
			if choice == 1:
				if queue_object.check_is_full():
					raise QueueFullException("ERROR: Queue is full")
				data = int(input("Enter integer data: "))
				queue_object.insert(data)
			elif choice == 2:
				print "Data deleted is: %s" % queue_object.remove()
			elif choice == 3:
				queue_object.display()
		except QueueEmptyException as qe:
			print qe
		except QueueFullException as qf:
			print qf

if __name__ == '__main__':
	show_menu()
