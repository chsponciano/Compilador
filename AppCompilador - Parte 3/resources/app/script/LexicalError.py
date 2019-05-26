from AnalysisError import AnalysisError

class LexicalError(AnalysisError):
	def __init__(self, msg, line):
		super(LexicalError, self).__init__(msg, line)

	def __str__(self):
		return f'Erro na linha {self.line} - {self.msg}'