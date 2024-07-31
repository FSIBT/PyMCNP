import os

from ..files.inp import inp


ERROR_INSUFFICENT_ARGS = "\x1b[1mpymcnp: \x1b[31mERROR:\x1b[0m Insufficent Arguments."
ERROR_EXCESSIVE_ARGS = "\x1b[1mpymcnp: \x1b[31mERROR:\x1b[0m Excesive Arguments."
ERROR_UNRECOGNIZED_ARGS = "\x1b[1mpymcnp: \x1b[31mERROR:\x1b[0m Unrecognized Arguments."
ERROR_UNRECOGNIZED_OPTION = "\x1b[1mpymcnp: \x1b[31mERROR:\x1b[0m Unrecognized Option."
ERROR_ALIAS_NOT_FOUND = "\x1b[1mpymcnp: \x1b[31mERROR:\x1b[0m INP Alias Not Found."
ERROR_FILE_NOT_FOUND = "\x1b[1mpymcnp: \x1b[31mERROR:\x1b[0m File Not Found."

ERROR_INP_VALUE = lambda _: "\x1b[1mpymcnp: \x1b[31mERROR:\x1b[0m INP Syntax Error: " + _
ERROR_INP_SYNTAX = lambda _: "\x1b[1mpymcnp: \x1b[31mERROR:\x1b[0m INP Value Error: " + _

INFO_RUNNING_CQEDITOR = "\x1b[1mpymcnp: \x1b[31m\x1b[34mINFO:\x1b[0m Launching CQ-Editor."
INFO_RUNNING_MCNP = "\x1b[1mpymcnp: \x1b[31m\x1b[34mINFO:\x1b[0m Launching MCNP."
INFO_BUILD_INP = "\x1b[1mpymcnp: \x1b[31m\x1b[34mINFO:\x1b[0m Built INP."
INFO_BUILD_CELL = "\x1b[1mpymcnp: \x1b[31m\x1b[34mINFO:\x1b[0m Built Cell."
INFO_BUILD_SURFACE = "\x1b[1mpymcnp: \x1b[31m\x1b[34mINFO:\x1b[0m Built Surface."
INFO_BUILD_DATUM = "\x1b[1mpymcnp: \x1b[31m\x1b[34mINFO:\x1b[0m Built Datum."
INFO_BUILD_TITLE = "\x1b[1mpymcnp: \x1b[31m\x1b[34mINFO:\x1b[0m Built Title."
INFO_BUILD_MESSAGE = "\x1b[1mpymcnp: \x1b[31m\x1b[34mINFO:\x1b[0m Built Message."
INFO_BUILD_OTHER = "\x1b[1mpymcnp: \x1b[31m\x1b[34mINFO:\x1b[0m Built Other."

SAVE_FILE = "pymcnp-save.txt"

import os.path
if not os.path.isfile(SAVE_FILE):
	os.system(f"touch ./{SAVE_FILE}")

def error(msg):
	print(msg)
	exit(1)


def get_save() -> dict:

	with open(SAVE_FILE, 'r') as file:
		lines = file.readlines()

	inpts = {}
	for line in lines:
		if not line: continue
		alias, path = line.strip().split(' ')

		if not os.path.isfile(path): continue
		inpts[alias] = (path, inp.Inp().from_mcnp_file(path))

	return inpts


def set_save(inpts) -> None:

	output = ''
	for alias, value in inpts.items():
		path, inpt = value
		output += f"{alias} {path}\n"

	with open(SAVE_FILE, 'w') as file:
		file.write(output)

from . import cq
from . import inpt
from . import ls
from . import run