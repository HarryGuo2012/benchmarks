#!/bin/bash
# task.slurm
#SBATCH --job-name=download_benchmarks
#SBATCH --mail-type=end
#SBATCH --mail-user=yi.zhou@univ-angers.fr
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --time=10:0:0
#SBATCH --mem-per-cpu=3G

# Dynamic Linking Library
# export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/yi.zhou/Gurobi_Env/gurobi811/linux64/lib

# your bash script
# you could give the control to python or whatever you like

# doms=("asn" "bio" "bn" "ca" "chem" "cit" "eco" "econ" "email" "graph500" "heter" "ia" "inf" "labeled" "massive" "power" "proximity" "rand" "rec" "road" "rt" "sc" "soc" "socfb" "tech" "web" "dynamic" "tscc" "bhoslib" "dimacs" "dimacs10" "mldata")

# dom=${doms[$SLURM_ARRAY_TASK_ID]}

# python3 main.py $dom

python3 main.py $1
