""" Exceptions.py: This file contains all exceptions required by classes in repository. """

__author__ = "Pratik Shah"
__maintainer__ = __author__

class BaseClassException(Exception):
	""" Base class for all exception """
	pass

class StackEmptyException(BaseClassException):
	""" Class for stack empty exception """
	pass

class StackFullException(BaseClassException):
	""" Class for stack full exception """
	pass

class OddLengthStringException(BaseClassException):
	""" Raised this exception if string_expression length is odd """
	pass

class QueueEmptyException(BaseClassException):
	""" Class for queue empty exception """
	pass

class QueueFullException(BaseClassException):
	""" Class for queue full exception """
	pass

class EmptyRootException(BaseClassException):
	""" Class for empty root in singly linked list program """
	pass

class ArrayLengthNotSameException(BaseClassException):
	""" Class for array length is not same in ReorderArray program """
	pass
