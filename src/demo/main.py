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

    file = open('.' + ''.join(args['<inp>'].split('.')[:-1]) + '.outp', 'x')
    file.write('MCNP Output! :)')
    file.close()
