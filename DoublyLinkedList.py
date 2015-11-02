""" DoublyLinkedList.py: Program for doubly linked list operations """

__author__ = "Pratik Shah"
__maintainer__ = __author__

from Exceptions import EmptyRootException

class Node():
	""" Node class to create new node """
	def __init__(self, data, prev_node=None, next_node=None):
		self.data = data
		self.next = next_node
		self.prev = prev_node

class DoublyLinkedList():
	""" Main class for performing operations of doubly linked list """
	def __init__(self):
		self.root = None

	def insert_node(self, data):
		""" Insert new node in linked list """
		if self.root is None:
			self.root = Node(data)
		else:
			current_node = self.root
			while current_node.next is not None:
				current_node = current_node.next
			current_node.next = Node(data, current_node)

	def display_nodes(self):
		""" Display linked list nodes """
		if self.root is None:
			raise EmptyRootException("ERROR: No node available in list. Please insert node in list.")
		current_node = self.root
		while current_node is not None:
			print "Node data: %s" % current_node.data
			current_node = current_node.next

	def search_node(self, data):
		""" Search for specified data in list of nodes """
		if self.root is None:
			raise EmptyRootException("ERROR: No node available in list. Please insert node in list.")
		current_node = self.root
		while current_node is not None:
			if current_node.data == data:
				print "Node with data %s has been found in list" % data
				return
			current_node = current_node.next
		print "Node with data %s not found in list" % data

	def delete_node_at_beginning(self):
		""" Delete start node of linked list """
		if self.root is None:
			raise EmptyRootException("ERROR: No node available in list. Please insert node in list.")
		current_node = self.root
		self.root = current_node.next
		self.root.prev = None
		self.display_nodes()

	def delete_node_at_end(self):
		""" Delete last node of linked list """
		if self.root is None:
			raise EmptyRootException("ERROR: No node available in list. Please insert node in list.")
		current_node = self.root
		while current_node.next.next is not None:
			current_node = current_node.next
		current_node.next = None
		self.display_nodes()

	def delete_node_at_position(self, position):
		""" Delete node at given position """
		if self.root is None:
			raise EmptyRootException("ERROR: No node available in list. Please insert node in list.")
		node_count = 0
		if node_count == position:
			self.delete_node_at_beginning()
		else:
			current_node = self.root
			for node_count in range(position-1):
				current_node = current_node.next
			current_node.next = current_node.next.next
			self.display_nodes()

def show_menu():
	""" Show operation menu on console """
	choice = 0
	dll_object = DoublyLinkedList()

	while choice >= 0 and choice < 7:
		print "\n1. Insert node"
		print "2. Search node"
		print "3. Delete node at beginning"
		print "4. Delete node at end"
		print "5. Delete node at position"
		print "6. Display nodes"
		print "7. Exit"
		choice = int(input("Enter choice: "))

		try:
			if choice == 1:
				data = int(input("Enter integer data: "))
				dll_object.insert_node(data)
			elif choice == 2:
				data = int(input("Enter integer data to search: "))
				dll_object.search_node(data)
			elif choice == 3:
				dll_object.delete_node_at_beginning()
			elif choice == 4:
				dll_object.delete_node_at_end()
			elif choice == 5:
				position = int(input("Enter index of node to delete: "))
				dll_object.delete_node_at_position(position)
			elif choice == 6:
				dll_object.display_nodes()
		except EmptyRootException as er:
			print er
if __name__ == '__main__':
	show_menu()
