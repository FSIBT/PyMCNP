"""
Helper class to write MCNP input files
"""
import numpy as np
import matplotlib.pyplot as plt
import os
from pathlib import Path


class MCNPwrite:
    def __init__(self, fileName):
        self.fileName = fileName
        self.path = Path.cwd() / fileName
        # check if fileName exists, and if not, create one
        if os.path.isfile(self.path):
            print(f"Existing file found in {self.path}")
        else:
            open(self.path, "a").close()
            print(f"No filename found. Creating one in {self.path}")
        # load file in memory and remove newline character
        with open(self.path) as f:
            file_str = f.readlines()
        self.file_lst = [line.rstrip("\n") for line in file_str]

    def save_to_file(self, new_file=None):
        if new_file is None:  # replace existing file
            with open(self.path, "w", newline="\n") as f:
                f.writelines(["%s\n" % line for line in self.file_lst])
        else:
            with open(new_file, "w", newline="\n") as f:
                f.writelines(["%s\n" % line for line in self.file_lst])

    def write_mcnp_line(self, line, pos=-1, char_limit=60):
        """
        Writes line to a position in a file. 0:start of file,
        -1: end of file, int: line number.
        after char_limit exceeded, append & and continue in next line.
        """
        line = str(line)
        if len(line) >= char_limit:
            tmp = line.split()
            n = len(line) // char_limit + 1
            # chunk_length = int(np.ceil(len(tmp)/n))
            spl = np.array_split(tmp, n)
            if pos == -1:
                for el in spl:
                    l = list(el)
                    l.append("&")
                    l_str = " ".join(l)
                    self.file_lst.append(l_str)
            else:
                for el in spl:
                    l = list(el)
                    l.append("&")
                    l_str = " ".join(l)
                    self.file_lst.insert(pos, l_str)
            # remove last & symbol
            self.file_lst[-1] = self.file_lst[-1][:-2]
        else:
            self.file_lst.append(line)
