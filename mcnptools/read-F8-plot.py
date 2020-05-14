"""
step x: read in final output and plot
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mcnpio as io

file_delay = "Moon/test1-F4/png_moon_all_V2_F8_delay_1e8.o"
file_prompt = "Moon/test1-F4/png_moon_all_V2_F8_prompt_1e8.o"

dfd = io.read_output(file_delay, tally=8, n=1, tally_type="e", particle="p")  # delayed
dfp = io.read_output(file_prompt, tally=8, n=1, tally_type="e", particle="p")  # prompt

plt.figure()
plt.plot(dfd.energy, dfd.cts, label="Delayed: 51 - 200 us")
plt.plot(dfp.energy, dfp.cts, label="Prompt: 0 - 50 us")
plt.xlim([0.3, 10])
plt.yscale("log")
plt.xlabel("Energy [MeV]")
plt.legend()
