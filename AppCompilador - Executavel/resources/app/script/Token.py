class Token:
	def __init__(self, identification, lexeme, position):
		self._identification = identification
		self._lexeme = lexeme
		self._position = position

	@property
	def identification(self):
		return self._identification
	
	@identification.setter
	def identification(self, identification):
		self._identification = identification

	@property
	def lexeme(self):
		return self._lexeme

	@lexeme.setter
	def lexeme(self, lexeme):
		self._lexeme = lexeme

	@property
	def position(self):
		return self._position
	
	@position.setter
	def position(self, position):
		self._position = position