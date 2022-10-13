# FIFO (first-in, first-out)

class Queue:
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0
	
	# this method takes in a value and adds it to the queue if there is space or if the queue is empty. If the queue is full, it will print the message “Sorry, no more room!”.
	def enqueue(self, value):
		if self.has_space():
			item_to_add = Node(value)
			print("Adding " + str(item_to_add.get_value()) + " to the queue!")
			if self.is_empty():
				self.head = item_to_add
				self.tail = item_to_add
			else:
				self.tail.set_next_node(item_to_add)
				self.tail = item_to_add
				self.size += 1
		else:
			print("Sorry, no more room!")

	# this method removes the value from the queue or prints “The queue is totally empty!” if there are no existing values.
	def dequeue(self):
		if self.get_size() > 0:
			item_to_remove = self.head
			print(str(item_to_remove.get_value()) + " is served!")
			if self.get_size() == 1:
				self.head = None
				self.tail = None
			else:
				self.head = self.head.get_next_node()
				self.size -= 1
			return item_to_remove.get_value()
		else:
			print("The queue is totally empty!")

	# this method returns the front value in the queue if there are existing values. If there are no values, it will print the message “No orders waiting!.”.
	def peek(self):
		if self.size > 0:
			return self.head.get_value()
		else:
			print("No orders waiting!")
	
	# this method returns the size of the queue.
	def get_size(self):
		return self.size
	
	# this method checks to see if the queue is empty.
	def is_empty(self):
		return self.size == 0
