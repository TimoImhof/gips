#!/usr/bin/env bash

#SBATCH --job-name=run_eval
#SBATCH --mail-user=timo.imhof.33@stud.tu-darmstadt.de
#SBATCH --output=/storage/ukp/work/imhof/gips/osv5m/run_eval.txt
#SBATCH --mail-type=ALL
#SBATCH --time=72:00:00
#SBATCH --partition=ukp
#SBATCH --cpus-per-task=16
#SBATCH --ntasks=1
#SBATCH --mem=256GB
#SBATCH --gpus=4
#SBATCH --constraint="gpu_mem:32gb"

BASE_PATH="/storage/ukp/work/imhof/gips/osv5m"

python3 ${BASE_PATH}/evaluation.py exp=eval_best_model dataset.global_batch_size=1024
