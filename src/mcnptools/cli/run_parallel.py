"""Usage:
   mcnptools-run-parallel [options] <inputfile> <nr_run>

Options:
  -n --dry-run         just print the commands it would run_dir
  --prefix=<pre>       prefix for the subdirectories to be used [default: sim].
                       The simulations will add the run_nr to this prefix [default: sims].
  --log                Log the random seed in a file, so that runs can be reproduced
  --dir=<dir>          directory for all simulatinos to run in
                       (defaults to sim-<inputfile without .i>-<date).
  -S --hosts=<hosts>   List of hosts to run on.

Runs the inputfile in mcnp in parallel on several hosts (with -S
option). It will figure out how many nodes/cores/threads are available
and then divide the number of particles by that amount and run one
simulations on each host.

We also check for SLURM variables on a cluster and use those to figure
out the available nodes.

The simulations and all subdirectories will be saved in the working
directory, that can be set using --dir.

TODO:
* support parameter scans
* how to get return files? use --return for parallel?

"""

from datetime import datetime
import os
from pathlib import Path
import subprocess
import sys

import docopt
import numpy as np
from rich import print
import shutil

import mcnptools as mt


def main():
    command = docopt.docopt(__doc__)
    # print(command)

    DRY_RUN = command["--dry-run"]
    PREFIX = command["--prefix"]
    LOG = command["--log"]
    WORKING_DIR = command["--dir"]
    HOSTS = command["--hosts"]

    INPUT = Path(command["<inputfile>"])
    NR_RUN = int(command["<nr_run>"])

    PARALLEL = shutil.which("parallel")
    if PARALLEL is None:
        print("[red]ERROR[/] Cannot find GNU parallel program.")
        sys.exit(1)

    # also test mcnp availabilty although we are not using it here
    if shutil.which("mcnp6") is None:
        print("[red]ERROR[/] Cannot find MCNP6 program.")
        sys.exit(2)

    if not INPUT.is_file():
        print(f"[red]ERROR[/] Cannot find input file {INPUT}.")
        sys.exit(3)

    if WORKING_DIR is None:
        date = datetime.today().strftime("%Y-%m-%d--%H-%M-%S")
        WORKING_DIR = Path(".") / f"sim-{INPUT.stem}-{date}"
    if not WORKING_DIR.is_dir():
        print(
            f"[yellow]INFO[/] Creating working directory: '{WORKING_DIR.absolute()}'."
        )
        WORKING_DIR.mkdir(parents=True)
    else:
        print(
            f"[yellow]INFO[/] Using existing working directory: '{WORKING_DIR.absolute()}'."
        )

    if HOSTS is None:
        HOSTS = os.getenv("SLURM_JOB_NODELIST")

    REMOTE_OPTION = ""
    if HOSTS:
        # we are doing remote, so add a working dir and also return data
        REMOTE_OPTION = (
            f"--workdir $HOME/.parallel/tmp "
            f"--return {WORKING_DIR}/{PREFIX}{{0#}} "
            f"--basefile {INPUT.absolute().parent}/./{INPUT.name}"
        )

    HOSTS = f"-S {HOSTS}" if HOSTS else ""
    command_to_run = (
        f"{PARALLEL} --plus {REMOTE_OPTION} {HOSTS}"
        + f" 'MCNPtools-run-single --prefix={PREFIX} --dir={WORKING_DIR}"
        + f" {INPUT} {{}} {NR_RUN}'"
        + f" ::: {{1..{NR_RUN}}}"
    )
    if DRY_RUN:
        print("[yellow]INFO[/] Would run:")
        print(f"   {command_to_run}")
    else:
        subprocess.run(command_to_run, shell=True)
