from pathlib import Path
import nibabel as nib
import numpy as np

dataset_path = Path(r"C:\Users\megha\Downloads\BraTS\BraTS2021_Training_Data")

patients = [p for p in dataset_path.iterdir() if p.is_dir()]

counts = []

for patient in patients:
    seg = nib.load(list(patient.glob("*_seg.nii.gz"))[0]).get_fdata()

    count = 0
    for i in range(seg.shape[2]):
        if np.any(seg[:, :, i] > 0):
            count += 1

    counts.append(count)

print("Patients:", len(counts))
print("Min tumor slices:", min(counts))
print("Max tumor slices:", max(counts))
print("Average tumor slices:", np.mean(counts))