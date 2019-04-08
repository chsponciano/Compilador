class Token:
	def __init__(self, classLexeme, lexeme, position):
		self._classLexeme = classLexeme
		self._lexeme = lexeme
		self._position = position

	@property
	def classLexeme(self):
		return self._classLexeme
	
	@classLexeme.setter
	def classLexeme(self, classLexeme):
		self._classLexeme = classLexeme

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

	def __repr__(self):
		return f'{str(self._position).ljust(8)}{self._classLexeme.ljust(20)}{self._lexeme}'