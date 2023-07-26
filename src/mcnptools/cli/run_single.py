"""Usage:
   mcnptools-run-single [options] <inputfile> <run_nr> <total_run_nr>

Options:
  -n --dry-run       just print the commands it would run_dir
  --prefix=<pre>     prefix for the subdirectories to be used [default: sim].
                     The simulations will add the run_nr to this prefix [default: sims].
  --log              Log the random seed in a file, so that runs can be reproduced
  --dir=<dir>        directory for all simulatinos to run in [default: .].

Runs the inputfile in mcnp. It will divide the number of particles by <total_run_nr>
and provide a random seed.

The simulations and all subdirectories will be saved in the working
directory, that can be set using --dir.

"""


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
    WORKING_DIR = Path(command["--dir"])

    INPUT = Path(command["<inputfile>"])
    RUN = int(command["<run_nr>"])
    TOTAL = int(command["<total_run_nr>"])

    if not INPUT.is_file():
        print(f"[red]ERROR[/] Cannot find input file '{INPUT.absolute()}'.")
        sys.exit(1)

    if not WORKING_DIR.is_dir():
        print(
            f"[yellow]INFO[/] Creating working directory: '{WORKING_DIR.absolute()}'."
        )
        WORKING_DIR.mkdir(parents=True)
    else:
        print(
            f"[yellow]INFO[/] Using existing working directory: '{WORKING_DIR.absolute()}'."
        )

    L = len(str(TOTAL))
    RUN_NAME = f"{PREFIX}{RUN:0{L}d}"  # needs to be the same as {0#} in gnu-parallel
    SIM_DIR = WORKING_DIR / RUN_NAME
    if SIM_DIR.is_file():
        print(
            f"[red]ERROR[/] A file with the name '{SIM_DIR.absolute()}' already exists... exiting."
        )
        sys.exit(2)
    SIM_DIR.mkdir(parents=True, exist_ok=True)

    input_file = mt.input_reader.Input(INPUT)
    nr = input_file.nps
    input_file.nps = int(nr / TOTAL)

    input_file.random_seed = np.random.randint(0, 1 << 63)

    output_files = f"outp={RUN_NAME}.o"
    if input_file.has_ptrac():
        output_files += f" ptrac={RUN_NAME}.ptrac"
    input_file.message = mt.InputLine(f"message: {output_files}", "")

    OUTPUT_FILE = SIM_DIR / f"{RUN_NAME}.i"

    with OUTPUT_FILE.open("w") as f:
        f.write(input_file.to_mcnp())

    if shutil.which("mcnp6") is None:
        print("[red]ERROR[/] Cannot find MCNP6 program.")
        sys.exit(3)

    command_to_run = f"mcnp6 i={OUTPUT_FILE.name}"
    if DRY_RUN:
        print("[yellow]INFO[/] Would run:")
        print(f"   {command_to_run}")
    else:
        subprocess.run(command_to_run, cwd=SIM_DIR, shell=True)


if __name__ == "__main__":
    main()
