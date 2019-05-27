from AnalysisError import AnalysisError

class LexicalError(AnalysisError):
	def __init__(self, msg, position, token):
		super(LexicalError, self).__init__(msg, position)
		self._token = token

	@property
	def token(self):
		return self._token

	def mensagem_error(self):
		return f'Error na linha {self.position} - {self.token} {self.msg}'
	


