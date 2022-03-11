import json  # Подключили библиотеку
import os


class ParseJSON:
	def __init__(self, tests, values):
		self.tests = tests
		self.values = values
		self.resp = {}

	def main_parse(self):
		test = read_json(self.tests)
		value = read_json(self.values)
		self.json_parse(value)
		self.json_parse(test, True)
		report_json = json.dumps(test, indent=4)
		with open(f'{os.getcwd()}/report.json', 'w') as f:
			f.write(report_json)
		return

	def json_parse(self, data, write=False):
		if isinstance(data, dict):
			for item in data:
				if isinstance(data.get(item), list):
					for x in data.get(item):
						if not write:
							self.insert_value(x)
							if x.get('values'):
								self.json_parse(x['values'], write)
						elif write:
							self.json_write(x)
							if x.get('values'):
								self.json_parse(x['values'], write)
		elif isinstance(data, list):
			for i in data:
				if not write:
					self.insert_value(i)
				elif write:
					self.json_write(i)
				self.json_parse(i, write)

	def insert_value(self, dct):
		id = dct.get('id')
		value = dct.get('value')
		self.resp[id] = value

	def json_write(self, dct):
		dct['value'] = self.resp.get(dct['id'])


def read_json(file):
	with open(file, 'r', encoding='utf-8') as f:
		file = json.load(f)
	return file


if __name__ == '__main__':
	tests = input('Путь до файла tests.json: ')
	values = input('Путь до файла values.json: ')
	parse = ParseJSON(tests, values)
	parse.main_parse()
