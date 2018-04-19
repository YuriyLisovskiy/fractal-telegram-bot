class Log:

	def __init__(self, file_path):
		self.file_path = file_path

	def __log(self, log_type, message):
		file = open(self.file_path, 'a')
		file.write('{}: {}\n'.format(log_type, message))
		file.close()

	def error(self, message):
		self.__log('ERROR', message)

	def warning(self, message):
		self.__log('WARNING', message)

	def info(self, message):
		self.__log('INFO', message)

	def time(self, message, time):
		self.__log(message, time)
