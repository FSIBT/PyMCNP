# THIS IS FOR TESTING

import sys

def main():
	if len(sys.argv) < 2: print("NO"); exit(1)

	inp = sys.argv[1]
	opt = sys.argv[1].split('.')[0] + '.txt'

	with open(inp, 'r') as file:
		out = '\n'.join(file.readlines()) + '\n'

	with open(opt, 'w') as file:
		file.write(out)

