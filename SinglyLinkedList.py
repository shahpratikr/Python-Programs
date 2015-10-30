""" SinglyLinkedList.py: Program for singly linked list operations. """

__author__ = "Pratik Shah"
__maintainer__ = __author__

from Exceptions import EmptyRootException

class Node():
	""" Node class to initialize new node """

	def __init__(self, data):
		self.data = data
		self.next = None

class SinglyLinkedList():
	""" Main class for singly linked list operations """

	def __init__(self):
		self.root = None

	def insert_node(self, data):
		""" Insert node to linked list """
		if self.root is None:
			self.root = Node(data)
		else:
			current_node = self.root
			while current_node.next is not None:
				current_node = current_node.next
			current_node.next = Node(data)

	def display_nodes(self):
		""" Display nodes in linked list """
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
		""" Delete first node of list """
		if self.root is None:
			raise EmptyRootException("ERROR: No node available in list. Please insert node in list.")
		current_node = self.root
		self.root = current_node.next
		del current_node
		self.display_nodes()

	def delete_node_at_end(self):
		""" Delete last node in list """
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
		current_node = self.root
		if node_count == position:
			self.delete_node_at_beginning()
		else:
			for node_count in range(position-1):
				current_node = current_node.next
			current_node.next = current_node.next.next
			self.display_nodes()


def show_menu():
	""" Display menu on console """
	choice = 0
	singly_linked_list_object = SinglyLinkedList()

	while choice >= 0 and choice < 7:
		print "\n1. Insert Node"
		print "2. Search Node"
		print "3. Display Node"
		print "4. Delete first node of list"
		print "5. Delete last node of list"
		print "6. Delete node at given position"
		print "7. Exit"
		choice = int(input("Enter choice: "))

		try:
			if choice == 1:
				data = int(input("Enter integer data to insert in list: "))
				singly_linked_list_object.insert_node(data)
			elif choice == 2:
				data = int(input("Enter integer data to search in list: "))
				singly_linked_list_object.search_node(data)
			elif choice == 3:
				singly_linked_list_object.display_nodes()
			elif choice == 4:
				singly_linked_list_object.delete_node_at_beginning()
			elif choice == 5:
				singly_linked_list_object.delete_node_at_end()
			elif choice == 6:
				position = int(input("Enter position from which node should be deleted: "))
				singly_linked_list_object.delete_node_at_position(position)
		except (ValueError, NameError):
			print "ERROR: Data entered should be an integer value"
		except EmptyRootException as er:
			print er

if __name__ == '__main__':
	show_menu()
