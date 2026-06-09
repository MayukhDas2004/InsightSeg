from pathlib import Path
import nibabel as nib
import numpy as np

dataset_path = Path(r"C:\Users\megha\Downloads\BraTS\BraTS2021_Training_Data")

patient = [p for p in dataset_path.iterdir() if p.is_dir()][0]

flair = nib.load(list(patient.glob("*_flair.nii.gz"))[0]).get_fdata()
t1 = nib.load(list(patient.glob("*_t1.nii.gz"))[0]).get_fdata()
t1ce = nib.load(list(patient.glob("*_t1ce.nii.gz"))[0]).get_fdata()
t2 = nib.load(list(patient.glob("*_t2.nii.gz"))[0]).get_fdata()

image = np.stack([flair, t1, t1ce, t2], axis=-1)

print("Combined shape:", image.shape)