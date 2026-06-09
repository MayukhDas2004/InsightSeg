from pathlib import Path
import nibabel as nib
import numpy as np

dataset_path = Path(r"C:\Users\megha\Downloads\BraTS\BraTS2021_Training_Data")

patient = [p for p in dataset_path.iterdir() if p.is_dir()][0]

# Load modalities
flair = nib.load(list(patient.glob("*_flair.nii.gz"))[0]).get_fdata()
t1 = nib.load(list(patient.glob("*_t1.nii.gz"))[0]).get_fdata()
t1ce = nib.load(list(patient.glob("*_t1ce.nii.gz"))[0]).get_fdata()
t2 = nib.load(list(patient.glob("*_t2.nii.gz"))[0]).get_fdata()

# Load mask
seg = nib.load(list(patient.glob("*_seg.nii.gz"))[0]).get_fdata()

# Normalize each modality separately
def normalize(img):
    return (img - np.mean(img)) / np.std(img)

flair = normalize(flair)
t1 = normalize(t1)
t1ce = normalize(t1ce)
t2 = normalize(t2)

# Stack into 4-channel image
image = np.stack([flair, t1, t1ce, t2], axis=-1)

print("Image shape:", image.shape)
print("Mask shape:", seg.shape)
print("Image dtype:", image.dtype)
print("Mask labels:", np.unique(seg))