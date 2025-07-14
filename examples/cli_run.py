"""
Example running INP files using ``Run``.
"""

import pathlib

import pymcnp


# Creating ``Run`` subclass.
class MyRun(pymcnp.cli.Run):
    def prehook_file(self, path, index):
        print(f'Calling ``prehook_file`` {path} {index}')

    def posthook_file(self, path, index):
        print(f'Calling ``posthook_file`` {path} {index}')

    def prehook_batch(self, path):
        print(f'Calling ``prehook_batch`` {path}')

    def posthook_batch(self, path):
        print(f'Calling ``posthook_batch`` {path}')


# Reading INP.
path0 = pathlib.Path(__file__).parent / 'files' / 'inp' / 'F1F8.i'
path1 = pathlib.Path(__file__).parent / 'files' / 'inp' / 'F1F8.i'
path2 = pathlib.Path(__file__).parent / 'files' / 'inp' / 'F1.i'
inp0 = pymcnp.Inp.from_file(path0)
inp1 = pymcnp.Inp.from_file(path1)
inp2 = pymcnp.Inp.from_file(path2)

# Running.
runner = MyRun([inp0, inp1, inp2], command='echo')
runner.run('.')
