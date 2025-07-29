#!/bin/bash -l

#SBATCH -A naiss2025-22-984
#SBATCH --job-name=cut_87.5%
#SBATCH --output=5.0_valid_87_5_flow_meas_laminar_trans.out
#SBATCH -p main
#SBATCH --ntasks 1
#SBATCH --time=0-10:00:00

module load bioinfo-tools

module load OpenFOAM/v1612+

echo \"libturbulenceModels.so\" > system/turbulenceLib

potentialFoam -initialiseUBCs -pName p -writep

pimpleFoam
