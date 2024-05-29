#!/usr/bin/env bash

#SBATCH --job-name=run_eval
#SBATCH --mail-user=timo.imhof.33@stud.tu-darmstadt.de
#SBATCH --output=/storage/ukp/work/imhof/gips/osv5m_github/run_eval.txt
#SBATCH --mail-type=ALL
#SBATCH --time=72:00:00
#SBATCH --partition=ukp
#SBATCH --cpus-per-task=1
#SBATCH --ntasks=1
#SBATCH --mem=128GB
#SBATCH --gpus=1

BASE_PATH="/storage/ukp/work/imhof/gips"

python3 ${BASE_PATH}/osv5m_github/evaluation.py exp=eval_best_model dataset.global_batch_size=1024
