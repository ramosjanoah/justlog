from datetime import datetime
import os
import pprint

LOG_FILE = 'log'
MAX_SIZE = os.get_terminal_size().columns
LAST_INFO_LENGTH = 25

def printl(text=None, type_='i'):
	"""
		@params type:
			i for Info ([I])
			e for Error ([E])
			w for Warnings ([W])
	"""
	if text == None:
		return
	if not isinstance(type_, str):
		raise Exception("paramater type_ must be 'i', 'e', xor 'w")

	type_ = type_[0].lower()
	if type_ == 'i':
		prefix = '[I]'
	elif type_ == 'e':
		prefix = '[E]'
	elif type_ == 'w':
		prefix = '[W]'

	date = datetime.now().strftime('%y-%d-%m')
	time = datetime.now().strftime('%H:%M:%S')

	# formatting for dictionary
	if isinstance(text, dict):
		f_text = '{} {} {} -- '.format(prefix, date, time, text)
		len_info = len(f_text)
		pformat_dict = pprint.pformat(text).split('\n')
		for i in range(len(pformat_dict)):
			if i != 0:
				pformat_dict[i] = ''.join([' ' for x in range(len_info)]) + pformat_dict[i]
		f_text = f_text + '\n'.join(pformat_dict)

	# formatting for string
	elif isinstance(text, str):
		f_text = '{} {} {} -- '.format(prefix, date, time)
		max_len = MAX_SIZE - len(f_text) - 1
		# formatting if length of string is more than max_len
		if len(text) > max_len:
			chunked_text = [text[i:i+max_len] for i in range(0, len(text), max_len)]
			for i in range(len(chunked_text)):
				if i != 0:
					chunked_text[i] = ''.join([' ' for x in range(len(f_text))]) + chunked_text[i]
			f_text = f_text + '\n'.join(chunked_text)

		# else, print it regularly
		else:
			f_text = '{} {} {} -- {}'.format(prefix, date, time, text)

	with open(LOG_FILE, 'a') as fo:
		fo.write(f_text)
		fo.write('\n')
	print(f_text)

def change_LOG_FILE(filename, move_log=True):
	global LOG_FILE
	if move_log:
		copy_log_to_file(filename)
	os.remove(LOG_FILE)
	LOG_FILE = filename

def copy_log_to_file(filename):
	with open(LOG_FILE) as fi:
		text = fi.read()
	with open(filename, 'w') as fo:
		fo.write(text)

def clear_log():
	with open(LOG_FILE, 'w') as fo:
		fo.write('')

def set_max_length(size):
	if size <= 26:
		raise Exception("size must bigger than 26")
	global MAX_SIZE 
	MAX_SIZE = size