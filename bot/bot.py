import os
import requests
import datetime
from utils import log
from .settings import *
from .text_answers import *
from datetime import timedelta
from utils.decorators import run_async


class Bot:

	def __init__(self):
		self.log_file = 'error_log.txt'
		self.bug_report = 'bug_report.txt'
		self.logger = log.Log(self.log_file)
		self.now = datetime.datetime.now() + timedelta(hours=3)

	def run(self):
		print(START_MSG)
		self.__send_error_log()
		new_offset = None
		while True:
			self.__get_updates(new_offset)
			last_update = self.__get_last_update()
			if last_update:
				last_update_data = self.__parse_last_update(last_update)
				if last_update_data['text']:
					try:
						self.__serve_user(
							command=last_update_data['text'],
							chat_id=last_update_data['chat_id'],
							username=last_update_data['username']
						)
					except Exception as exc:
						print('Error: {}'.format(exc))
						self.__send_message(
							chat_id=last_update_data['chat_id'],
							text=CRASHED
						)
						self.logger.error(exc)
				else:
					self.__send_message(
						chat_id=last_update_data['chat_id'],
						text=INVALID_INPUT
					)
				new_offset = last_update_data['id'] + 1

	@staticmethod
	def __parse_last_update(last_update):
		chat = last_update['message']['chat']
		data = {
			'id': last_update['update_id'],
			'chat_id': chat['id']
		}
		if 'username' in chat:
			data['username'] = '@' + chat['username']
		else:
			data['username'] = chat['first_name'] + ' ' + chat['last_name']
		if 'text' in last_update['message']:
			data['text'] = last_update['message']['text']
		else:
			data['text'] = None
		return data

	@staticmethod
	def __get_updates(offset=None, timeout=30):
		method = 'getUpdates'
		params = {
			'timeout': timeout,
			'offset': offset
		}
		response = requests.get(BASE_URL + method, params)
		if not response.json()['ok']:
			raise ValueError("Bot not found or invalid bot token.")
		return response.json()['result']

	@staticmethod
	def __send_message(chat_id, text):
		method = 'sendMessage'
		params = {
			'chat_id': chat_id,
			'text': text,
			'parse_mode': 'Markdown'
		}
		response = requests.post(BASE_URL + method, params)
		if response.json()['ok']:
			print(RESPONSE_SENT.format('Message', datetime.datetime.now()))
		else:
			print(RESPONSE_FAILED.format('Message', datetime.datetime.now()))
		return response

	@staticmethod
	def __send_photo(chat_id, photo):
		method = 'sendPhoto'
		response = requests.post(
			BASE_URL + method,
			data={'chat_id': chat_id},
			files={'photo': photo}
		)
		if response.json()['ok']:
			print(RESPONSE_SENT.format('Photo', datetime.datetime.now()))
		else:
			print(RESPONSE_FAILED.format('Photo', datetime.datetime.now()))
		return response

	@staticmethod
	def __send_document(params, doc):
		response = requests.post(
			BASE_URL + 'sendDocument',
			data=params,
			files={'document': doc}
		)
		if response.json()['ok']:
			print(RESPONSE_SENT.format('Report', datetime.datetime.now()))
		else:
			print(RESPONSE_FAILED.format('Report', datetime.datetime.now()))

	@run_async
	def __send_error_log(self):
		while True:
			self.now = datetime.datetime.now() + timedelta(hours=3)
			if str(self.now.time())[:10] == REPORT_TIME:
				if os.path.exists(self.log_file):
					self.logger.time('Report time', self.now)
					file = open(self.log_file, 'rb')
					params = {
						'chat_id': AUTHOR_CHAT_ID,
						'caption': '*Log report for developer*',
						'parse_mode': 'Markdown'
					}
					self.__send_document(params=params, doc=file)
					file.close()
					os.remove(self.log_file)
				else:
					self.__send_message(
						chat_id=AUTHOR_CHAT_ID,
						text='There are not any errors for {}'.format(self.now)
					)
				if os.path.exists(self.bug_report):
					params = {
						'chat_id': AUTHOR_CHAT_ID,
						'caption': '*Bug report for developer*',
						'parse_mode': 'Markdown'
					}
					file = open(self.bug_report, 'rb')
					self.__send_document(params=params, doc=file)
					file.close()
					os.remove(self.bug_report)
				else:
					self.__send_message(
						chat_id=AUTHOR_CHAT_ID,
						text='There are not any bug reports for {}'.format(self.now)
					)

	@staticmethod
	def __normalize_string(username):
		return username.replace('_', '\_')

	def __write_bug_report(self, command, username):
		log.Log(self.bug_report).error(
			'Bug report from {}\nMessage: {}\nTime: {}\n\n'.format(
				username,
				command[4:],
				self.now
			)
		)

	def __get_last_update(self):
		get_result = self.__get_updates()
		return get_result[-1] if len(get_result) > 0 else None

	def __serve_user(self, command, chat_id, username):
		data = {
			'chat_id': chat_id
		}
		if command == COMMAND_START:
			username = self.__normalize_string(username)
			data['text'] = START.format(username, username)
		elif command == COMMAND_HELP:
			data['text'] = HELP
		else:
			data['text'] = 'Sorry, this is beta version of Fractal Bot'
		return self.__send_message(**data)
