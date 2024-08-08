"""
'_save'
"""


import os.path
from typing import *

import pymcnp


class Save:
	"""
	'Save'
	"""

	def __init__(self, path) -> Self:
		"""
		'__init__'
		"""

		self.path = path

		if not os.path.isfile(path):
			os.system(f"touch ./{path}")


	def get_save(self) -> dict:
		"""
		'get_save'
		"""

		with open(self.SAVE_FILE, 'r') as file:
			lines = file.readlines()

		inpts = {}
		for line in lines:
			if not line: continue
			alias, path = line.strip().split(' ')

			if not os.path.isfile(path): continue
			inpts[alias] = (path, inp.Inp().from_mcnp_file(path))

		return inpts


	def set_save(self, inpts) -> None:
		"""
		'set_save'
		"""

		output = ''
		for alias, value in inpts.items():
			path, inpt = value
			output += f"{alias} {path}\n"

		with open(self.SAVE_FILE, 'w') as file:
			file.write(output)