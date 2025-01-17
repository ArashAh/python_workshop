#!/bin/bash
#SBATCH --job-name=pandas_plots
#SBATCH --account=ec12
#SBATCH --time=00:30:00
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=4G
#SBATCH --output=pandas_plots_%j.out
#SBATCH --error=pandas_plots_%j.err

# Load necessary modules
module purge
module load SciPy-bundle/2024.05-gfbf-2024a
module load matplotlib/3.7.2-gfbf-2023a
# Activate virtual environment if needed
# source /path/to/your/venv/bin/activate

# Run the Python script
python pandas_plots.py
