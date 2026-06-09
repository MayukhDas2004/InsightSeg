from pathlib import Path
import nibabel as nib
import numpy as np

dataset_path = Path(r"C:\Users\megha\Downloads\BraTS\BraTS2021_Training_Data")

patient = [p for p in dataset_path.iterdir() if p.is_dir()][0]

seg = nib.load(list(patient.glob("*_seg.nii.gz"))[0]).get_fdata()

labels, counts = np.unique(seg, return_counts=True)

for label, count in zip(labels, counts):
    print(f"Label {int(label)}: {count}")