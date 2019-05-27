from AnalysisError import AnalysisError

class SyntaticError(AnalysisError):
	def __init__(self, msg, line, token):
		super(SyntaticError, self).__init__(msg, line)
		self._token = token

	@property
	def token(self):
		return self._token

	def __str__(self):
		return f'Erro na linha {self.line} - encontrado {self.token} {self.msg}'