from pathlib import Path
import nibabel as nib
import numpy as np

dataset_path = Path(r"C:\Users\megha\Downloads\BraTS\BraTS2021_Training_Data")

patient = [p for p in dataset_path.iterdir() if p.is_dir()][0]

print("Patient:", patient.name)

seg = nib.load(list(patient.glob("*_seg.nii.gz"))[0]).get_fdata()

count = 0

for i in range(seg.shape[2]):
    if np.any(seg[:, :, i] > 0):
        count += 1

print("Tumor-containing slices:", count)