import logging
import logging.config

class FFLog:
	logger = None
	@staticmethod
	def Logger():
		if FFLog.logger == None:
			logging.config.fileConfig("logging.config")  # 采用配置文件
			FFLog.logger = logging.getLogger("logger_root")
		return FFLog.logger

'''
	logger.debug("debug message")
	logger.info("info message")
	logger.warn("warn message")
	logger.error("error message")
	logger.critical("critical message")'''