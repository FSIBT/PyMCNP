"""
Run MCNP through Python using the package subprocess.
Code modifed from https://gist.github.com/abnowack
"""

import numpy as np
import subprocess
import shutil
import os
from pathlib import Path


def set_mcnp_environment(DATAPATH, ISCDATA, MCNPPATH, force=False):
    if force or 'DATAPATH' not in os.environ:
        os.environ['DATAPATH'] = DATAPATH

    if force or 'ISCDATA' not in os.environ:
        os.environ['ISCDATA'] = ISCDATA

    if force or 'MCNPPATH' not in os.environ:
        os.environ['MCNPPATH'] = MCNPPATH
        os.environ['PATH'] += os.pathsep + str(os.environ['MCNPPATH'])


def create_directory(directory):
    """
    If directory already exists, append 1 to the name and create a new one.
    If directory does not exist, create it.

    Parameters:
    directory (Path object): Directory path to check/create.
    """
    if directory.exists():
        print(f"Directory '{directory}' already exists.")
        new_name = directory.name + f'-{np.random.randint(0, 999)}'
        new_dir = directory.parent / new_name
        new_dir.mkdir()
        print(f"Directory '{new_dir}' created successfully.")
    else:
        new_dir = directory
        new_dir.mkdir()
        print(f"Directory '{new_dir}' created successfully.")
    return new_dir


def clean_directory(clean_dir):
    shutil.rmtree(clean_dir)


DATAPATH = r'C:\MCNP62\MCNP_DATA'
ISCDATA = r'C:\MCNP62\MCNP_CODE\MCNP620\Utilities\ISC\data'
MCNPPATH = r'C:\MCNP62\MCNP_CODE\bin'

set_mcnp_environment(DATAPATH, ISCDATA, MCNPPATH)

input_file = 'C:/Users/mayll/Documents/MCNP-tools/examples/Data/proton-dist.i'
# test_dir = "C:/Users/mayll/Documents/MCNP-tools/test-delete"

# args = f"i={input_file} o=testout.o"

# run = subprocess.run("mcnp6.exe " + args, shell=True, cwd=test_dir, capture_output=True)
# print(run)


def run_mcnp(input_file, out_dir=None, out_name=None, cores=1, clean=False):
    """
    Python interface for running MCNP

    Parameters
    ----------
    input_file : string
        Input file full path.
    out_dir : string, optional.
        Directory where output files will be saved. The default is None
        (will be saved to the same directory as the input file)
    out_name : string, optional.
        Output file name. The default is None
        (will be saved with the same name as the input file)
    cores : int, optional
        Number of threads used (not available for all particle types). The default is 1.
    clean : bool, optional
        Delete secondary output files. The default is False.

    Returns
    -------
    Dictionary with information about the run.
    """
    input_file = Path(input_file)
    if out_dir is None:
        out_dir = input_file.parent / 'test-folder'
        new_out_dir = create_directory(out_dir)
    else:
        new_out_dir = Path(out_dir)
    if out_name is None:
        new_name = input_file.name
    else:
        new_name = out_name
    if cores <= 2:
        args = f'i={input_file} o={new_name}.o'
    else:
        args = f'i={input_file} o={new_name}.o tasks {cores}'

    args = f'i={input_file} o={new_name}.o'
    run = subprocess.run('mcnp6.exe ' + args, shell=True, cwd=new_out_dir, capture_output=True)
    return run


out_dir = 'C:/Users/mayll/Documents/MCNP-tools/examples/Data/test-folder'
run = run_mcnp(input_file=input_file)

# @contextmanager
# def run_mcnp(card, extra_args=None, params=None, cores=1, clean=True):
#     """ Python interface for running MCNP programs.
#     Parameters
#     ----------
#     card : str
#         MCNP input card, can contain variable expressions using str.format(params)
#     extra_args: dict
#         Dictionary of additional arguments for MCNP, eg `mcnp $KEY=$VALUE`
#     params : dict, optional
#         Values to apply on MCNP input card
#     cores : int
#         Number of CPU cores for MCNP to run on
#     clean : bool
#         Clean the temporary output directory
#     Returns
#     -------
#     run : subprocess.CompletedProcess
#         Contains successful run information
#     output_dir : file directory
#         Temporary output directory containing MCNP results
#     """
#     if params:
#         card = card.format(**params)

#     args = []
#     if extra_args:
#         for (arg, val) in extra_args:
#                 args.append('{}={}'.format(arg, val))

#     args.append('tasks {}'.format(cores))

#     # create temp folder
#     output_dir = tempfile.mkdtemp()
#     with open(output_dir + '\\input.i', 'w') as f:
#         f.write(card)

#     args.append('i=input.i')

#     # mcnp doesn't use errorcodes or stderr, so Popen doesnt add features
#     # stick with simpler check_output and parse stdout
#     run = subprocess.run(['mcnp6.exe'] + args, shell=True, cwd=output_dir, capture_output=True)

#     # check for errors in stdout
#     stdout_str = str(run.stdout)
#     if 'bad trouble' in stdout_str or 'fatal error' in stdout_str:
#         print('Error in MCNP outout')
#         print(run.args)
#         print(run.stdout)
#         status = False
#     else:
#         status = True

#     try:
#         yield (run, output_dir)
#     finally:
#         if clean:
#             print(output_dir)
#             clean_directory(output_dir)

# if __name__ == '__main__':
#   DATAPATH=r'C:\MCNP62\MCNP_DATA'
#   ISCDATA=r'C:\MCNP62\MCNP_CODE\MCNP620\Utilities\ISC\data'
#   MCNPPATH=r'C:\MCNP62\MCNP_CODE\bin'

#   set_mcnp_environment(DATAPATH, ISCDATA, MCNPPATH)


#   input_card = \
#   r"""PUT YOUR MCNP INPUT CARD HERE
#   IT CAN HAVE {} for formatting the card with values filled in by params arg in run_mcnp
#   """

#   # use run_mcnp in the following way as a context manager
#   with run_mcnp(input_card, cores=4, clean=False) as (run, out_dir):
#   print(run.stdout)
#   print(out_dir)
