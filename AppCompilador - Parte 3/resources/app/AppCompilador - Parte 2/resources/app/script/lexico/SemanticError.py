from AnalysisError import AnalysisError

class SemanticError(AnalysisError):
	def __init__(self, msg, position):
		super(SemanticError, self).__init__(msg, position)		