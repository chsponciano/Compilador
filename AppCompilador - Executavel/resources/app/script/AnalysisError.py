class AnalysisError(Exception):
	def __init__(self, msg, line):
		super(AnalysisError, self).__init__(msg)
		self._msg = msg
		self._line = line

	@property
	def line(self):
		return self._line

	@property
	def msg(self):
		return self._msg