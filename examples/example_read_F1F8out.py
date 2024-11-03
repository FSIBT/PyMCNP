"""
Example to read simple energy output files with possibly more than one tally
and subtallies
"""

import pymcnp
import matplotlib.pyplot as plt

file = 'data/output_files/F1F8.o'
out = pymcnp.outp.ReadOutput(file)
print(out.get_runtime())

# store tally information
df_info = out.df_info
print(df_info.head(5))

# Based on df_info, choose desired tally
df1 = out.read_tally(n=1)
print(df1.head(5))

df8 = out.read_tally(n=6)
df18 = out.read_tally(n=7)

plt.figure()
plt.plot(df1['energy'], df1['cts'], label='F1')
plt.plot(df18['energy'], df18['cts'], label='F8')
plt.plot(df8['energy'], df8['cts'], label='F8 + GEB')
plt.xlabel('Energy (MeV)')
plt.ylabel('Counts')
plt.legend()
