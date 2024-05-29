#!/usr/bin/env bash

#SBATCH --job-name=prep_data
#SBATCH --mail-user=timo.imhof.33@stud.tu-darmstadt.de
#SBATCH --output=/storage/ukp/work/imhof/gips/experiments/image_captioning.txt
#SBATCH --mail-type=ALL
#SBATCH --time=72:00:00
#SBATCH --partition=ukp
#SBATCH --cpus-per-task=1
#SBATCH --ntasks=1
#SBATCH --mem=128GB

BASE_PATH="/storage/ukp/work/imhof/gips"

python3 ${BASE_PATH}/experiments/image_captioning.py
