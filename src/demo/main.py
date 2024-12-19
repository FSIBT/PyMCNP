import sys

import docopt


DEMO_DOCOPT = """
Usage:
    demo <inp>
"""


def main():
    args = docopt.docopt(DEMO_DOCOPT)

    try:
        open(args['<inp>'])
        print(f"[DEMO] Args: {' '.join(sys.argv)}")
    except FileNotFoundError:
        print('[DEMO] Input file not found.')
        exit(1)

    path = ''.join(args['<inp>'].split('.')[:-1]) + '.outp'
    with open(path, 'x') as file:
        print(path)
        file.write('MCNP Output! :)')
