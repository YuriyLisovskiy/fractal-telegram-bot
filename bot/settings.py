# Bot token received after bot registration in Telegram
TOKEN = 'set_in_local_settings'

# Developer chat id for daily error report (Set in local settings)
AUTHOR_CHAT_ID = 0

try:
	from .local_settings import *
except ImportError:
	pass

# Report time
REPORT_TIME = '23:00:00.5'


# This message will be shown when bot is started
START_MSG = 'Fractal Bot\nVersion 0.1.0\nStarted listening for updates...'


# Base url for bot responses
BASE_URL = 'https://api.telegram.org/bot{}/'.format(TOKEN)


# Template for successful response message
RESPONSE_SENT = '{} response sent, time: {}'

# Template for failing response message
RESPONSE_FAILED = '{} response failed, time: {}'


# Available commands
COMMAND_START = '/start'
COMMAND_HELP = '/help'
COMMAND_BUG = '/bug'
