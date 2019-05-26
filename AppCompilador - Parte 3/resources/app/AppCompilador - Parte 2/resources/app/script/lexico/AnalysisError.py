class AnalysisError(Exception):
	def __init__(self, msg, position):
		super(AnalysisError, self).__init__(msg)
		self._msg = msg
		self._position = position

	@property
	def position(self):
		return self._position

	@property
	def msg(self):
		return self._msg
	

	def __repr__(self):
		return f'{super}, @ {self._position}'		