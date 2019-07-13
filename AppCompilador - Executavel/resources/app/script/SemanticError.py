from AnalysisError import AnalysisError

class SemanticError(AnalysisError):
	def __init__(self, msg, line):
		super(SemanticError, self).__init__(msg, line)

	def __str__(self):
		return f'Erro na linha {self.line} - {self.msg}'
	
