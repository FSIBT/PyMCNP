"""
Usage:
    demo <inp>
"""

import docopt


def main():
    args = docopt.docopt(__doc__)

    try:
        open(args['<inp>'])
    except FileNotFoundError:
        exit(1)

    path = ''.join(args['<inp>'].split('.')[:-1]) + '.outp'
    with open(path, 'x') as file:
        file.write('MCNP Output! :)')
