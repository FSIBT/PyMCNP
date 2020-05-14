#!/bin/bash
# Job name:
#SBATCH --job-name=mcnp
#
# Partition:
#SBATCH --partition=lr5
#
# QoS:
#SBATCH --qos=lr_normal
#
# Account:
#SBATCH --account=pc_rootsapi
#
# Processors:
#SBATCH --nodes=1
#
# Wall clock limit:
#SBATCH --time=15:00:00
#

## Run command

module load intel
module load openmpi


export DATAPATH=/global/home/groups-sw/pc_rootsapi/MCNP/MCNP_DATA
/global/home/groups-sw/pc_rootsapi/MCNP/MCNP_CODE/MCNP6/bin/linux/mcnp6_linux_x86_64_omp i=MCNP-F1-sample.i o=MCNP-Fi-sample.o