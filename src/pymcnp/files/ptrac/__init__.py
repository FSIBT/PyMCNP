import re


def preprocess_ptrac(source: str):
	processed_source = re.compile(r"(\n\n)").sub("\n", source)
	processed_source = re.compile(r" \n").sub("\n", processed_source)
	processed_source = re.compile(r" +").sub(" ", processed_source)
	return processed_source


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


class PtracEventType(Enum):
	SOURCE = 1000
	SURFACE = 3000
	COLLISIONS = 4000
	TERMINATION = 5000
	FINAL = 9000

