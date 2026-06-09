from pathlib import Path
import nibabel as nib
import numpy as np

dataset_path = Path(r"C:\Users\megha\Downloads\BraTS\BraTS2021_Training_Data")

patients = [p for p in dataset_path.iterdir() if p.is_dir()]

total_slices = 0

for patient in patients:
    seg = nib.load(list(patient.glob("*_seg.nii.gz"))[0]).get_fdata()

    for i in range(seg.shape[2]):
        if np.any(seg[:, :, i] > 0):
            total_slices += 1

print("Total tumor-containing slices:", total_slices)
print("Average per patient:", total_slices / len(patients))