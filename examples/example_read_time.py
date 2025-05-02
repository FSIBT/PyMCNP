"""
Example to read a tally with time bins e.g. a pulsed neutron generator
"""

import pymcnp
import matplotlib.pyplot as plt

file = 'examples/data/outp/png.o'
out = pymcnp.outp.ReadOutput(file)

# information about tallies found
dfi = out.df_info
df = out.read_tally(n=0, mode='t')

plt.figure()
plt.plot(df['time'] * 1e-2, df['cts'])
plt.xlabel('Time (us)')
plt.ylabel('counts')
