class Stack:
	def __init__(self):
		self.stack = []
		self.len_stack = 0

	def push(self, e):
		self.stack.append(e)
		self.len_stack += 1

	def pop(self):
		if not self.empty():
			self.len_stack -= 1
			return self.stack.pop(-1)
		return None

	def peek(self):
		if not self.empty():
			return self.stack[-1]
		return None

	def empty(self):
		return (self.len_stack == 0)

	def length(self):
		return self.len_stack

	def clear(self):
		self.stack = []
		self.len_stack = 0