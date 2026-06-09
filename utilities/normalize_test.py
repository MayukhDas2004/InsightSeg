from pathlib import Path
import nibabel as nib
import numpy as np

dataset_path = Path(r"C:\Users\megha\Downloads\BraTS\BraTS2021_Training_Data")

patient = [p for p in dataset_path.iterdir() if p.is_dir()][0]

flair = nib.load(list(patient.glob("*_flair.nii.gz"))[0]).get_fdata()

normalized = (flair - np.mean(flair)) / np.std(flair)

print("New Mean:", np.mean(normalized))
print("New Std:", np.std(normalized))
print("New Min:", np.min(normalized))
print("New Max:", np.max(normalized))