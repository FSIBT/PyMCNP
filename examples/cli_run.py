"""
Examples for running INP files using ``Run``.
"""

import pathlib

import pymcnp


# Creating ``Run`` subclass.
class MyRun(pymcnp.cli.Run):
    def prehook_file(self, path):
        print(f'Calling ``prehook_file`` {path}')

    def posthook_file(self, path):
        print(f'Calling ``posthook_file`` {path}')

    def prehook_batch(self, path):
        print(f'Calling ``prehook_batch`` {path}')

    def posthook_batch(self, path):
        print(f'Calling ``posthook_batch`` {path}')


# Reading INP.
inp0 = pymcnp.Inp.from_file(pathlib.Path(__file__).parent / 'files' / 'inp' / 'F1F8.i')
inp1 = pymcnp.Inp.from_file(pathlib.Path(__file__).parent / 'files' / 'inp' / 'F1F8.i')
inp2 = pymcnp.Inp.from_file(pathlib.Path(__file__).parent / 'files' / 'inp' / 'F1.i')

# Running.
runner = MyRun([inp0, inp1, inp2], command='echo')
runner.run('.')
