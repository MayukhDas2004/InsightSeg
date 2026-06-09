from pathlib import Path
import nibabel as nib
import numpy as np

dataset_path = Path(r"C:\Users\megha\Downloads\BraTS\BraTS2021_Training_Data")

patient = [p for p in dataset_path.iterdir() if p.is_dir()][0]

flair = nib.load(list(patient.glob("*_flair.nii.gz"))[0]).get_fdata()

print("Minimum:", np.min(flair))
print("Maximum:", np.max(flair))
print("Mean:", np.mean(flair))
print("Standard Deviation:", np.std(flair))