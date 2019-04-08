from LexicoConstants import LexicoConstants
from LexicalError import LexicalError
from Token import Token

class Lexico(LexicoConstants):
	def __init__(self, input_text):
		super(Lexico, self).__init__()
		self._input_text = input_text
		self._position = 0

	@property
	def position(self):
		return self._position
	
	@position.setter
	def position(self, position):
		self._position = position

	def hasInput(self):
		return self._position < len(self._input_text)

	def classLexeme(self, token):
		if token == 2:
			return self.CLASS_LEXEME[0]
		elif token == 3:
			return self.CLASS_LEXEME[1]
		elif token == 4:
			return self.CLASS_LEXEME[2]
		elif token == 5:
			return self.CLASS_LEXEME[3]
		elif token == 6:
			return self.CLASS_LEXEME[4]
		elif token >= 9 and token <= 30:
			return self.CLASS_LEXEME[5]
		elif token >= 31 and token <= 47:
			return self.CLASS_LEXEME[6]

		return -1

	def lineToken(self, position):
		aux = self._input_text[0:position]
		return len(aux.split("\n"))


	def nextChar(self):
		out = -1
		
		if self.hasInput:
			out = list(self._input_text)[self._position]
			self._position += 1

		return out

	def lookupToken(self, base, key):
		start = self.SPECIAL_CASES_INDEXES[base]
		end = self.SPECIAL_CASES_INDEXES[base + 1] - 1

		while start <= end:
			half = int((start + end) / 2)
			comp = self.compareTo(self.SPECIAL_CASES_KEYS[half], key)
			if comp == 0:
				return self.SPECIAL_CASES_VALUES[half]
			elif comp < 0:
				start = half + 1
			else:
				end = half - 1

		return base 

	def compareTo(self, str1, str2):
		if str1 == str2:
			return 0

		elif str1 < str2:
			return -1

		return 1

	def tokenForState(self, state):
		if state < 0 or state >= len(self.TOKEN_STATE):
			return -1

		return self.TOKEN_STATE[state]

	def nextState(self, c, state):
		start = self.SCANNER_TABLE_INDEXES[state]
		end = self.SCANNER_TABLE_INDEXES[state + 1] - 1
		c = ord(c)

		while start <= end:
			half = int((start + end) / 2)

			if self.SCANNER_TABLE[half][0] == c:
				return self.SCANNER_TABLE[half][1]
			elif self.SCANNER_TABLE[half][0] < c:
				start = half + 1
			else:
				end = half - 1

		return -1

	def nextToken(self):
		if not self.hasInput():
			return None

		start = self._position
		state = 0
		lastState = 0
		endState = -1
		end = -1

		while self.hasInput():
			lastState = state
			state = self.nextState(self.nextChar(), state)

			if state < 0:
				break
			else:
				if self.tokenForState(state) >= 0:
					endState = state
					end = self._position

		if endState < 0 or (endState != state and self.tokenForState(lastState) == -2):
			raise LexicalError(self.SCANNER_ERROR[lastState], self.lineToken(start), self._input_text[start])

		self._position = end
		token = self.tokenForState(endState)

		if token == 0:
			return self.nextToken()
		else:
			lexeme = self._input_text[start:end]
			token = self.lookupToken(token, lexeme)
			classLexeme = self.classLexeme(token)
			line = self.lineToken(start)
			return Token(classLexeme, lexeme, line)
