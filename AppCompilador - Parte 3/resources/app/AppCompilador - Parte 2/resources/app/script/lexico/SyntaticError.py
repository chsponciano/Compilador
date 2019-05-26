from AnalysisError import AnalysisError

class SyntaticError(AnalysisError):
	def __init__(self, msg, position):
		super(SyntaticError, self).__init__(msg, position)