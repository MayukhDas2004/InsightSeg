from pathlib import Path
import nibabel as nib
import numpy as np

dataset_path = Path(r"C:\Users\megha\Downloads\BraTS\BraTS2021_Training_Data")

patient = [p for p in dataset_path.iterdir() if p.is_dir()][0]

seg = nib.load(list(patient.glob("*_seg.nii.gz"))[0]).get_fdata()

total_voxels = seg.size
tumor_voxels = np.sum(seg > 0)

print("Total voxels:", total_voxels)
print("Tumor voxels:", tumor_voxels)
print("Tumor percentage:", 100 * tumor_voxels / total_voxels)