from utils import log
from bot.bot import Bot

if __name__ == '__main__':
	try:
		while True:
			Bot().run()
	except KeyboardInterrupt:
		pass
	except Exception as exc:
		print("Error: {}".format(exc))
		log.Log('error_log.txt').error(exc)
