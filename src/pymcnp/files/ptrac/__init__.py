import re


from enum import Enum


class PtracKeywords(Enum):
	BUFFER = 1
	CELL = 2
	EVENT = 3
	FILE = 4
	FILTER = 5
	MAX	 = 6
	MENP = 7
	NPS	 = 8
	SURFACE = 9
	TALLY = 10
	TYPE = 11
	VALUE = 12
	WRITE = 13
	UNKNOWN = 14


from . import ptrac