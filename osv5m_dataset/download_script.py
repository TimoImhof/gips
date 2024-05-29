from huggingface_hub import snapshot_download
import os

from dotenv import load_dotenv
load_dotenv()

local_dir = os.getenv('LOCAL_DIR')

# Residual script copied from: https://github.com/gastruc/osv5m/blob/main/scripts/download-dataset.py
snapshot_download(repo_id="osv5m/osv5m", local_dir=local_dir, repo_type='dataset')

# extract the dataset
import os
import zipfile
for root, dirs, files in os.walk(local_dir):
    for file in files:
        if file.endswith(".zip"):
            with zipfile.ZipFile(os.path.join(root, file), 'r') as zip_ref:
                zip_ref.extractall(root)
                os.remove(os.path.join(root, file))
